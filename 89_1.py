import requests

dane = requests.get("https://api.chucknorris.io/jokes/categories")
x = dane.json()

print("### Żarty Chucka Norrisa ###")
print("Kategorie:")
for i in x:
    print(i, end=", ")

print()
category = input("Wybierz z jakiej kategorii, chciałbyś otrzymać losowy żart :)")

joke = requests.get(f"https://api.chucknorris.io/jokes/random?category={category}")
joke_show = joke.json()
# print(joke_show['value'])

joke_before = joke_show['value']
joke_after = joke_before.replace('Chuck Norris', 'Paweł Wrzesień')
print(joke_after)





