
class QuizBrain:
    def __init__(self, question_list):
        self. question_number = 0
        self.question_list = question_list
        self.score = 0


    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):

        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong.")
        
        print(f"The correct answer was: {correct_answer}")
        print(f"Your currrent score {self.score}/{self.question_number + 1}")
        print("\n")
        

    def display_results(self):
        print("You've completed the quiz")
        print(f"Your final score was {self.score}/{self.question_number + 1}")

    def next_question(self):


        if self.question_number < len(self.question_list):
            user_input = input(f"Q.{self.question_number + 1 }: {self.question_list[self.question_number].text} (True/False)?: ")
            self.check_answer(user_input, self.question_list[self.question_number].answer)

        self.question_number += 1
