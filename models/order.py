class Order:

    def __init__(self, customer_name, order_date, quantity, book_title, description, url):
        self.customer_name = customer_name
        self.order_date = order_date
        self.quantity = quantity
        self.book_title = book_title
        self.description = description
        self.url = url