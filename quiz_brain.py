# Ask user the questions
# Check if the answers were correct
# Check if we're at the end of the quiz

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0  # keep track which question the user is on. use this to go thru q_list
        self.questions_list = q_list
        self.score = 0

    def still_has_questions(self):
        has_question = True
        return self.question_number < len(self.questions_list)

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_ans = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_ans, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong!")
            print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")