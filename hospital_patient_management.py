class Patient:
    consultation_fee = 500
    def __init__(self, name, age, disease, days_admitted):
        self.name = name                #-->constructer
        self.age = age
        self.disease = disease
        self.days_admitted = days_admitted
        self.admitted = False
    def admit_patient(self):
        self.admitted = True
        print(self.name, "has been admitted")
    def discharge_patient(self):
        self.admitted = False
        print(self.name, "has been discharged")
    def calculate_bill(self):
        bill = self.days_admitted * Patient.consultation_fee
        print("Total Bill:", bill)
    @classmethod
    def update_consultation_fee(cls, fee):
        cls.consultation_fee = fee
        print("Consultation fee updated to", fee)
p1 = Patient("Sharanya", 20, "Fever", 3)
p2 = Patient("Paddu", 25, "Infection", 5)
p1.admit_patient()
p1.calculate_bill()
Patient.update_consultation_fee(700)
p1.calculate_bill()
p1.discharge_patient()
