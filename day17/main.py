from question_model import Question
from data           import question_data
from quiz_brain     import QuizBrain


print("Welcom to day 17")
question_list = []

for i in question_data:
    question_list.append(Question(i["text"], i["answer"]))

quiz_brain_instance = QuizBrain(question_list)

while quiz_brain_instance.still_have_question():
    quiz_brain_instance.next_question()

print(f"Final core is {quiz_brain_instance.core}")