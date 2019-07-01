import numpy as np

class Car:
    "Represents a Car object"

    def __init__(self, price, mpg, size, color, ftype, hp, seats, wd, make):
        "Fill attributes"
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
        self.attrs = np.zeros(33)
        "Price"
        if price < 16000:
            self.attrs[0] = 1
        elif price < 20000:
            self.attrs[1] = 1
        elif price < 25000:
            self.attrs[2] = 1
        elif price < 30000:
            self.attrs[3] = 1
        elif price < 37500:
            self.attrs[4] = 1
        else:
            raise Exception('Price not supported')
        "MPG"
        if mpg < 20:
            self.attrs[5] = 1
        elif mpg < 30:
            self.attrs[6] = 1
        elif mpg < 40:
            self.attrs[7] = 1
        else:
            raise Exception('MPG not supported')
        "Size"
        if size == 'sedan':
            self.attrs[8] = 1
        elif size == 'sports':
            self.attrs[9] = 1
        elif size == 'van':
            self.attrs[10] = 1
        elif size == 'suv':
            self.attrs[11] = 1
        elif size == 'truck':
            self.attrs[12] = 1
        else:
            raise Exception('Size not supported')
        "Color"
        if color == 'red':
            self.attrs[13] = 1
        elif color == 'black':
            self.attrs[14] = 1
        elif color == 'silver':
            self.attrs[15] = 1
        else:
            raise Exception('Color not supported')
        "Engine Fuel Type"
        if ftype == 'gas':
            self.attrs[16] = 1
        elif ftype == 'electric':
            self.attrs[17] = 1
        elif ftype == 'diesel':
            self.attrs[18] = 1
        else:
            raise Exception('Fuel type not supported')
        "Horsepower"
        if hp < 300:
            self.attrs[19] = 1
        elif hp < 500:
            self.attrs[20] = 1
        else:
            raise Exception('Horsepower type not supported')
        "Seats"
        if seats <= 4:
            self.attrs[21] = 1
        elif seats == 5:
            self.attrs[22] = 1
        elif seats <= 7:
            self.attrs[23] = 1
        else:
            raise Exception('MPG not supported')
        "Wheel Drive"
        if wd == 'front':
            self.attrs[24] = 1
        elif wd == 'rear':
            self.attrs[25] = 1
        elif wd == 'all':
            self.attrs[26] = 1
        elif wd == '4':
            self.attrs[27] = 1
        else:
            raise Exception('Wheel Drive type not supported')
        "Make"
        if make == 'audi':
            self.attrs[28] = 1
        elif make == 'hyundai':
            self.attrs[29] = 1
        elif make == 'jeep':
            self.attrs[30] = 1
        elif make == 'mercedes':
            self.attrs[31] = 1
        elif make == 'toyota':
            self.attrs[32] = 1
        else:
            raise Exception('Make not supported')

    def getAttrs(self):
        return self.attrs
