def describe_city(City, Country):
    if Country == "":
        Country = 'China'
    print(f"{City.title()} is in {Country.title()}")

describe_city('London', 'England')
describe_city('Cairo', '')
describe_city('Paris', '')
