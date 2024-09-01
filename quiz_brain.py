
class QuestionBrain:
     def __init__(self,qlist):
             self.question_num = 0
             self.questionlist = qlist
             self.score= 0

     def stiil_has_que(self):
         return self.question_num< len(self.questionlist)



     def next_question(self):
         current_question =self.questionlist[self.question_num]
         self.question_num +=1
         useranswer= input(f"Q.{self.question_num}:{current_question.text}(True/False):")
         self.check_answer(useranswer,current_question.answer)
     def check_answer(self,useranswer,correct_answer):
         if useranswer.lower() == correct_answer.lower():
             self.score += 1
             print("you are right")
         else:
             print("that's wrong")
         print(f" the corret ans is:{correct_answer}.")
         print(f"your score is :{self.score}/{self.question_num}")

