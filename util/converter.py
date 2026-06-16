from abc import ABC, abstractmethod
from users.user import Cashier, Customer
from products.product import Hamburger, Soda, Drink, HappyMeal

class Converter(ABC):
  @abstractmethod
  def convert(self,dataFrame,*args) -> list:
      pass  
  def print(self, objects):
    for item in objects:
      print(item.describe())

class CashierConverter(Converter):
  def convert(self,dataFrame):    
    cashiers = []
    for index, row in dataFrame.iterrows():
      cashier = Cashier(row['dni'], row['name'], row['age'], row['timetable'], row['salary'])
      cashiers.append(cashier)
    return cashiers
    pass

class CustomerConverter(Converter):
  def convert(self,dataFrame):
    customers = []
    for index, row in dataFrame.iterrows():
      customer = Customer(row['dni'], row['name'], row['age'], row['email'], row['postalcode'])
      customers.append(customer)
    return customers
    pass

class ProductConverter(Converter):
  def convert(self, df_hamburgers, df_sodas, df_drinks, df_happymeals):
    products = []
    for index, row in df_hamburgers.iterrows():
      products.append(Hamburger(row['id'], row['name'], row['price']))
    for index, row in df_sodas.iterrows():
      products.append(Soda(row['id'], row['name'], row['price']))
    for index, row in df_drinks.iterrows():
      products.append(Drink(row['id'], row['name'], row['price']))
    for index, row in df_happymeals.iterrows():
      products.append(HappyMeal(row['id'], row['name'], row['price']))
    return products
    pass
