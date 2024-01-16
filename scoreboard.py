from turtle import Turtle

# Importing the utility function
from utils import get_user_input


class Scoreboard(Turtle):
    """
    A class to represent and manage the game's scoreboard, inheriting from Turtle.

    Attributes:
        game_screen (GameScreen): The game screen object where the scoreboard is displayed.
        score (int): Current score of the game.
        alignment (str): Text alignment for the scoreboard.
        font_type (str): Font type for the scoreboard text.
        font_size (int): Font size for the scoreboard text.
        font_style (str): Font style (normal or bold) for the scoreboard text.
    """

    def __init__(self, game_screen):
        """
        Initializes the scoreboard with customizable settings.

        Args:
            game_screen (GameScreen): The game screen object to display the scoreboard.
        """
        super().__init__()
        self.game_screen = game_screen
        self.score = 0

        self.alignment = get_user_input("How should the scoreboard be aligned?", "center")
        self.font_type = get_user_input("What font should the scoreboard text be?", "Arial")
        self.font_size = get_user_input("What font size should the scoreboard text be?", 16, int)
        self.font_style = get_user_input("Should the font be normal or bold?", "normal")
        self.color(get_user_input("What color should the scoreboard text be?", "white"))

        self.penup()
        self.hideturtle()
        self.goto(0, self.game_screen.get_height_boundary() - 40)
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Updates and displays the current score on the scoreboard.
        """
        self.clear()
        self.write(f"Score: {self.score}", align=self.alignment, font=(self.font_type, self.font_size, self.font_style))

    def game_over(self):
        """
        Displays the 'Game Over' message.
        """
        self.goto(0, 0)
        self.write("GAME OVER", align=self.alignment, font=(self.font_type, self.font_size, self.font_style))

    def increase_score(self):
        """
        Increases the game score and updates the scoreboard.
        """
        self.score += 1
        self.update_scoreboard()


if __name__ == "__main__":
    # Example usage
    from custom_game_screen import GameScreen
    import turtle

    def exit_game():
        """
        Exits the game after a delay, allowing time to view the scoreboard.
        """
        game_screen.screen.bye()

    game_screen = GameScreen()
    scoreboard = Scoreboard(game_screen)
    scoreboard.increase_score()

    # Set a timer to exit the game after 4000 milliseconds (4 seconds)
    turtle.ontimer(exit_game, 4000)

    turtle.mainloop()
