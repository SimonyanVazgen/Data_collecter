from bs4 import BeautifulSoup
import requests
import csv

headers = {
    "User-Agent": "YOUR VERSION"
}

url = "https://forexample.com"
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "lxml")

rows = soup.find("tbody").find_all("tr")

with open("data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["id", "name", "manufacturer", "country", "price", "old_price", "history", "update_date"])

    for row in rows:
        try:
            id_value = row.find("th").text.strip()
            name = row.find("td", {"data-title": "name"}).text.strip()

            country_full = row.find("td", {"data-title": "country"}).text.strip()
            parts = country_full.split(" ", 1)

            if len(parts) == 2:
                country = parts[0]
                factory = parts[1]
            else:
                country = country_full
                factory = "Null"

            cost = row.find("td", {"data-title": "price"}).text.strip()

            old_cost_tag = row.find("td", {"data-title": "old_price"})
            old_cost = old_cost_tag.text.strip() if old_cost_tag else ""

            writer.writerow([id_value, name, factory, country, cost, old_cost])

        except Exception:
            continue