import tkinter as tk
from tkinter import messagebox

questions = [
    {
        "question": "What is the output of: print(2**3)?",
        "options": ["6", "8", "9", "5"],
        "answer": "8"
    },
    {
        "question": "Which keyword is used for function in Python?",
        "options": ["fun", "def", "function", "define"],
        "answer": "def"
    },
    {
        "question": "What data type is the object below?\nx = [1, 2, 3]",
        "options": ["List", "Tuple", "Dictionary", "Set"],
        "answer": "List"
    },
    {
        "question": "Which operator is used for floor division?",
        "options": ["/", "%", "//", "**"],
        "answer": "//"
    },
    {
        "question": "What does len([1, 2, 3, 4]) return?",
        "options": ["3", "4", "5", "Error"],
        "answer": "4"
    },
    {
        "question": "Which of the following is a Python tuple?",
        "options": ["[1,2,3]", "(1,2,3)", "{1,2,3}", "<1,2,3>"],
        "answer": "(1,2,3)"
    },
    {
        "question": "What will be the output of: bool(0)?",
        "options": ["True", "False", "0", "1"],
        "answer": "False"
    },
    {
        "question": "Which function converts a string to lowercase?",
        "options": ["lower()", "uppercase()", "down()", "lowerCase()"],
        "answer": "lower()"
    },
    {
        "question": "What is the correct file extension for Python files?",
        "options": [".pyt", ".pyth", ".pt", ".py"],
        "answer": ".py"
    },
    {
        "question": "How do you start a comment in Python?",
        "options": ["//", "/*", "#", "--"],
        "answer": "#"
    },
    {
        "question": "Which keyword is used to create a class?",
        "options": ["class", "define", "object", "struct"],
        "answer": "class"
    },
    {
        "question": "How do you insert COMMENTS in Python?",
        "options": ["/* comment */", "# comment", "// comment", "<!-- comment -->"],
        "answer": "# comment"
    },
    {
        "question": "Which is not a core data type in Python?",
        "options": ["List", "Dictionary", "Class", "Tuple"],
        "answer": "Class"
    },
    {
        "question": "What is the correct way to create a function in Python?",
        "options": ["create myFunc():", "function myFunc():", "def myFunc():", "func myFunc():"],
        "answer": "def myFunc():"
    },
    {
        "question": "What does the 'pass' statement do?",
        "options": ["Exits the loop", "Skips the iteration", "Does nothing", "Terminates program"],
        "answer": "Does nothing"
    },
    {
        "question": "What is the output of: type('Hello')?",
        "options": ["str", "int", "list", "bool"],
        "answer": "str"
    },
    {
        "question": "Which of the following is a loop in Python?",
        "options": ["repeat", "for", "do", "iterate"],
        "answer": "for"
    },
    {
        "question": "How do you get the length of a string?",
        "options": ["count()", "length()", "len()", "size()"],
        "answer": "len()"
    },
    {
        "question": "Which is used to handle exceptions in Python?",
        "options": ["catch", "try/except", "error/handle", "do/except"],
        "answer": "try/except"
    },
    {
        "question": "What does range(5) return?",
        "options": ["1 to 5", "0 to 4", "0 to 5", "1 to 4"],
        "answer": "0 to 4"
    }
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Quiz - 1 Mark Each")
        self.root.geometry("600x400")
        self.qn = 0
        self.score = 0
        self.selected_answers = [tk.StringVar() for _ in questions]

        self.create_widgets()
        self.display_question()

    def create_widgets(self):
        self.ques_label = tk.Label(self.root, width=80, height=4, wraplength=500, font=('Arial', 12, 'bold'), anchor='w', justify='left')
        self.ques_label.pack(pady=10)

        self.option_buttons = []
        self.options_frame = tk.Frame(self.root, bg="#f9f9f9")
        self.options_frame.pack()

        for i in range(4):
            btn = tk.Radiobutton(self.options_frame, text="", variable=self.selected_answers[self.qn],
                                 value="", font=("Arial", 11), anchor='w', justify='left',
                                 bg="#f0f0f0", width=50, padx=10, pady=5, indicatoron=0, relief="groove", borderwidth=1)
            btn.pack(pady=5)
            self.option_buttons.append(btn)

        nav_frame = tk.Frame(self.root)
        nav_frame.pack(pady=20)

        self.prev_btn = tk.Button(nav_frame, text="Previous", command=self.prev_question, width=10, font=("Arial", 11))
        self.prev_btn.grid(row=0, column=0, padx=20)

        self.next_btn = tk.Button(nav_frame, text="Next", command=self.next_question, width=10, font=("Arial", 11))
        self.next_btn.grid(row=0, column=1, padx=20)

    def display_question(self):
        q = questions[self.qn]
        self.ques_label.config(text=f"Q{self.qn + 1}: {q['question']}")
        var = self.selected_answers[self.qn]

        for i in range(4):
            self.option_buttons[i].config(text=q['options'][i], value=q['options'][i], variable=var)

        # Enable/disable Previous button
        self.prev_btn.config(state=tk.NORMAL if self.qn > 0 else tk.DISABLED)

    def next_question(self):
        if self.selected_answers[self.qn].get() == questions[self.qn]['answer']:
            pass  # Score will be calculated at the end

        if self.qn < len(questions) - 1:
            self.qn += 1
            self.display_question()
        else:
            self.calculate_score()

    def prev_question(self):
        if self.qn > 0:
            self.qn -= 1
            self.display_question()

    def calculate_score(self):
        self.score = 0
        for i in range(len(questions)):
            if self.selected_answers[i].get() == questions[i]['answer']:
                self.score += 1
        messagebox.showinfo("Quiz Completed", f"You scored {self.score}/{len(questions)}")
        self.root.quit()

root = tk.Tk()
app = QuizApp(root)
root.mainloop()

