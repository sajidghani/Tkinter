# # class Laptop:
# #     def total_amount(self,a,b):
# #         return a *b
# #
# # laptop1 = Laptop()
# # laptop1.name = 'Lenevo'
# # laptop1.ram = '12GB'
# # laptop1.storage = '256GB'
# # laptop1.window = '2010'
# # laptop1.price = 20000
# # laptop1.quantity = 10
# # total_price = laptop1.total_amount(laptop1.price,laptop1.quantity)
# # print(f'Total Price of {laptop1.name} is {total_price} ')
#
#
# class Book:
#     discount_rate = 0.5
#
#     def __init__(self, name: str, price: float, quantity=0):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#         assert price >= 0, f'Price {price} is not valid check it in arguments'
#         assert quantity >= 0, f'Quantity {quantity} is not valid. check in arguments'
#
#
#
#
#     def total_amount(self):
#        return self.price * self.quantity
#
#     def discount_on_book(self):
#      self.price = self.price * self.discount_rate
#
#
# book1 = Book("History of Balochistan", 500, 100)
# tp = book1.total_amount()
# print(f'{book1.name} total amount: {tp}')
#
# print(f'Original Price: {book1.price}')
# book1.discount_on_book()
# print(f'Price after discount: {book1.price}')
#
# print("========================================")
# book2 = Book("Computer Graphics", 500, 5)
# tp = book2.total_amount()
# print(f'{book2.name} total amount: {tp}')
# print(f'Original Price: {book2.price}')
#
# book2.discount_rate = 0.4
# #book2.discount_on_book()
# print(f'Price after discount: {book2.price}')


class Electronics:
    discount_rate = 0.4
    def __init__(self,name:str,price:float,quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity
        assert quantity>=0 ,f'The entered value {self.quantity} is wrong'
        assert price>=0, f'please enter a valid price {self.price}'

    def total_amount(self):
        return self.price * self.quantity

    def discount_p(self):
        self.price = self.price * self.discount_rate

fan1 = Electronics('K fan',3000,3)
fan1.discount_p()
print(f'discounted Price {fan1.price} of {fan1.name}')
fan1.total_amount()
print(f'total amount of {fan1.name} is {fan1.}')