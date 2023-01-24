# The DB file contains the processes and functions to create our Database or connect to it as well as run the initial SQL
# The DB file should also contain query functions that the Service file can use to read or modify the data
import sqlite3

conn = sqlite3.connect("/orders")
curs = conn.cursor()

"""initialise table by reading sql in order"""
sql_file = open("order.sql")
sql_string = sql_file.read()
curs.executescript(sql_string)

_orders={}

class ordermethods():
    """class of available methods """

    def __init__(self,username,password):
        """initialising vars"""
        self.username=username
        self.__password=password


    def add_to_table(self,customer,item,quantity):
        if "admin" in self.username and len(self.__password)>8 :
            curs.execute(f"INSERT INTO orders (customer, item, quantity) \
                            VALUES ({customer}, {item}, {quantity})")
            return f"added {customer}'s order of {quantity} {item} to the orders table "

    def addOrder(self,customer=input("Customer name: "),input_iter=1):
        """add to items to order """
        self.customer=customer
        self.item=item
        for num in range(input_iter):
            item=input(f"Item {num} Name: ")
            quantity=input(f"Quantity of {item}: ")
            _orders[self.customer][item]=quantity


    def getCommitedOrders(self):
        """get all orders from order table"""
        if "admin" in self.username and len(self.__password)>8 :
            return curs.execute("SELECT * FROM orders")
        return "Incorrect login"
        
        
    def getCurrentOrderList(self):
        """get buffer orders- uncommitted"""
        return _orders.items()

    def commit_orderlist(self):
        """commit uncommitted orders,only means to commit to table"""
        
        for customer in _orders.keys():
            for item,quantity in _orders[customer].items():
                curs.execute(f"INSERT INTO orders (customer, item, quantity) \
                            VALUES ({customer}, {item}, {quantity})")
        conn.commit()

    def deleteOrder(self,customer):
        """deleting customer order from uncommitted orders"""
        del _orders[customer]

    def updateOrder(self,customer,item,quantity):
        """updating uncommitted orders"""
        _orders[customer][item]=quantity
