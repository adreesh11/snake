from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0 , 270)
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", move=True, align='center', font=('Arial', 14, "normal"))
    def increase_score(self):
        self.score += 1
        self.clear()
        self.goto( 0 , 270)
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", True , 'center' , font = ('Arial', 14, "normal"))