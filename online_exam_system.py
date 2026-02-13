import logging

logging.basicConfig(
    filename="online_exam.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class OnlineExam:

    pass_marks = 40
    active_students = []

    def __init__(self, student_name, total_questions):
        self.student_name = student_name
        self.total_questions = total_questions
        self.score = 0


    def start_exam(self):

        if self.student_name in OnlineExam.active_students:
            logging.warning("Exam already started for %s", self.student_name)
            return

        OnlineExam.active_students.append(self.student_name)
        logging.info("Exam started successfully for %s", self.student_name)


    def submit_exam(self):

        if self.student_name not in OnlineExam.active_students:
            logging.warning("Exam not started yet for %s", self.student_name)
            return

        logging.info("Exam submitted successfully by %s", self.student_name)


    def calculate_score(self, correct_answers):

        if self.student_name not in OnlineExam.active_students:
            logging.warning("Exam not started yet for %s", self.student_name)
            return

        self.score = correct_answers

        if self.score >= OnlineExam.pass_marks:
            logging.info("%s PASSED with score %d", self.student_name, self.score)
        else:
            logging.info("%s FAILED with score %d", self.student_name, self.score)

    @classmethod
    def update_pass_marks(cls, marks):
        cls.pass_marks = marks
        logging.info("Pass marks updated to : %d", cls.pass_marks)

e1 = OnlineExam("Sharanya", 50)
e1.start_exam()
e1.calculate_score(45)
e1.submit_exam()
e2 = OnlineExam("paddu", 50)
e2.start_exam()
e2.calculate_score(30)
OnlineExam.update_pass_marks(50)
e1.calculate_score(45)
