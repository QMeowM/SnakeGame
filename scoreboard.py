from turtle import Turtle

SCORE_COLOR = "maroon"
ALIGNMENT = "center"
FONT = ('Arial', 20, 'bold')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color(SCORE_COLOR)
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)
        self.score += 1

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", False, align=ALIGNMENT, font=FONT)
