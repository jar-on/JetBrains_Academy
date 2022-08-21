from random import choice, randrange


class SimpleMathExam:

    LEVEL = {
        '1': 'simple operations with numbers 2-9',
        '2': 'integral squares of 11-29'
    }

    WELCOME_TEXT = (
        'Which level do you want? Enter a number:'
        f'1 - {LEVEL["1"]}'
        f'2 - {LEVEL["2"]}'
    )
    SAVE_QUERY = 'Would you like to save your result to the file? Enter yes or no.'

    def __init__(self):
        self.a = 0
        self.b = 0
        self.operator = None
        self.current_result = 0
        self.correct_results_no = 0
        self.questions_no = 0
        self.difficulty = 0

    def run_exam(self, questions_no=int) -> None:
        """Main functionality;
        questions_no is the number of questions that will be asked"""
        self.set_difficulty_level()
        self.questions_no = questions_no
        for task in range(questions_no):
            self.generate_equation()
            self.check_user_answer()
        self.give_final_mark()

    def generate_equation(self) -> None:
        """ generates a test question based on difficulty and sets all related variables"""
        if self.difficulty == '1':
            self.a = randrange(2, 10)
            self.b = randrange(2, 10)
            self.operator = choice('+-*')
            if self.operator == "+":
                self.current_result = self.a + self.b
            elif self.operator == "-":
                self.current_result = self.a - self.b
            elif self.operator == "*":
                self.current_result = self.a * self.b
            print(self.a, self.operator, self.b)
        else:  # for self.difficulty == '2'
            self.a = randrange(11, 30)
            print(self.a)
            self.current_result = self.a * self.a

    def check_user_answer(self) -> None:
        """checks if user's input is equal to the expected equation result"""
        while True:
            try:
                user_result: int = int(input())
            except ValueError:
                print('Incorrect format.')
                continue
            else:
                if user_result == self.current_result:
                    print('Right!')
                    self.correct_results_no += 1
                else:
                    print('Wrong!')
                break

    def give_final_mark(self) -> None:
        """Calculates final mark on basis of the number of correct test answers"""
        mark = f'{self.correct_results_no}/{self.questions_no}'
        print(f'Your mark is {mark}')
        if input(self.SAVE_QUERY).lower() in ('yes', 'y'):  # functionality for saving results
            name = input('What is your name?')
            with open('results.txt', 'a') as file:
                file.write(f'{name}: {mark} in level {self.difficulty} ({self.LEVEL[self.difficulty]}).')
            print('The results are saved in "results.txt".')

    def set_difficulty_level(self) -> None:
        """sets the difficulty of the test"""
        while True:
            self.difficulty = input(self.WELCOME_TEXT)
            if self.difficulty not in ('1', '2'):
                print('Incorrect format')
                continue
            break


exam1 = SimpleMathExam()
exam1.run_exam(questions_no=5)
