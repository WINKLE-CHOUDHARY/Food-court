# functions

def browse_food():
    print('''🍕 Pizza — ₹149
🍔 Veg Burger — ₹99
🌯 Veg Wrap — ₹89
🍜 Hakka Noodles — ₹129
🥗 Paneer Salad — ₹119''')

def search_food():
    pass

def restaurants():
    print('''🍕 Pizza Palace
🍜 Wok Express
🥘 Spice Hub
🍔 Burger Point''')


def cart():
    pass


def available_seats():
    pass


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
    pass


def notifications():
    pass


def profile():
    pass


def logout():
    pass


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
    