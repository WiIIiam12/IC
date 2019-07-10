import numpy as np
from Car import Car

cars = []

def importCars():
    """"Returns a list of all cars that will be used"""
    # car0: 2019 Mercedes A class sedan
    cars.append(Car('2019 Mercedes A class sedan', 32500, 35, 'sedan', 'silver', 'gas', 188, 5, 'all', 'mercedes'))
    # car1: 2019 Audi RS3
    cars.append(Car('2019 Audi RS3', 56200, 28, 'sports', 'red', 'gas', 394, 5, 'all', 'audi'))
    # car2: Ford F-150 XL
    cars.append(Car('Ford F-150 XL', 29300, 26, 'truck', 'silver', 'gas', 325, 5, 'four', 'ford'))

    return cars

def createAttrMatrix(carsList):
    """"Returns a 2d array where each column is the attribute list of a car, so rows=33 and columns=carsList.len"""
    attrMatrix = np.zeros((33, len(carsList)))
    i = 0
    while i < len(carsList):
        attrMatrix[:, i] = np.transpose(carsList[i].getAttrs())
        i += 1
    return attrMatrix

def getBrowsingAttrs(n):
    """Returns list of n tuples (attr #, score) that comes from browsed cars and their respective times"""
    cars = []  # get list of cars browsed
    times = np.array([])  # get arr of corresponding browsing times
    # -------TEST VALUES-------
    cars.append(Car('2019 Mercedes A class sedan', 32500, 35, 'sedan', 'silver', 'gas', 188, 5, 'all', 'mercedes'))
    times = np.array([1])
    # -------TEST VALUES-------
    times = np.divide(times, sum(times))
    attrs = np.zeros((len(cars), 33))
    i = 0
    while i < len(cars):
        attrs[i, :] = cars[i].getAttrs() * times[i]
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
    """"Returns an array of the weighted preferences associated with each attribute (prefArr.len=33)"""
    wp = np.zeros(33)
    # -------TEST VALUES-------
    wp[2] = 2  # price 30<x<40
    wp[7] = 1  # mpg 30<x<40
    wp[8] = 1  # size = sedan
    wp[13] = 1 # color = red
    # -------TEST VALUES-------
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
        print("%s is a %.1f%% match" %(cars[car[0]].name, car[1]*100))


if __name__ == '__main__':
    main()