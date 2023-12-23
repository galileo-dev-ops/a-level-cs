"""
class Flower:
    def __init__(self, flower, height, evergreen):
        self._flower = flower
        self._height = height
        self._evergreen = evergreen
    def __str__(self):
        return f'This is a {self._height} {self._flower} that is {self._evergreen}'
    def get_flower(self):
        return self._flower
    def get_height(self):
        return self._height
    def get_evergreen(self):
        return self._evergreen
    
class Rose(Flower):
    def __init__(self, height, evergreen):
        super().__init__('Rose', height, evergreen)

print(Rose('1m', 'evergreen'))
"""

"""
class Person:
    def __init__(self, name, age, address):
        self._name = name
        self._age = age
        self._address = address
    def __str__(self):
        return f'{self._name} is {self._age} years old and lives in {self._address}'
    def get_name(self):
        return self._name
    def get_age(self):
        return self._age
    def get_address(self):
        return self._address
    
class Employee(Person):
    def __init__(self, name, age, address, NInsurance):
        super().__init__(name, age, address)
        self._NIn = NInsurance
    def __str__(self):
        return f'{self._name} is {self._age} years old and lives in {self._address} and has NI {self._NInsurance}'
    def get_NI(self):
        return self._NInsurance
    def get_name(self):
        return "Employee " + self._name

Person1 = Person('Bill', 25, 'Stevenage')
Emp1 = Employee('Tom', 26, 'Hitchin', 'NX10527PX')


print(Person1.get_name())
print(Emp1.get_name())



"""

def moneyFormat(num):
    return '{:,.2f}'.format(num)


class ItemSale:
    def __init__(self, name, price):
        self._name = name
        self._price = price
        self._discount = 0
    def __str__(self):
        priceMoney = moneyFormat(self._price)
        return f'{self._name} costs £{priceMoney}'
    def get_name(self):
        return self._name
    def get_price(self):
        return self._price
    def set_discount(self, discount):
        if discount > 50:
            print('Discount too high')
            exit()
        discount = int(input('Enter discount: '))
        global discPrice
        discPrice = self._price - (self._price * (discount/100))
        return discount
    def calc_discount(self):
        money = moneyFormat(discPrice)
        print(f'{self._name} now costs £{money}')
        return discPrice
    
crisps = ItemSale('Crisps', 0.90)
marsBar = ItemSale('Mars Bar', 1.50)

print(crisps)
print(marsBar)

crisps.set_discount(10)
crisps.calc_discount()

marsBar.set_discount(20)
marsBar.calc_discount()


class ItemForSaleOnline(ItemSale):
    def __init__(self, name, price, weblink):
        super().__init__(name, price)
        self._weblink = weblink
        self._discount = 0
    def __str__(self):
        priceMoney = moneyFormat(self._price)
        return f'{self._name} costs £{priceMoney} and the weblink is {self._weblink}'
    def get_weblink(self):
        return self._weblink
    def set_discount(self, discount):
        discount = int(input('Enter discount: '))
        if discount > 50:
            print('Discount too high')
            exit()
        global discPrice
        discPrice = self._price - (self._price * ((discount/100) + 0.2))
        return discount
    def calc_discount(self):
        money = moneyFormat(discPrice)
        print(f'{self._name} now costs £{money} and weblink is {self._weblink}')
        return discPrice
    
crispsOnline = ItemForSaleOnline('CrispsOnline', 0.90, 'www.crisps.com')
marsBarOnline = ItemForSaleOnline('Mars Bar Online', 1.50, 'www.mars-bar.com')

crispsOnline.set_discount(10)
crispsOnline.calc_discount()

marsBarOnline.set_discount(20)
marsBarOnline.calc_discount()