def carsData():
    cars = ['BMW','Ford','Fortuner','RollsRoyce','Benz','maruti']
    cars.append('Jaguar')
    for car in cars:
        if(car.__eq__('maruti')):
            #cars[cars.index(car)] = 'Tata' # update element
            cars.remove(car) # remove element
    print(cars)
    cars.sort()
    print(cars)              
              
carsData();


