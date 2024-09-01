from question_model import Question
from data import question_data
from quiz_brain import QuestionBrain
question_bank =[]
for question in question_data:
    qt=question["text"]
    qa=question["answer"]
    new_question=Question(qt,qa)
    question_bank.append(new_question)

quiz = QuestionBrain(question_bank)
while quiz.stiil_has_que():
   quiz.next_question()
print("you'have completed your quiz")
print(f"your final score was : {quiz.score}/{quiz.question_num}")