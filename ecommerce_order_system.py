import logging
logging.basicConfig(
    filename="order_system.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
class Order:
    tax_percentage = 5
    placed_orders = []
    def __init__(self, customer_name, order_id, price):
        self.customer_name = customer_name
        self.order_id = order_id
        self.price = price
        self.status = "Not Placed"
    def place_order(self):
        if self.order_id in Order.placed_orders:
            logging.warning("Order already placed: %s", self.order_id)
            return
        self.status = "Placed"
        Order.placed_orders.append(self.order_id)
        logging.info("Order placed successfully by %s", self.customer_name)
    def cancel_order(self):
        if self.order_id not in Order.placed_orders:
            logging.warning("No such placed order found: %s", self.order_id)
            return
        self.status = "Cancelled"
        Order.placed_orders.remove(self.order_id)
        logging.info("Order cancelled successfully: %s", self.order_id)
    def calculate_total_price(self):
        if self.status != "Placed":
            logging.warning("Order not placed yet: %s", self.order_id)
            return
        tax_amount = (self.price * Order.tax_percentage) / 100
        total_amount = self.price + tax_amount

        logging.info("Total price for order %s is %.2f", self.order_id, total_amount)
    @classmethod
    def update_tax_percentage(cls, new_tax):
        cls.tax_percentage = new_tax
        logging.info("Tax percentage updated to %d", cls.tax_percentage)
o1 = Order("Sharanya", "ORD101", 5000)
o1.place_order()
o1.calculate_total_price()
o2 = Order("Ravi", "ORD102", 3000)
o2.place_order()
o2.cancel_order()
Order.update_tax_percentage(12)
o1.calculate_total_price()