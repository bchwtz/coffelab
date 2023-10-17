from datetime import datetime
from random import choice
from blabel import LabelWriter
import time

class Beverage:
    
    # type:  Espresso, Kaffee, Cappucchino, Hot Chocolate
    # size:  S, M , L
    # syrup: Zucker, Vanille, Haselnuss
    
    types = {"Espresso": ["S"], 
            "Kaffee": ["S", "M", "L"], 
            "Cappucchino": ["M"],
            "Hot Chocolate": ["L"],
            "Tee": ["L"]}
             
    def __init__(self, type, size = None, extrashot = False, syrup = None):
        
        self.type = type
        self.size = size
        self.extrashot = extrashot
        self.syrup = syrup
        
        self.cookie = choice([True, False])
        self.machine = choice(["M1", "M2"])
        self.starttime = datetime.now()

    def setType(self, type):
        self.type = type
        self.starttime = datetime.now()
        

    @property
    def lastchangetime(self):
        return datetime.now()

    @property
    def price(self):
        price = 1.00
        if self.type == "Kaffee":
            price += 1.00
        if self.type == "Cappucchino":
            price += 2.00
        if self.extrashot:
            price += 1.2
        return(price)

    @property
    def typeabbr(self):
        return self.type[0] # Get first Letter from Type

    @property
    def shortcode(self):
        shortcode = self.machine + " "
        shortcode += self.typeabbr
        if self.extrashot:
            if self.type == "Espresso" or self.type == "Kaffee":
                shortcode +="2"
            else:
                shortcode += "+"    
        shortcode += " " + self.size
        if self.cookie:
            shortcode += " " + u"\u00A9"
        return shortcode

    @property
    def record(self):
        baseurl = "https://baseurl.com/form?"
        formurl = baseurl + \
            "type=" + self.typeabbr + "&" + \
            "extrashot=" + str(int(self.extrashot)) + "&" \
            "cookie=" + str(int(self.cookie)) + "&" \
            "machine=" + self.machine

        record = [
            dict(qr = formurl,
            type = self.type,
            typeabbr = self.typeabbr,
            size = self.size,
            extrashot = self.extrashot,
            syrup = self.syrup,
            shortcode = self.shortcode,
            cookie = self.cookie,
            machine = self.machine,
            price = self.price,
            starttime = self.starttime.strftime("%Y-%m-%d %H:%M:%S"),
            lastchangetime = self.lastchangetime.strftime("%Y-%m-%d %H:%M:%S")
             )
            ]
        return record


    def __repr__(self):
        return "Beverage({} // {:.2f})".format(self.shortcode, self.price) 


