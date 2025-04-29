# Web Scraper for NHK Easy News

This project is a web scraper designed to extract news articles from the NHK Easy News website (https://www3.nhk.or.jp/news/easy/). The scraper respects the site's `robots.txt` file to ensure compliance with its scraping policies.

## Project Structure

```
web-scraper
├── src
│   ├── scraper.py        # Main logic for the web scraper
│   ├── utils
│   │   └── __init__.py   # Utility functions for the scraper
│   └── __init__.py       # Marks the src directory as a Python package
├── requirements.txt       # Dependencies for the project
├── .gitignore             # Files and directories to ignore by Git
├── README.md              # Documentation for the project
└── robots.txt             # Scraping permissions for the target website
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd web-scraper
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the web scraper, execute the following command:

```
python src/scraper.py
```

Make sure to check the `robots.txt` file included in the project to understand the scraping permissions for the NHK Easy News website.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.