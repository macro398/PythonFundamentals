class Queue:
    def __init__(self):
        self.orders = []

    def size(self):
        return  len(self.orders)
    
    def enqueue(self,item):
        self.orders.append(item)

    def dequeue(self):
        if self.size() == 0:
            return None
        return self.orders.pop(0)

    def show_queue(self):
        print(self.orders)
    
    def my_orders(self):
        return self.orders

class IceCreamShoppe:
    def __init__(self, flavors):
        self.flavors = flavors
        self.queue = Queue()

    def take_order(self, name, flavor, scoops):
        if flavor not in self.flavors:
            print(f"{flavor} isn't valid please select a valid flavor.")
            
        elif scoops < 1 or scoops > 3:
            print(f"{scoops} isn't a valid option, must be between 1-3 scoops.")
            
        else:
            order = {"name":name, 'flavor':flavor, 'scoops':scoops}
            print("New order created.")
            self.queue.enqueue(order)
    
    def show_all_orders(self):
        for order in self.queue.my_orders():
            print(order)
    
    def next_order(self):
        print("next order up:", self.queue.dequeue())

shop = IceCreamShoppe(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()
shop.next_order()
shop.next_order()
shop.next_order()