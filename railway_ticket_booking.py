import logging

logging.basicConfig(
    filename="railway_ticket.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
class Ticket:
    base_fare = 100
    booked_passengers = []
    
    def __init__(self, passenger_name, ticket_id, distance):
        self.passenger_name = passenger_name
        self.ticket_id = ticket_id
        self.distance = distance
        self.status = "Not Booked"
    
    
    def book_ticket(self):
        if self.ticket_id in Ticket.booked_passengers:
            logging.warning("Ticket already booked: %s", self.ticket_id)
            return
        Ticket.booked_passengers.append(self.ticket_id)
        self.status = "Booked"
        logging.info("Ticket booked successfully for %s", self.passenger_name)
    
    
    def cancel_ticket(self):
        if self.ticket_id not in Ticket.booked_passengers:
            logging.warning("No booking found for ticket: %s", self.ticket_id)
            return
        Ticket.booked_passengers.remove(self.ticket_id)
        self.status = "Cancelled"
        logging.info("Ticket cancelled successfully: %s", self.ticket_id)
    
    
    def calculate_fare(self):
        if self.status != "Booked":
            logging.warning("Ticket not booked yet: %s", self.ticket_id)
            return
        total_fare = Ticket.base_fare + (self.distance * 2)
        logging.info("Total fare for ticket %s is %d", self.ticket_id, total_fare)
    
    @classmethod
    def update_base_fare(cls, new_fare):
        cls.base_fare = new_fare
        logging.info("Base fare updated to %d", cls.base_fare)


t1 = Ticket("Sharanya", "T101", 150)
t1.book_ticket()
t1.calculate_fare()
t2 = Ticket("paddu", "T102", 80)
t2.book_ticket()
t2.cancel_ticket()
Ticket.update_base_fare(200)
t1.calculate_fare()
