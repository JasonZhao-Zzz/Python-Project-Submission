# Python-Project-Submission
This code implements a Book Recommendation System that interfaces with the Open Library API. Here are its key features and components:

    System Architecture:

    The code defines custom exceptions for error handling (DataCollectionError and InvalidInputError)
    Utilizes logging for error tracking
    Contains helper functions for displaying book information
    Implements a main interactive loop for user interaction

    Main Functionality: The system offers four primary options:

    Search Books: Allows users to search for books using keywords
    Browse Books by Subject: Enables browsing books by specific subjects
    Get Book Details: Provides detailed information about a specific book
    Exit: Terminates the program

    Key Features:

    Data saving: Search results are automatically saved as CSV files in a 'book_list_result' directory
    Flexible search options: Users can specify the number of results they want to see
    Detailed book information: Displays various book attributes including:
        Title
        Author(s)
        Publication year
        Subject categories

    User Interface:

    Implements a command-line interface with numbered menu options
    Provides clear prompts for user input
    Displays formatted book information in an easy-to-read manner

    Error Handling:

    Includes comprehensive error handling through try-except blocks
    Logs errors for debugging purposes
    Provides user-friendly error messages

The code is designed to be user-friendly while providing robust functionality for searching and exploring books through the Open Library platform.
