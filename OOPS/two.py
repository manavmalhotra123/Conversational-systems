class Restaurant():
    def __init__(self):
        self.menu_items = {}
        self.bookings = {}
        self.orders = {}

    def add_new_item(self, item_name, price):
        self.menu_items[item_name] = price

    def make_booking(self, table_number, date):
        if table_number not in self.bookings:
            self.bookings[table_number] = date
        else:
            print(f"Table {table_number} is already booked for {self.bookings[table_number]}.")

    def place_order(self, table_number, items):
        if table_number not in self.orders:
            self.orders[table_number] = items
        else:
            print(f"Table {table_number} already has an order. Please check the order or select another table.")

    def print_details(self):
        print("Menu Items:", self.menu_items)
        print("Bookings:", self.bookings)
        print("Orders:", self.orders)


restaurant = Restaurant()

restaurant.add_new_item("Pizza", 15)
restaurant.add_new_item("Burger", 10)
restaurant.add_new_item("Pasta", 20)

restaurant.make_booking(1, "2023-08-25")
restaurant.make_booking(2, "2023-08-26")
restaurant.make_booking(1, "2023-08-27")  

restaurant.place_order(1, ["Pizza", "Burger"])
restaurant.place_order(2, ["Pasta"])
restaurant.place_order(2, ["Pizza"])  

restaurant.print_details()
