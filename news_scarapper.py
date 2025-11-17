import requests
from bs4 import BeautifulSoup
import time

# requesting the website

url = "https://www.bbc.com/news"

response = requests.get(url)
print("The response code is : " , response)

#parsese the HTML document

soup = BeautifulSoup(response.content,'html.parser')

# Extract the new from html
headlines = soup.find_all('h2')

# Display the headlines

for headline in headlines:
    print(headline.text,"\n")
    time.sleep(4)