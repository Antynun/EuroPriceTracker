import requests
from bs4 import BeautifulSoup
import time
from plyer import notification

initial_price = None

def get_product_price(url):
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            price_element = soup.select_one('#calculator > div:nth-child(1) > div:nth-child(2) > div > div > div:nth-child(2) > div:nth-child(1) > h3 > span:nth-child(2) > span')
            
            if price_element:
                price_text = price_element.get_text().strip()
                # Remove comma from price text
                price_text = price_text.replace(',', '')
                # Convert price to decimal format
                price_decimal = float(price_text) / 1000
                return price_decimal
            else:
                return "Price not found"
        else:
            print("Error: Unable to retrieve page.")
    except Exception as e:
        print("An error occurred while fetching the product price:", str(e))

product_url = "https://wise.com/br/currency-converter/eur-to-brl-rate?amount=1"

initial_price = get_product_price(product_url)
notification.notify(
    title='Wise Price Check',
    message=f'EUR price is: {initial_price:.3f}',
    timeout=10
)

while True:
    product_price = get_product_price(product_url)
    
    print("EUR price is:", product_price)
    
    if initial_price is not None:
        percentage_change = ((product_price - initial_price) / initial_price) * 100
        print("Daily Variation:", percentage_change)
        
        notification.notify(
            title='Wise Price Check',
            message=f'EUR price is: {product_price:.3f}\nDaily Variation: {percentage_change:.2f}%',
            timeout=10
        )
        
    time.sleep(3600)
