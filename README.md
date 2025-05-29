```markdown
# Open Library Book Recommendation System

A Python-based interactive command-line tool that allows users to search, browse and get detailed information about books using the Open Library API.

## Features

- Search books by keywords
- Browse books by subject categories
- Get detailed book information
- Auto-save search results to CSV files
- User-friendly command-line interface

## Installation

1. Clone this repository:

https://github.com/JasonZhao-Zzz/Python-Project-Submission/tree/1b6ac58c78648cfeebdbdeaaf2d201cb0ef4f355/V1


2. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

Run the main script:
```bash
python main.py
```

The system provides four main options:
1. **Search Books**: Search books by keywords with customizable result limits
2. **Browse Books by Subject**: Find books in specific subject categories
3. **Get Book Details**: Get detailed information about a specific book
4. **Exit**: Close the program

### Example Usage:
```bash
=== Open Library Book Recommendation System ===
1. Search Books
2. Browse Books by Subject
3. Get Book Details
4. Exit

Please select an option (1-4): 1
Enter search keyword: Python Programming
How many books to return (default 20): 10
```

## Dependencies

- Python 3.6+
- pandas
- requests
- logging (built-in)
- os (built-in)

## Project Structure

```
open-library-book-recommender/
├── main.py
├── data_collector.py
├── requirements.txt
├── book_list_result/
└── README.md
```

## Data Storage

Search results are automatically saved in CSV format in the `book_list_result` directory, with filenames based on search queries or subjects.

## Error Handling

The system includes comprehensive error handling for:
- Data collection errors
- Invalid user inputs
- API connection issues
- File saving operations


## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

[janzhao@]
- GitHub: [@JasonZhao-Zzz]
- Email: 1534246554@qq.com

## Acknowledgments

- Open Library API for providing the book data
- Contributors and maintainers of the pandas library
```
