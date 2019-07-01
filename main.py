import numpy as np
from Car import Car

def importCars():
    "Returns a list of all cars that will be used"
    cars = []
    #car0: Mercedes A class sedan 2019
    cars.append(Car(32500, 35, 'sedan', 'silver', 'gas', 188, 5, 'all', 'mercedes'))

    return cars

def createAttrMatrix(carsList):
    "Returns a 2d array where each column is the attribute list of a car, so rows=33 and columns=carsList.len"
    attrMatrix = np.zeros((33, len(carsList)))
    i = 0
    while i < len(carsList):
        attrMatrix[:, i] = np.transpose(carsList[i].getAttrs())
        i += 1
    return attrMatrix

def getBrowsingAttrs(n):
    "Returns list of n tuples (attr #, score) that comes from browsed cars and their respective times"
    cars = []  # get list of cars browsed
    times = np.array([])  # get arr of corresponding browsing times
    times = times / sum(times)
    attrs = np.zeros((len(cars), 33))
    i = 0
    while i < len(cars):
        attrs[i, :] = cars[i].getAttrs() * times[i]
        i += 1
    sumArr = np.sum(a=attrs, axis=1)
    sortedInd = np.flip(np.argsort(sumArr), 0)
    bestAttrs = []
    i = 0
    while i < n:
        attrInd = sortedInd[i]
        bestAttrs.append((attrInd, sumArr[attrInd]))
        i += 1
    return bestAttrs

def getPrefArr(attrs2boost):
    "Returns an array of the weighted preferences associated with each attribute (prefArr.len=33)"
    #check attrs2boost to see if any have scores of 0; if so, ignore
    wp = np.zeros(33)


def getScoreArray(attrMatrix, prefArr):
    "Calculates score array by:"
    "  *multiplying attributes (rows) by corresponding weighted pref values"
    "  *summing scores for each car (column)"
    scoreArray = attrMatrix * prefArr[:, None]
    scoreArray = np.sum(a=scoreArray, axis=1)
    return scoreArray

def getBestCars(scoreArray, n):
    "Returns a list of n tuples of best cars' (indices, score)"
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

if __name__ == '__main__':
    main()