def make_car (manufacturer, model, **add_Info):
    carInfo = {'carManufacturer' : manufacturer, 'name' : model}
    carInfo['color'] = input("Please enter car color: ")
    carInfo['transmission'] = input("Please enter the transmission type: ")
    for key, value in add_Info.items():
        carInfo[key] = value
    return carInfo

    #main program
manufacturer = input("Please enter the car manufacturer: ")
model = input("Please enter the model name: ")
car = make_car(manufacturer, model, camera = 360, seats = 'leather')
print(car)
