# functions


def browse_food():
    order = input('''plz enter the food you want to browse''')
    print(f"searhing for {order}.......")
    dict = {
        'pizza': '🍕from Pizza Palace',
        'burger': '🍔 from Burger Point',
        'pasta': '🍜 from Wok Express'
    }
    if order in dict:
        print(f"Found {order}! Here's the emoji: {dict[order]}")
    else:
        print(f"Sorry, {order} is not available.")

def search_food():
    pass

def restaurants():
    print('''1. 🍕 Pizza Palace
2. 🍜 Wok Express
3. 🍚 Spice Hub
4. 🍔 Burger Point
5. Exit ''')

    while True:
            
        user = input("Enter the restaurant number to view menu: ")
        if user == '1':
            print('''🍕 Pizza Palace Menu:''')
        elif user == '2':
            print('''🍜 Wok Express Menu:''')
        elif user == '3':
            print('''🍚 Spice Hub Menu:''')
        elif user == '4':
            print('''🍔 Burger Point Menu:''')
        elif user == '5':
            print("Exiting restaurant menu.")
            break
        else:
            print("Invalid input. Please enter a number between 1 and 5.")

def cart():
    pass


def available_seats():
    while True:
        user_input = input("Do you want to check available seats? (yes/no): ")
        if user_input.lower() == 'yes':
            print("from which restaurant you want to check available seats?" \
            "1. 🍕 Pizza Palace\n2. 🍜 Wok Express\n3. 🍚 Spice Hub\n4. 🍔 Burger Point")
            restaurant_choice = input("Enter the restaurant number: ")
            if restaurant_choice == '1':
                seats = 20
                print(f"Available seats at Pizza Palace: {seats}")
                user= input("do you want to book the seats? (yes/no)")
                if user.lower() == 'yes':
                    seats_to_book = int(input("How many seats do you want to book? "))
                    if seats_to_book <= 20:
                        seats -= seats_to_book
                        print(f"{seats_to_book} seats booked at Pizza Palace.")
                    else:
                        print("Sorry, not enough seats available.")
            elif restaurant_choice == '2':
                seats = 15
                print(f"Available seats at Wok Express: {seats}")
                user = input("do you want to book the seats? (yes/no)")
                if user.lower() == 'yes':
                    seats_to_book = int(input("How many seats do you want to book? "))
                    if seats_to_book <= 15:
                        seats -= seats_to_book
                        print(f"{seats_to_book} seats booked at Wok Express.")
                    else:
                        print("Sorry, not enough seats available.") 
            elif restaurant_choice == '3':
                seats = 25
                print(f"Available seats at Spice Hub: {seats}")
                user = input("do you want to book the seats? (yes/no)")
                if user.lower() == 'yes':
                    seats_to_book = int(input("How many seats do you want to book? "))
                    if seats_to_book <= 25:
                        seats -= seats_to_book
                        print(f"{seats_to_book} seats booked at Spice Hub.")
                    else:
                        print("Sorry, not enough seats available.")
            elif restaurant_choice == '4':
                seats = 10
                print(f"Available seats at Burger Point: {seats}")
                user = input("do you want to book the seats? (yes/no)")
                if user.lower() == 'yes':
                    seats_to_book = int(input("How many seats do you want to book? "))
                    if seats_to_book <= 10:
                        seats -= seats_to_book
                        print(f"{seats_to_book} seats booked at Burger Point.")
                    else:
                        print("Sorry, not enough seats available.")
            else:
                print("Invalid choice.")
        elif user_input.lower() == 'no':
            print("Okay, maybe next time!")
            break

def my_reservations():
    pass


def my_orders():
    pass


def favorites():
    pass


def offers():
    pass


def wallet():
    pass


def food_points():
    pass


def reviews():
    while True: 
        user_input = input("want to give a review? (yes/no)")
        if user_input.lower() == 'yes':
            review = input("Please enter your review: ")
            print(f"Thank you for your review: {review}")
        elif user_input.lower() == 'no':
            print("No problem! Maybe next time.")
            break
        else:
            print("Invalid input. Please type 'yes' or 'no'.")


def notifications():
    pass


def profile():
    pass


def logout():
    print("You have been logged out. Thank you for visiting!")
    


def main_lobby():
    print("""
════════════════════════════════════
👤 USER PORTAL
════════════════════════════════════

Welcome user!

1. 🍔 Browse Food
2. 🔎 Search Food
3. 🏪 Restaurants
4. 🛒 Cart
5. 🪑 Available Seats
6. 📅 My Reservations
7. 📦 My Orders
8. ❤️ Favorites
9. 🎟️ Offers
10. 💰 Wallet
11. 🏆 Food Points
12. ⭐ Reviews
13. 🔔 Notifications
14. 👤 Profile
15. 🚪 Logout
""")

    while True:
            
        choice=int(input("Enter the number according to your choice:"))

        if choice == 1:
            browse_food()

        elif choice == 2:
            search_food()

        elif choice == 3:
            restaurants()

        elif choice == 4:
            cart()

        elif choice == 5:
            available_seats()

        elif choice == 6:
            my_reservations()

        elif choice == 7:
            my_orders()

        elif choice == 8:
            favorites()

        elif choice == 9:
            offers()

        elif choice == 10:
            wallet()

        elif choice == 11:
            food_points()

        elif choice == 12:
            reviews()

        elif choice == 13:
            notifications()

        elif choice == 14:
            profile()

        elif choice == 15:
            logout()
            break


#main maal
while True:

    print("welocome to alakh da dhaaba")
    print("Please type 1 for login ")
    print("Please type 2 for exit")
    request=int(input("enter the number:"))
    if request==1:
        user=input("enter your Name:")
        password=int(input("enter the password in numerical form:"))
        if user=="prince" and password==2007:
            main_lobby()
        elif user=="winkle" and password==2711:
            main_lobby()
        else:
            print(f"u are not a regular customer:( {user}")
            exit()

    elif request==2:
        exit()
    else:
        print("please give appropriate input...")
    