import numpy as np
from Car import Car
import pandas as pd

cars = []
ARRAY_SIZE = 44

def importCars():
    """"Returns a list of all cars that will be used"""
    # # car0: 2019 Mercedes A class sedan
    # cars.append(Car('2019 Mercedes A class sedan', 32500, 35, 'sedan', 'silver', 'gas', 188, 5, 'all', 'mercedes'))
    # # car1: 2019 Audi RS3
    # cars.append(Car('2019 Audi RS3', 56200, 28, 'sports', 'red', 'gas', 394, 5, 'all', 'audi'))
    # # car2: Ford F-150 XL
    # cars.append(Car('Ford F-150 XL', 29300, 26, 'truck', 'silver', 'gas', 325, 5, 'four', 'ford'))

    df = pd.read_excel('CarData.xlsx', sheet_name='Sheet1')
    names = df['Name']
    price = df['Price']
    hwyMPG = df['Highway MPG']
    size = df['Size']
    color = df['Color']
    fuel = df['Engine Fuel Type']
    hp = df['Horsepower']
    seats = df['Seats']
    wd = df['Wheel Drive']
    make = df['Make']
    carsNumber = len(names)
    i = 0
    while i < carsNumber:
        cars.append(Car(names[i], price[i], hwyMPG[i], size[i], color[i], fuel[i], hp[i], seats[i], wd[i], make[i]))
        i += 1
    return cars

def createAttrMatrix(carsList):
    """"Returns a 2d array where each column is the attribute list of a car,
    so rows=ARRAY_SIZE and columns=carsList.len"""
    attrMatrix = np.zeros((ARRAY_SIZE, len(carsList)))
    i = 0
    while i < len(carsList):
        attrMatrix[:, i] = np.transpose(carsList[i].getAttrs())
        i += 1
    return attrMatrix

def getBrowsingAttrs(n):
    """Returns list of n tuples (attr #, score) that comes from browsed cars and their respective times"""
    # browsedCars = []  # get list of cars browsed
    # times = np.array([])  # get arr of corresponding browsing times
    # # -------TEST VALUES-------
    # browsedCars.append(Car('2019 Mercedes A class sedan', 32500, 35, 'sedan', 'silver', 'gas', 188, 5, 'all', 'mercedes'))
    # times = np.array([1])
    # # -------TEST VALUES-------
    browsedCars = []
    times = []
    # read in file
    df = pd.read_excel('BrowsingAttrs.xlsx', sheet_name='Sheet1')
    names = df['Name']
    price = df['Price']
    hwyMPG = df['Highway MPG']
    size = df['Size']
    color = df['Color']
    fuel = df['Engine Fuel Type']
    hp = df['Horsepower']
    seats = df['Seats']
    wd = df['Wheel Drive']
    make = df['Make']
    timesList = df['Time']
    carsNumber = len(names)
    i = 0
    while i < carsNumber:
        browsedCars.append(Car(names[i], price[i], hwyMPG[i], size[i], color[i], fuel[i], hp[i], seats[i], wd[i], make[i]))
        times.append(timesList[i])
        i += 1
    # do calculations
    times = np.divide(times, sum(times))
    attrs = np.zeros((len(browsedCars), ARRAY_SIZE))
    i = 0
    while i < len(browsedCars):
        attrs[i, :] = browsedCars[i].getAttrs() * times[i]
        i += 1
    sumArr = np.sum(a=attrs, axis=0)
    sortedInd = np.flip(np.argsort(sumArr), 0)
    bestAttrs = []
    i = 0
    while i < n and sortedInd.size > i:
        attrInd = sortedInd[i]
        bestAttrs.append((attrInd, sumArr[attrInd]))
        i += 1
    return bestAttrs

def getPrefArr(attrs2boost):
    """"Returns an array of the weighted preferences associated with each attribute (prefArr.len=ARRAY_SIZE)"""
    # wp = np.zeros(ARRAY_SIZE)
    # # -------TEST VALUES-------
    # wp[3] = 2   # price 30<x<35
    # wp[11] = 1  # mpg 30<x<35
    # wp[12] = 1  # mpg 35<x<40
    # wp[14] = 1  # size = sedan
    # wp[19] = 1  # color = red
    # # -------TEST VALUES-------
    df = pd.read_excel('PrefArr.xlsx', sheet_name='Sheet1')
    wp = df['Attributes']
    # check scores of attrs2boost to only boost attrs with scores > .5
    for attr in attrs2boost:
        if attr[1] > .5:
            wp[attr[0]] += 1

    """"""""""""""""""""""""""""""""""""
    wp = np.divide(wp, sum(abs(wp)))
    return wp

def getScoreArray(attrMatrix, prefArr):
    """Calculates score array by:
         *multiplying attributes (rows) by corresponding weighted pref values
         *summing scores for each car (column)"""
    scoreArray = attrMatrix * prefArr[:, None]
    scoreArray = np.sum(a=scoreArray, axis=0)
    return scoreArray

def getBestCars(scoreArray, n):
    """Returns a list of n tuples of best cars' (indices, score)"""
    sortedInd = np.flip(np.argsort(scoreArray), 0)
    bestCars = []
    i = 0
    while i < n:
        carInd = sortedInd[i]
        bestCars.append((carInd, scoreArray[carInd]))
        i += 1
    return bestCars

def main():
    carsList = importCars()
    attrMatrix = createAttrMatrix(carsList)
    attrs2boost = getBrowsingAttrs(3)
    prefArr = getPrefArr(attrs2boost)
    scoreArray = getScoreArray(attrMatrix, prefArr)
    bestCarsList = getBestCars(scoreArray, 3)
    # print(bestCarsList)
    for car in bestCarsList:
        print("%s-%.1f%%" %(cars[car[0]].name, car[1]*100))


if __name__ == '__main__':
    main()