from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.goto(0, 270)
        self.color("white")
        self.shapesize(stretch_wid=40, stretch_len=40)
        self.hideturtle()
        self.update_scoreboard()

    def add(self):
        self.score += 1

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Courier", 18, "normal"))

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", mode="w") as file:
                file.write(f"{self.score}")
                self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
