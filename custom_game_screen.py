import turtle

# Importing the utility function
from utils import get_user_input


class GameScreen:
    """
    A class to represent and customize the game screen using the turtle graphics library.

    Attributes:
        screen (turtle.Screen): The turtle screen object for the game.
        height (int): The height of the game screen in pixels.
        width (int): The width of the game screen in pixels.
    """

    def __init__(self):
        """
        Initializes the game screen with user-customized settings.
        """
        self.screen = turtle.Screen()
        self.height = get_user_input("Screen height (in pixels)", 600, int)
        self.width = get_user_input("Screen width (in pixels)", 600, int)

        self._setup_screen()

    def _setup_screen(self):
        """
        Configures the screen properties.
        """
        self.screen.bgcolor(get_user_input("Screen color", "black"))
        self.screen.title(get_user_input("Name of game", "Snake Game"))
        self.screen.setup(self.width, self.height)
        self.screen.tracer(0)

    def get_height_boundary(self):
        """
        Calculates the y-coordinate of the upper and lower boundary of the screen.

        Returns:
            int: The y-coordinate of the height boundary.
        """
        return (self.height // 2) - 20

    def get_width_boundary(self):
        """
        Calculates the x-coordinate of the left and right boundary of the screen.

        Returns:
            int: The x-coordinate of the width boundary.
        """
        return (self.width // 2) - 20


if __name__ == "__main__":
    # Example usage
    game_screen = GameScreen()
    turtle.done()
