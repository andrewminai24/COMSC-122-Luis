#Luis Mejia
#A Coffee File Management Program
import LastnameFirstInitial_coffee_records
 #Here's ehere we import the module that we just made.


ADD_COFFEE_CHOICE=1 #define global constants for all the choices
SHOW_COFFEE_CHOICE=2
SEARCH_COFFEE_CHOICE=3
MODIFY_COFFEE_CHOICE=4
DELETE_COFFEE_CHOICE=5
QUIT_CHOICE=6
#Which includes the choice to quit

def main():
    choice=0
    while choice != QUIT_CHOICE:
        display_menu()
        choice=int(input("Enter your choice: "))
        if choice==ADD_COFFEE_CHOICE:
            LastnameFirstInitial_coffee_records.add_coffee() #We call the function
        elif choice==SHOW_COFFEE_CHOICE:
            LastnameFirstInitial_coffee_records.show_coffee()
        elif choice==SEARCH_COFFEE_CHOICE:
            LastnameFirstInitial_coffee_records.search_coffee()

        elif choice == MODIFY_COFFEE_CHOICE:
            LastnameFirstInitial_coffee_records.modify_coffee()

        elif choice==DELETE_COFFEE_CHOICE:
            LastnameFirstInitial_coffee_records.delete_coffee()
      
        elif choice==QUIT_CHOICE:
            print("Exiting the program...")
        else:
            print("Error: invalid selection.")
def display_menu():
    print("\nJUAN VALDEZ COFFEE MANAGEMENT MENU")
    print("1) Add more Coffee Choices to List")
    print("2) Display all the Coffee Choices")
    print("3) Search Coffee Choices")
    print("4) Modify coffee Choices")
    print("5) Delete a Coffee Choice")
    print("6) Quit")

main()