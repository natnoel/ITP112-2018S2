class Book:
    def __init__(self, id, price, quantity, title):
        self.id = id
        self.price = price
        self.quantity = quantity
        self.title = title
class Order:
    def __init__(self, book_id, quantity):
        self.book_id = book_id
        self.quantity = quantity


class Store:
    book_dict = {}
    order_list = []

    def __init__(self):
        # Part A
        # Assign both class variables with sample data if they are empty
        self.create_books()
        self.create_orders()

    def create_books(self):
        # 3 sample book data
        b1 = Book('b123a', 10.0, 15, 'Basic Python')
        b2 = Book('b145b', 20.0, 22, 'Advanced Python')
        b3 = Book('b234h', 5.0, 2, 'Basic Java')
        Store.book_dict[b1.id] = b1
        Store.book_dict[b2.id] = b2
        Store.book_dict[b3.id] = b3

    def create_orders(self):
        # 3 sample Order data
        o1 = Order('b123a', 2)
        o2 = Order('b145b', 5)
        o3 = Order('b234h', 2)
        Store.order_list.append(o1)
        Store.order_list.append(o2)
        Store.order_list.append(o3)

    def print_orders(self):
        # Part B
        # Print the orders in Store.order_list
        # eg. 'Ordered 2 copies of b123a'
        for order in Store.order_list:
            print(f'Ordered {order.quantity} of {order.book_id}')

    def search(self, keyword):
        # Part C
        # Search for books with title containing the keyword
        # return a list of Book objects that fit the search criteria
        result_list = []
        for book in Store.book_dict.values():
            if keyword.lower() in book.title.lower():
                result_list.append(book)
        return result_list

    def calculate_revenue(self):
        # Part D
        # Calculate the total revenue earned from the orders
        # Revenue is calculated by quantity * price
        # return the total revenue as a number
        revenue = 0
        for order in Store.order_list:
            print(f'{order.quantity} of {order.book_id} at {Store.book_dict[order.book_id].price} each')
            revenue += order.quantity * Store.book_dict[order.book_id].price
        return revenue

    def order(self, book_id, quantity):
        # Part E
        # Create an order method that allows an order to be made
        # Show error message 'Invalid book id {}' if book id is not valid
        if book_id not in Store.book_dict:
            print(f'Invalid book id {book_id}')
            return
        # Show error message 'Insufficient quantity for {}' if quantity is not sufficient
        elif quantity > Store.book_dict[book_id].quantity:
            print(f'Insufficient quantity for {book_id}')
            print(f'U want {quantity} but only {Store.book_dict[book_id].quantity} available')
            return

        # If the order for the same book exists, update the order quantity
        order_exist = False
        for order in Store.order_list:
            if book_id == order.book_id:
                order_exist = True
                order.quantity += quantity

        # Otherwise, add in a new order if order has not been created
        if not order_exist:
            Store.order_list.append(Order(book_id, quantity))

        # Deduct the quantity of the book from the book dictionary
        Store.book_dict[book_id].quantity -= quantity


def demo1():
    print('>> Testing search() method:')
    s = Store()
    list = s.search('Python')
    for i in list:
        print(i.title)


def demo2():
    print('>> Testing calculate_revenue() method:')
    s = Store()
    print(s.calculate_revenue())


def demo3():
    print('>> Testing order method:')
    s = Store()
    s.order('b234h', 2)
    s.order('xxxx', 1)
    s.print_orders()


#demo1()
#demo2()
demo3()
