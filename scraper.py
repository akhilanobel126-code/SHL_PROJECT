import requests
from bs4 import BeautifulSoup
import json
import time

url = "https://www.shl.com/solutions/products/product-catalog/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

links = soup.find_all("a")

data = []

for link in links:

    href = link.get("href")

    if href and "/products/product-catalog/view/" in href:

        name = link.text.strip()

        full_url = "https://www.shl.com" + href

        page = requests.get(full_url, headers=headers)

        page_soup = BeautifulSoup(page.text, "html.parser")
        desc_tag = page_soup.find("p")
        description = desc_tag.text.strip() if desc_tag else "No description"

        paragraphs = page_soup.find_all("p")

description = ""

for p in paragraphs:
    text = p.text.strip()

    if (
        text
        and "upgrade to a modern browser" not in text.lower()
        and len(text) > 50
    ):
        description = text
        break

        item = {
            "name": name,
            "url": full_url,
            "description": description
        }

        data.append(item)

        print("Saved:", name)

        time.sleep(1)

with open("catalog.json", "w") as f:

    json.dump(data, f, indent=4)

print("All data saved")
