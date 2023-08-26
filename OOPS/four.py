class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_id, item_name, stock_count, price):
        if item_id not in self.items:
            self.items[item_id] = {
                'item_name': item_name,
                'stock_count': stock_count,
                'price': price
            }
            print(f"Added item: {item_name} with ID: {item_id}")
        else:
            print(f"Item with ID {item_id} already exists. Use update_item to modify it.")

    def update_item(self, item_id, item_name=None, stock_count=None, price=None):
        if item_id in self.items:
            if item_name:
                self.items[item_id]['item_name'] = item_name
            if stock_count is not None:
                self.items[item_id]['stock_count'] = stock_count
            if price is not None:
                self.items[item_id]['price'] = price
            print(f"Updated item with ID: {item_id}")
        else:
            print(f"Item with ID {item_id} does not exist. Use add_item to add it.")

    def check_item_details(self, item_id):
        return self.items.get(item_id, "Item not found in inventory.")

inventory = Inventory()
inventory.add_item(1, "Laptop", 5, 1000)
inventory.add_item(2, "Mouse", 50, 25)
inventory.update_item(1, stock_count=4)
inventory.update_item(2, price=30)
print(inventory.check_item_details(1))
print(inventory.check_item_details(2))
