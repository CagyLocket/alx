import requests
from bs4 import BeautifulSoup


page = requests.get("https://www.alx.pl/")
soup = BeautifulSoup(page.content, "html.parser")
soup = soup.find("ul", {"class", "main-nav"})
soup = soup.find("li")
soup = soup.find_all("a")
for i in soup:
    print(i.get_text())
