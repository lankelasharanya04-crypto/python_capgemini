import logging

logging.basicConfig(
    filename="result_man.log",
    level=logging.INFO,
    format="%(asctime)s -%(levelname)s - %(message)s"
)



class result_10th:
    def __init__(self,name,phno,email,passing_yr,class_name):
        self.name=name
        self.phno=phno
        self.email=email
        self.passing_yr=passing_yr
        self.class_name=class_name

    def display(self):
        # print(self.name,self.phno,self.email,self.passing_yr,self.class_name)
        logging.info("name:%s \n phno:%d \n email:%s \n",self.name,self.phno,self.email)

class result_12th(result_10th):
    def __init__(self,name,phno,email,passing_yr,class_name,passing_yr_12,percentage_12):
        super().__init__(name,phno,email,passing_yr,class_name)
        self.passing_yr_12=passing_yr_12
        self.percentage_12=percentage_12
    def display(self):
        super().display()
        print(self.passing_yr_12,self.percentage_12)

class result_be(result_12th):
    def __init__(self,name,phno,email,passing_yr,class_name,passing_yr_12,percentage_12,branch,university,be_perc):
        super().__init__(name,phno,email,passing_yr,class_name,passing_yr_12,percentage_12)
        self.branch=branch
        self.university=university
        self.be_perc=be_perc

    def display(self):
        super().display()
        print(self.branch,self.university,self.be_perc)

s1=result_be("sharanya",8143853303,"bc@gmail.com",2020,"elite",2022,96.2,"cse-aiml","bvrit",79)
s1.display()

