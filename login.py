
#functions
def main_lobby():
    print("""
════════════════════════════════════
          👤 USER PORTAL
════════════════════════════════════

Welcome user!

🍔 Browse Food
🔎 Search Food
🏪 Restaurants
🛒 Cart
🪑 Available Seats
📅 My Reservations
📦 My Orders
❤️ Favorites
🎟️ Offers
💰 Wallet
🏆 Food Points
⭐ Reviews
🔔 Notifications
👤 Profile
🚪 Logout""")

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
    
