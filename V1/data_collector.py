# janzhao@
import requests
import pandas as pd
import time
from typing import List, Dict
import logging
import os

class DataCollectionError(Exception):
    """Exception raised for errors in data collection process"""
    pass

# Define a class for collecting data from Open Library API
class OpenLibraryCollector:
    def __init__(self):
        self.search_url = "http://openlibrary.org/search.json"
        self.works_url = "https://openlibrary.org/works/{}.json"
        self.books_url = "https://openlibrary.org/api/books"
    # serach books by keyword
    def search_books(self, query: str, limit: int = 20) -> pd.DataFrame:
        """
        Search for books and return basic information
        Args:
            query: Search keyword
            limit: Number of results to return
        Returns:
            DataFrame containing book information
        """
        try:
            params = {
                'q': query,
                'limit': limit
            }

            response = requests.get(self.search_url, params=params)
            response.raise_for_status()

            data = response.json()
            books_data = []

            for book in data.get('docs', []):
                book_info = {
                    'title': book.get('title', ''),
                    'authors': ', '.join(book.get('author_name', ['Unknown'])),
                    'work_id': book.get('key', '').split('/')[-1],
                    'first_publish_year': book.get('first_publish_year', ''),
                    'language': book.get('language', [''])[0] if book.get('language') else '',
                    'subjects': ', '.join(book.get('subject', []))[:100],  # Get first 3 subjects, max 100 chars
                    'number_of_pages': book.get('number_of_pages_median', ''),
                    'edition_count': book.get('edition_count', '')  # Using edition_count as popularity measure
                }
                books_data.append(book_info)

            return pd.DataFrame(books_data)

        except Exception as e:
            logging.error(f"Error searching books: {str(e)}")
            raise DataCollectionError(f"Error searching books: {str(e)}")
    # get detailed information for a single book
    def get_book_details(self, work_id: str) -> Dict:
        """
        Get detailed information for a single book
        Args:
            work_id: Open Library work ID
        Returns:
            Dictionary containing detailed book information
        """
        try:
            response = requests.get(self.works_url.format(work_id))
            response.raise_for_status()

            book_data = response.json()

            return {
                'title': book_data.get('title', ''),
                'description': book_data.get('description', {}).get('value', '')
                if isinstance(book_data.get('description'), dict)
                else book_data.get('description', ''),
                'subjects': ', '.join(book_data.get('subjects', []))[:100],  # Get first 3 subjects, max 100 chars
                'cover_id': book_data.get('covers', [None])[0],
                'first_publish_date': book_data.get('first_publish_date', ''),
                'edition_count': book_data.get('edition_count', '')  # Using edition_count as popularity measure
            }

        except Exception as e:
            logging.error(f"Error getting book details: {str(e)}")
            raise DataCollectionError(f"Error getting book details: {str(e)}")
    # search books by subject
    def collect_books_by_subject(self, subject: str, limit: int = 20) -> pd.DataFrame:
        """
        Collect books by subject
        Args:
            subject: Subject keyword
            limit: Number of results to return
        Returns:
            DataFrame containing books of the specified subject
        """
        try:
            params = {
                'subject': subject,
                'limit': limit
            }

            response = requests.get(self.search_url, params=params)
            response.raise_for_status()

            data = response.json()
            books_data = []

            for book in data.get('docs', []):
                book_info = {
                    'title': book.get('title', ''),
                    'authors': ', '.join(book.get('author_name', ['Unknown'])),
                    'first_publish_year': book.get('first_publish_year', ''),
                    'language': book.get('language', [''])[0] if book.get('language') else '',
                    'subjects': ', '.join(book.get('subject', []))[:100],  # Get first 3 subjects, max 100 chars
                    'subject': subject,
                    'edition_count': book.get('edition_count', '')  # Using edition_count as popularity measure
                }
                books_data.append(book_info)

            return pd.DataFrame(books_data)

        except Exception as e:
            logging.error(f"Error collecting books by subject: {str(e)}")
            raise DataCollectionError(f"Error collecting books by subject: {str(e)}")
    # save data to file
    def save_data_to_file(self, df: pd.DataFrame, filename: str) -> None:
        """
        Save DataFrame to CSV file, appending if file exists
        Args:
            df: DataFrame containing book information
            filename: CSV filename to save to
        """
        try:
            # Check if the file exists
            if os.path.exists(filename):
                # Append to the existing file without writing the header
                df.to_csv(filename, mode='a', header=False, index=False)
            else:
                # Create a new file with the header
                df.to_csv(filename, index=False)

        except Exception as e:
            logging.error(f"Error saving data to file: {str(e)}")
            raise DataCollectionError(f"Error saving data to file: {str(e)}")


# Usage example
if __name__ == "__main__":
    #Below code is for testing the data_collector.py file
    collector = OpenLibraryCollector()

    # Search books
    df_search = collector.search_books(query="Python")
    collector.save_data_to_file(df_search, "search_books.csv")

    # Collect books by subject
    df_subject = collector.collect_books_by_subject(subject="Science Fiction")
    collector.save_data_to_file(df_subject, "subject_books.csv")