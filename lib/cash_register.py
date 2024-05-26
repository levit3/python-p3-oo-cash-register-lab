#!/usr/bin/env python3

class CashRegister:
  def __init__ (self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    
  def add_item(self, title, price, quantity = 1):
    self.title = title
    self.price = price
    self.total += (price * quantity)
    self.last_price = (price * quantity)
    for i in range(quantity):
      self.items.append(title)
    
  def apply_discount(self):
    if self.total > 0 :
      self.total -= self.last_price
      self.last_price = (self.last_price * 0.8)
      self.total += self.last_price
      print (f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")
      
  def void_last_transaction(self):
    self.total -= self.last_price