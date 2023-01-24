# The controller acts as the API for the app, in this case it will exist as a terminal based app
# using inputs and if statements to specify what the app should do

# It will run commands from the service file, which in turn uses the DB file to 
# query and create data and will return the data back to the use
import service

print("Welcome to the QA Cafe, what would you like to do?:")
action=input("\
        1. add order/s \
        2. update order in table\
        3. add to current order list\
        4. get allorders\
        5. get orders in list\
        6. commit current orders\
        7. delete order in list \
        8. update item in list\
        "
)
match action:
    case 1:
        print(service.add_Order())
    case 2:
        print(service.update_Order())
    case 3:
        print(service.addCurrOrder())
    case 4:
        print(service.getOrders())
    case 5:
        print(service.getCurrOrder())
    case 6:
        print(service.commit_Curr_Orders())
    case 7:
        print(service.delete_Curr_Order())
    case 8:
        print(service.update_Curr_Item())