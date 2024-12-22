#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.current_item = None
    self.items = []

  def add_item(self, title="", price=0, qty=1):
    self.current_item = {"name": title, "price": price, "qty": qty}
    item_total = price * qty
    self.total += item_total
    self.items.extend(title for _ in range(qty))

  def apply_discount(self):
    if self.discount == 0:
      print('There is no discount to apply.')
    else:
      pct_disc: float = self.discount/100
      actual_disc: float = pct_disc * self.total
      self.total -= actual_disc
      print_total = int(self.total) if int(self.total) == self.total else self.total
      print(f"After the discount, the total comes to ${print_total}.")
      
  def void_last_transaction(self):
    item_price = self.current_item["price"]
    item_count = self.current_item["qty"]
    credit = item_price * item_count
    
    self.total -= credit
    self.items = self.items[:-item_count]
      