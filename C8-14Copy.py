def make_bike (manufacturer, model, **add_Info):
    bikeInfo = {'bikeManufacturer' : manufacturer, 'name' : model, 'bikeSafetyFeatures' : safetyFeatures, 'engineSystem' : engineType}
    bikeInfo['color'] = input("Please enter bike color: ")
    bikeInfo['transmission'] = input("Please enter the transmission type: ")
    for key, value in add_Info.items():
        bikeInfo[key] = value
    return bikeInfo

    #main program
manufacturer = input("Please enter the bike manufacturer: ")
model = input("Please enter the model name: ")
safetyFeatures = input("Please enter the safety features on your bike: ")
engineType = input("Please enter the type of engine: ")
bike = make_bike(manufacturer, model, safetyFeatures = safetyFeatures, engineType = engineType)
print(bike)
