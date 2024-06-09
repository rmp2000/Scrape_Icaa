# ICAA Film Data Scraper

This project is a web scraping tool designed to extract film data from the ICAA (Instituto de la Cinematografía y de las Artes Audiovisuales) website. The tool is implemented using Python and utilizes libraries such as `requests`, `BeautifulSoup`, and `selenium` to automate the data extraction process. The extracted data is saved into Excel files for further analysis.

## Features

- Scrapes film data for a specified range of years.
- Handles pagination and dynamic content loading using Selenium.
- Utilizes multiple User-Agent strings to avoid detection and blocking.
- Includes robust error handling and retry mechanisms.
- Saves the extracted data into well-structured Excel files.

## Prerequisites

- Python 3.x
- Google Chrome browser
- ChromeDriver (ensure it matches your Chrome version)

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/icaa-film-scraper.git
   cd icaa-film-scraper
    ```
## Installation

Install the required Python packages:

```bash
pip install -r requirements.txt
```

Download ChromeDriver and add it to your system's PATH.

## Usage


```bash
python main.py
```

### Example
```bash
python main.py YEAR
```
This will scrape film data from the specified URL for the year desire(default year is 2024), and save the results into an Excel file named `icaa_year.xlsx` in the `excel_final` directory.

## Project Structure

- `main.py`: Main script to run the scraper.
- `clean_data_frame.py` : Clean the data frame.
- `scrap_page.py`: Contains the core scraping functions.
- `setap_page.py` : Make the setap to star the scraping
- `requirements.txt`: List of required Python packages.
- `excel_final/`: Directory where the resulting Excel files are saved.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgements

This project uses the following libraries:

- Requests
- BeautifulSoup
- Selenium

## Contact

For any questions or suggestions, please contact rmartinezpeinado@example.com.
