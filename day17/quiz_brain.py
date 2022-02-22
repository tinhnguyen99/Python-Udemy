#
class QuizBrain:
    """
    question_list: List of Question Class.
    """
    def __init__(self, question_list):
        self.question_number = 0
        self.core =0
        self.question_list = question_list

    def next_question(self):
        """
        Print out question base on question number
        """
        current_question = f"Q.{self.question_number}: {self.question_list[self.question_number].question} (True/False)? "
        answer = input(current_question)
        self.check_answer(answer, self.question_list[self.question_number].answer)
        self.question_number += 1

    def still_have_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, system_answer):
        if user_answer.lower() == system_answer.lower():
            self.core +=1
            print("That a true answer")


