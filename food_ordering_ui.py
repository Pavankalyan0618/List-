#user interface to the main menu
import data
import functions
def show_main_menu():
  order_items = list()
  while True:
    print("Pavan Kalyan Pendyala diner") #edit to show your name
    print("__________")
    print('Insert N for a new order')
    print('Insert X for close orders and print the check')
    print('Insert C to change the order')
    print('Insert Q for quit')
    user_menu_choice = input('Your choice: ')
    if user_menu_choice in 'Qq':
      break
    elif user_menu_choice in 'Xx':
      for i in range(len(order_items)):
        print(order_items[i][0],'x',order_items[i][1],'----',int(order_items[i][2])*int(order_items[i][0]))
    elif user_menu_choice in 'Nn':
     while True:
        quantity,item,price = make_order(user_menu_choice.upper()) #calls a function for adding to the orders
        print(quantity,'x',item)
        order_items.append([quantity,item,price])
        print('Do you want to add more items?')
        choice = input('Press "y" for YES and "n" for NO\n')
        if choice in "Yy":
          continue
        elif choice in "Nn":
          break
        else:
          print('invalid choice')
    elif user_menu_choice in 'Cc':
      if len(order_items) == 0:
        print("You haven't ordered anything yet")
      else:
        close_order(user_menu_choice.upper())
        order_items = []

      
def make_order(menu_choice):
  user_selection = functions.get_item_number()
  item_code, quantity = user_selection.split()
  return quantity,functions.get_item_information(item_code)[0],functions.get_item_information(item_code)[1]

def close_order(menu_choice):
  print('Fnctionality for menu choice ', menu_choice)



if __name__ == '__main__':
    #initialize the lists
    drinks = []
    appetizers = []
    salads = []
    entrees = []
    dessert= []
    #print(functions.get_item_information('D1'))
    show_main_menu()