from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):  # quiz_brain: QuizBrain let it know the data type has been passed in
        # passing quiz_brain.py here
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # score label
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        # create canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some questions...",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # true button
        true_img = PhotoImage(file="images/true.png")
        # method inside the command without () because we want it actions when the button actually detects
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        # false button
        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        # show the first question in first round
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        # check if we can get next question as there only have 10 questions in total
        if self.quiz.still_has_questions():
            # everytime change to next question, the background colour should be white
            self.canvas.config(bg="white")

            # change the score shows on the screen
            self.score_label.config(text=f"Score: {self.quiz.score}")

            # import next_question() method from quiz_brain.py
            q_text = self.quiz.next_question()

            # change the current text inside the canvas to the new question text
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            # change the text shows on the canvas
            self.canvas.itemconfig(self.question_text, text="END")

            # disable the button and change background to white
            self.true_button.config(state="disable")
            self.false_button.config(state="disable")
            self.canvas.config(bg="white")

    # when the true button has been pressed
    def true_pressed(self):
        # passing the true or false answer in give_feedback method
        self.give_feedback(self.quiz.check_answer("Ture"))

    # when the false button has been pressed
    def false_pressed(self):
        # same thing passing the true or false answer in give_feedback method but separate into two parts
        check_ans = self.quiz.check_answer("False")
        self.give_feedback(check_ans)

    def give_feedback(self, check_ans):
        # if answer is correct, the canvas background color change to green, else change to red
        if check_ans:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        # set 1000 milliseconds we want to delay, then call get_next_question() method without ()
        self.window.after(1000, self.get_next_question)


