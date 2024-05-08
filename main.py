import csv
import requests
from bs4 import BeautifulSoup

proxies = {
    "http":  "http://scraperapi:c7175bbc61fe138f6fa85049901a8283@proxy-server.scraperapi.com:8001",
    "https": "http://scraperapi:c7175bbc61fe138f6fa85049901a8283@proxy-server.scraperapi.com:8001"
}
def csv_function_writer(RestName, RestRating):
    with open('restaurants.csv', 'a', newline='') as file:
        fieldnames = ["NAME", "RATING"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow({"NAME": RestName, "RATING": RestRating})

                         

r = requests.get('https://www.swiggy.com/city/kolkata', proxies=proxies, verify=False)
soup = BeautifulSoup(r.text, 'html.parser')

restaurant_elements = soup.find_all('div', class_="styled__StyledRestaurantGridCard-sc-fcg6mi-0 lgOeYp")

if restaurant_elements:
    for restaurant in restaurant_elements:
        restaurant_name = restaurant.find('div', class_="sc-beySbM lfjhyG").text.strip()
        rating = restaurant.find('span', class_='sc-beySbM jdpFZn').text.strip()


        print(f'Restaurant Name: {restaurant_name}')
        print(f'Rating: {rating}')
        csv_function_writer(restaurant_name,rating)