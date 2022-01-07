import requests
import BeautifulSoup4 as BeautifulSoup

data = requests.get('https://darksky.net/forecast/45.3836,-122.7581/us12/en')
data.text
soup = BeautifulSoup(data.text, 'html.parser')
soup.prettify()