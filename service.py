# The service file interacts with the DB file to Query or Modify data within the database
# Typically there will be a function for each process that is required, and these will take in data and return data

import getpass
import sqlite3

conn = sqlite3.connect("orders")
curs = conn.cursor()
_orders={}

class ordermethods:

    """class of available methods """
    def __init__(self,customer="",username=input("Username: "),password=getpass.getpass("Password:")):
        """initialising vars"""
        self.username=username
        self.__password=password
        self.customer=customer

    def add_Order(self,item,quantity):
        if "admin" in self.username and len(self.__password)>8 :
            curs.execute(f"INSERT INTO orders (customer, item, quantity) \
                            VALUES ({self.customer}, {item}, {quantity})")
            return f"added {self.customer}'s order of {quantity} {item} to the orders table "

    def update_Order(self,customer):
        if "admin" in self.username and len(self.__password)>8 :
            choice=input("do you want to update item or quantity?")
            column="item" if "ite*" in choice else "quantity"
            value=input("what is the updated value")
            curs.execute(f"UPDATE orders SET {column}={value} \
                            WHERE customer = {customer}")
            return f"updated {customer}'s order to {value} {column} "

    def addCurrOrder(self,item,input_iter=1):
        """add to items to order """
        self.customer=input("Customer: ")
        for num in range(input_iter):
            item=input(f"Item {num} Name: ")
            quantity=input(f"Quantity of {item}: ")
            _orders[self.customer][item]=quantity
            return("added order")

    def getOrders(self):
        """get all orders from order table"""
        if "admin" in self.username and len(self.__password)>8 :
            return curs.execute("SELECT * FROM orders")
        return "Incorrect login"
        
    def getCurrOrder(self):
        """get buffer orders- uncommitted"""
        return _orders.items()

    def commit_Curr_Orders(self):
        """commit uncommitted orders,only means to commit to table"""
        for customer in _orders.keys():
            for item,quantity in _orders[customer].items():
                curs.execute(f"INSERT INTO orders (customer, item, quantity) \
                            VALUES ({customer}, {item}, {quantity})")
        conn.commit()
        return"committed change"

    def delete_Curr_Order(self):
        """deleting customer order from uncommitted orders"""
        self.customer=input("Customer: ")
        del _orders[self.customer]
        return f"deleted order by {self.customer}"

    def update_Curr_Item(self,item,quantity):
        """updating uncommitted orders"""
        _orders[self.customer][item]=quantity
        return "updated uncommitted orders"