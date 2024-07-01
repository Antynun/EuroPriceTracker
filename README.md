# Wise EUR to BRL Price Tracker

This Python program monitors the exchange rate of EUR to BRL from Wise.com and provides notifications about the current price and its daily variation. The script fetches the exchange rate at regular intervals and alerts the user with updated information.

## Features

- **Web Scraping**: Utilizes `requests` and `BeautifulSoup` to extract the EUR to BRL exchange rate from Wise.com.
- **Notifications**: Sends desktop notifications using `plyer` to inform users of the current exchange rate and the percentage change from the initial price.
- **Periodic Updates**: Checks the exchange rate every hour and prints the current rate and daily variation to the console.

## How It Works

1. **Fetch Initial Price**: The script retrieves the initial exchange rate of EUR to BRL.
2. **Hourly Check**: Every hour, it checks the current exchange rate and calculates the percentage change from the initial price.
3. **Notifications**: Sends a desktop notification with the current exchange rate and daily variation.

## Installation

To run this program, you need to have Python and the following libraries installed:

- `requests`
- `beautifulsoup4`
- `plyer`

You can install the required libraries using pip:
```bash
pip install -r requirements.txt
```
## Usage

Clone the repository:
```bash
git clone https://github.com/yourusername/your-repository.git
```
Navigate to the directory:
```bash
cd your-repository
```
Run the script:
```bash
python main.py
```
The script will start monitoring the EUR to BRL exchange rate and notify you of any changes.


## Contributing

Contributions are welcome! If you have any improvements or feature suggestions, feel free to fork this repository, make your changes, and submit a pull request. For major changes, please open an issue first to discuss the proposed modifications.
