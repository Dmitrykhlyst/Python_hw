class Address:
    index = "000000"
    city = "name"
    street = "name"
    home_number = "000"
    apart_number = "0000"

    def __init__(self, index, city, street, home_number, apart_number):
        self.i = index
        self.c = city
        self.s = street
        self.h = home_number
        self.an = apart_number