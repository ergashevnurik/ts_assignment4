# Example 1

import requests

# Sample URL for testing
url = "https://httpbin.org/anything"

# 1. GET request
response_get = requests.get(url)
print("GET Response:", response_get.json())

# 2. POST request
data = {"key": "value"}
response_post = requests.post(url, json=data)
print("POST Response:", response_post.json())

# 3. PUT request
response_put = requests.put(url, json={"update": "new_value"})
print("PUT Response:", response_put.json())

# 4. DELETE request
response_delete = requests.delete(url)
print("DELETE Response:", response_delete.status_code)

# 5. HEAD request
response_head = requests.head(url)
print("HEAD Response Headers:", response_head.headers)

# 6. OPTIONS request
response_options = requests.options(url)
print("OPTIONS Response Allow:", response_options.headers.get('allow'))

# 7. PATCH request
response_patch = requests.patch(url, json={"key": "patched_value"})
print("PATCH Response:", response_patch.json())

# Parameters Example
headers = {'User-Agent': 'custom-agent'}
params = {'search': 'example'}
cookies = {'session_id': '12345'}
response_with_params = requests.get(url, headers=headers, params=params, cookies=cookies)
print("Custom Headers and Params Response:", response_with_params.json())

# Example 2
import requests

# Google search simulation (use Bing or DuckDuckGo for actual crawling due to restrictions)
url = "https://www.google.com/search"
params = {'q': 'Python programming'}

response = requests.get(url, params=params)
print("--------------------------------------")
print("Search URL:", response.url)
print("Response Status:", response.status_code)

# Example 3
import os
import requests

# Create a folder for storing images
os.makedirs('images', exist_ok=True)

# List of image URLs
image_urls = [
    "https://via.placeholder.com/150",
    "https://via.placeholder.com/300"
]

# Crawl and save images
for idx, img_url in enumerate(image_urls):
    response = requests.get(img_url)
    if response.status_code == 200:
        with open(f'images/image_{idx}.jpg', 'wb') as f:
            f.write(response.content)
        print("-------------------")
        print(f"Image {idx} saved.")

# Example 4
import requests
from bs4 import BeautifulSoup

# URL for university rankings
url = "https://www.shanghairanking.com/rankings/arwu/2023"

# Step 1: Fetch the webpage
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Step 2: Parse the rankings
rankings = []
rows = soup.select('table tbody tr')
for row in rows:
    rank = row.select_one('.ranking').text.strip()
    name = row.select_one('.univ-name').text.strip()
    td_elements = row.find_all('td', attrs={"data-v-ae1ab4a8": True})
    score = td_elements[-1].text.strip() if td_elements else "N/A"  # Get the last matching <td>
    rankings.append((rank, name, score))

# Step 3: Display rankings
print("---------------------------------------------------------")
print("{:<5} {:<50} {:<10}".format("Rank", "University", "Score"))
for rank, name, score in rankings:
    print(f"{rank:<5} {name:<50} {score:<10}")


# Example 5
import requests
from bs4 import BeautifulSoup

# Sample e-commerce site
url = "https://www.euronics.lv/ru/telefony"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Extract product information
products = soup.select('.product-card')
for product in products:
    name = product.select_one('.product-card__title').text.strip()
    price = product.select_one('.product-card__price .price').text.strip()
    print("--------------------------------")
    print(f"Product: {name}\nPrice: {price}")


# Example 6
import scrapy

class UniversitySpider(scrapy.Spider):
    name = "university"
    start_urls = ["https://www.shanghairanking.com/rankings/arwu/2023"]

    def parse(self, response):
        for row in response.css('table tbody tr'):
            rank = row.css('.ranking::text').get()
            name = row.css('.univ-name::text').get()
            yield {"Rank": rank, "University": name}
