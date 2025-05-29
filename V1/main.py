#janzhao@
import os
from data_collector import OpenLibraryCollector
import logging
class DataCollectionError(Exception):
    """Exception raised for errors in data collection process"""
    pass
class InvalidInputError(Exception):
    """Exception raised for invalid user input"""
    pass


logging.basicConfig(level=logging.INFO)


def display_book_info(book):
    """Display book information"""
    print("\n=== Book Information ===")
    for key, value in book.items():
        if value and key != 'work_id':
            print(f"{key.replace('_', ' ').title()}: {value}")


def main():
    try:
        # use imported collector class to collect data from Open Library API
        collector = OpenLibraryCollector()
        #provide user with options to search for books, browse by subject, or get book details
        while True:
            print("\n=== Open Library Book Recommendation System ===")
            print("1. Search Books")
            print("2. Browse Books by Subject")
            print("3. Get Book Details")
            print("4. Exit")

            choice = input("Please select an option (1-4): ")
            # validate user input
            if choice == "1":
                query = input("Enter search keyword: ")
                limit = int(input("How many books to return (default 20): ") or "20")
                # search for books and display results
                books_df = collector.search_books(query, limit)
                # save search results to file
                book_file_path = os.path.join(os.getcwd(), 'book_list_result', query + '.csv')
                collector.save_data_to_file(books_df, book_file_path)
                print(f"\nFound {len(books_df)} books:")
                for idx, book in books_df.iterrows():
                    print(f"\n{idx + 1}. {book['title']} by {book['authors']}")
                    if book['first_publish_year']:
                        print(f"   Published: {book['first_publish_year']}")
                    if book['subjects']:
                        print(f"   Subjects: {', '.join(book['subjects'])}")

            elif choice == "2":
                subject = input("Enter subject keyword: ")
                limit = int(input("How many books to return (default 20): ") or "20")

                books_df = collector.collect_books_by_subject(subject, limit)
                # save search results to file
                book_file_path = os.path.join(os.getcwd(), 'book_list_result', subject + '.csv')
                collector.save_data_to_file(books_df, book_file_path)
                print(f"\nFound {len(books_df)} books:")
                for idx, book in books_df.iterrows():
                    print(f"\n{idx + 1}. {book['title']} by {book['authors']}")
                    if book['first_publish_year']:
                        print(f"   Published: {book['first_publish_year']}")

            elif choice == "3":
                # First search for the book
                query = input("Enter book title to search: ")

                books_df = collector.search_books(query, 5)

                print("\nSearch Results:")
                for idx, book in books_df.iterrows():
                    print(f"{idx + 1}. {book['title']} by {book['authors']}")

                book_idx = int(input("\nSelect book number for details (1-5): ")) - 1
                if 0 <= book_idx < len(books_df):
                    work_id = books_df.iloc[book_idx]['work_id']
                    book_details = collector.get_book_details(work_id)
                    display_book_info(book_details)
                else:
                    print("Invalid selection")

            elif choice == "4":
                print("Thank you for using the system! Goodbye!")
                break

            else:
                print("Invalid choice, please try again.")

    except Exception as e:
        logging.error(f"Program error: {str(e)}")
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
