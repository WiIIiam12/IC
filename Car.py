import numpy as np

class Car:
    "Represents a Car object"

    def __init__(self, name, price, mpg, size, color, ftype, hp, seats, wd, make):
        "Fill attributes"
        self.name = name
        self.price = price
        self.mpg = mpg
        self.size = size
        self.color = color
        self.ftype = ftype
        self.hp = hp
        self.seats = seats
        self.wd = wd
        self.make = make

        "Fill attribute array"
        self.attrs = np.zeros(44)
        "Price"
        count = 0
        if price < 20000:
            self.attrs[count] = 1
        elif price < 25000:
            self.attrs[count+1] = 1
        elif price < 30000:
            self.attrs[count+2] = 1
        elif price < 35000:
            self.attrs[count+3] = 1
        elif price < 40000:
            self.attrs[count+4] = 1
        elif price < 45000:
            self.attrs[count+5] = 1
        elif price < 50000:
            self.attrs[count+6] = 1
        elif price < 55000:
            self.attrs[count+7] = 1
        elif price < 60000:
            self.attrs[count+8] = 1
        else:
            raise Exception('Price not supported')
        "MPG"
        count += 9
        if mpg < 20:
            self.attrs[count] = 1
        elif mpg < 30:
            self.attrs[count+1] = 1
        elif mpg < 40:
            self.attrs[count+2] = 1
        else:
            raise Exception('MPG not supported')
        "Size"
        count += 3
        if size == 'sedan':
            self.attrs[count] = 1
        elif size == 'sports':
            self.attrs[count+1] = 1
        elif size == 'van':
            self.attrs[count+2] = 1
        elif size == 'suv':
            self.attrs[count+3] = 1
        elif size == 'truck':
            self.attrs[count+4] = 1
        else:
            raise Exception('Size not supported')
        "Color"
        count += 5
        if color == 'red':
            self.attrs[count] = 1
        elif color == 'black':
            self.attrs[count+1] = 1
        elif color == 'silver':
            self.attrs[count+2] = 1
        elif color == 'blue':
            self.attrs[count+3] = 1
        elif color == 'white':
            self.attrs[count+4] = 1
        else:
            raise Exception('Color not supported')
        "Engine Fuel Type"
        count += 5
        if ftype == 'gas':
            self.attrs[count] = 1
        elif ftype == 'electric':
            self.attrs[count+1] = 1
        elif ftype == 'hybrid':
            self.attrs[count+2] = 1
        elif ftype == 'diesel':
            self.attrs[count+3] = 1
        else:
            raise Exception('Fuel type not supported')
        "Horsepower"
        count += 4
        if hp < 200:
            self.attrs[count] = 1
        elif hp < 300:
            self.attrs[count+1] = 1
        elif hp < 400:
            self.attrs[count+2] = 1
        elif hp < 500:
            self.attrs[count+3] = 1
        else:
            raise Exception('Horsepower type not supported')
        "Seats"
        count += 4
        if seats <= 4:
            self.attrs[count] = 1
        elif seats == 5:
            self.attrs[count+1] = 1
        elif seats <= 7:
            self.attrs[count+2] = 1
        else:
            raise Exception('MPG not supported')
        "Wheel Drive"
        count += 3
        if wd == 'front':
            self.attrs[count] = 1
        elif wd == 'rear':
            self.attrs[count+1] = 1
        elif wd == 'all':
            self.attrs[count+2] = 1
        elif wd == 'four':
            self.attrs[count+3] = 1
        else:
            raise Exception('Wheel Drive type not supported')
        "Make"
        count += 4
        if make == 'audi':
            self.attrs[count] = 1
        elif make == 'hyundai':
            self.attrs[count+1] = 1
        elif make == 'ford':
            self.attrs[count+2] = 1
        elif make == 'mercedes':
            self.attrs[count+3] = 1
        elif make == 'toyota':
            self.attrs[count+4] = 1
        else:
            raise Exception('Make not supported')

    #should we make vars private??
    def getAttrs(self):
        return self.attrs

    def getName(self):
        return self.name
