def city_country(City, Country):
    return f'{City}, {Country}'
for i in range(3):
    cities = input("Please enter the name of a city: ")
    countries = input("Please enter the name of the country: ")
    x = city_country(cities, countries)
    print(x)
