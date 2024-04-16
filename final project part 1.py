import random


class QuizMaker:
    def __init__(self):
        self.questions = [
            {"question": "Who created Python?", "options": {"a": "Guido van Rossum", "b": "Bjarne Stroustrup", "c": "Brendan Eich", "d": "Linus Torvalds"}, "correct_answer": "a"},
            {"question": "Which function is non-mutable?", "options": {"a": "list", "b": "tuple", "c": "both A and B", "d": "none of the above"}, "correct_answer": "c"},
            {"question": "What does the multiline continuation character do?", "options": {"a": "Breaks a statement into multiple lines", "b": "Adds a return in between lines", "c": "Splits the statement into separate arguments", "d": "None of the above"}, "correct_answer": "a"},
            {"question": "What function gives the items stored in a dictionary in Python? (Both keys and values in list as tuple.)", "options": {"a": "dict.values()", "b": "dictionary.keysandvalues()", "c": "dictionary.items()", "d": "None of the above"}, "correct_answer": "c"},
            {"question": "Are strings mutable or immutable?", "options": {"a": "Mutable", "b": "Immutable", "c": "Neither", "d": "Both mutable and immutable"}, "correct_answer": "b"},
            {"question": "In C++, what character does a preprocessor directive begin with?", "options": {"a": "!", "b": "*", "c": "#", "d": "$"}, "correct_answer": "c"},
            {"question": "In Python what does Pass do?", "options": {"a": "Pass a value to a function.", "b": "Continue the program after an exception is caught.", "c": "Terminate a loop.", "d": "None of the above"}, "correct_answer": "b"},
            {"question": "What does GPU stand for?", "options": {"a": "Graphics Processing Unit", "b": "Graphics Performance Unit", "c": "Graphics Processing Arena", "d": "Graphics Performance Arena"}, "correct_answer": "a"},
            {"question": "What does LAN stand for?", "options": {"a": "Local Arena Network", "b": "Light Area Network", "c": "Local Area Network", "d": "Light Arena Network"}, "correct_answer": "c"},
            {"question": "What does DMA stand for?", "options": {"a": "Directional Mapping Area", "b": "Direct Memory Access", "c": "Direct Mainstream Arena", "d": "Digital Memory Access"}, "correct_answer": "b"},
        ]
        if len(self.questions) < 10:
            raise ValueError("The question bank should have at least 10 questions.")

    def get_info(self):
        attempts = 0
        while attempts < 3:
            quiz_data.student_id = input("Enter your student ID (format: A12345): ")
            if quiz_data.student_id.startswith('A') and quiz_data.student_id[1:].isdigit() and len(quiz_data.student_id) == 6:
                quiz_data.first_name = input("Enter your First name: ")
                return True
            else:
                print("Invalid ID format. Please enter a valid ID.")
                attempts += 1
        print("You have exceeded the maximum number of attempts. Exiting...")
        return False

    def display_question(self, question):
        print("\nQuestion: " + question["question"])
        for option, text in question["options"].items():
            print(option + ". " + text)

    def get_answer(self, question):
        while True:
            choice = input("Enter your answer (a, b, c, or d): ").lower()
            if choice in question["options"]:
                return choice
            else:
                print("Invalid choice. Please enter a valid option.")

    def conduct_quiz(self):
        quiz_data.score = 0
        for question in quiz_data.questions:
            self.display_question(question)
            while True:
                answer = self.get_answer(question)
                if answer == question["correct_answer"]:
                    quiz_data.score += 1
                    break  
                else:
                    print("Incorrect answer. Please try again.")

    def save_results(self):
        filename = quiz_data.student_id + ".txt"
        with open(filename, "w") as file:
            file.write("Student ID: " + quiz_data.student_id + "\n")
            file.write("First name: " + quiz_data.first_name + "\n")
            file.write("Score: " + str(quiz_data.score) + "/10\n")

    def start(self):
        while True:
            if self.get_info():
                self.conduct_quiz()
                self.save_results()
                print("Quiz completed. Results saved.")

            choice = input("Enter 'Q' to quit or any other key to start a new quiz: ").upper()
            if choice == 'Q':
                break
            else:
                continue

if __name__ == "__main__":
    quiz_data = QuizMaker()
    quiz_data.start()
