from turtle import Turtle
import random

# Importing the utility function
from utils import get_user_input

# Constants for direction
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Food(Turtle):
    """
    A class to represent and manage the food in the game, inheriting from Turtle.

    Attributes:
        game_screen (GameScreen): The game screen object where the food is displayed.
    """

    def __init__(self, game_screen):
        """
        Initializes the food object with customizable settings.

        Args:
            game_screen (GameScreen): The game screen object to display the food.
        """
        super().__init__()
        self.game_screen = game_screen

        self.shape(get_user_input("What shape should the food be?", "circle"))
        self.color(get_user_input("What color should the food be?", "red"))
        self.penup()
        self.speed("fastest")  # Fastest animation speed
        self.refresh()

    def refresh(self):
        """
        Places the food at a random location within the game boundaries.
        """
        random_x = random.randint(-self.game_screen.get_width_boundary(), self.game_screen.get_width_boundary())
        random_y = random.randint(-self.game_screen.get_height_boundary(), self.game_screen.get_height_boundary())
        self.goto(random_x, random_y)


class GamePlay:
    """
    A class to manage the game settings and mechanics in the snake game.

    Attributes:
        game_screen (GameScreen): The game screen where the gameplay takes place.
        snake_speed (float): The time delay (in seconds) between each movement of the snake.
        snake_distance (int): The distance each segment of the snake moves per step.
        snake_color (str): The color of the snake.
        segment_shape (str): The shape of each segment of the snake.
        nr_segments (int): The initial number of segments of the snake.
        segments (list): A list of Turtle objects that represent the snake's segments.
        head (Turtle): The first segment of the snake, acting as the head.
        tail (Turtle): The last segment of the snake, acting as the tail.
    """

    def __init__(self, game_screen):
        """
        Initializes the game settings.

        Args:
            game_screen (GameScreen): The game screen object to play the game.
        """
        self.game_screen = game_screen
        self.snake_speed = get_user_input("How many seconds between each movement?", 0.1, float)
        self.snake_distance = get_user_input("How many paces should the snake move during each movement?", 20, int)
        self.snake_color = get_user_input("What color would you like the snake to be?", "white")
        self.segment_shape = get_user_input("What shape would you like the segments to be?", "square")
        self.nr_segments = get_user_input("How many segments would you like the snake to have?", 3, int)
        self.segments = []
        self.head = None
        self.tail = None
        self._construct_snake()

    def _construct_snake(self):
        """
        Constructs the initial snake at the start of the game.

        This method creates a number of snake segments (Turtles), as specified by nr_segments.
        Each segment is positioned horizontally with a specified gap (20 pixels by default).
        The first segment created is treated as the head of the snake.
        """
        x = 0
        for _ in range(self.nr_segments):
            segment = Turtle(self.segment_shape)
            segment.color(self.snake_color)
            segment.penup()
            segment.goto(x, 0)
            self.segments.append(segment)
            x -= 20  # Moving the x-coordinate for the next segment to position each segment with a gap of 20 pixels.
        self.head = self.segments[0]
        self.tail = self.segments[-1]

    def extend_snake(self):
        """
        Adds a new segment to the snake's tail.

        This method is called when the snake eats food. A new segment is created at the position of the last segment
        (the current tail) of the snake, effectively extending the snake.
        """
        new_segment = Turtle(shape=self.segment_shape)
        new_segment.color(self.snake_color)
        new_segment.penup()
        new_segment.goto(self.tail.position())  # Positioning the new segment at the tail.
        self.segments.append(new_segment)  # Adding the new segment to the list of segments.
        self.tail = new_segment  # Update the tail reference

    def move_snake(self):
        """
        Moves the entire snake forward in its current direction.

        This method updates the position and heading of each segment of the snake. Starting from the tail, each segment
        moves to the position of the segment in front of it and checks that their heading directions match. The segment
        adjusts heading position if the snake has turned directions in the game based on key press. The head of the
        snake (first segment) then moves forward in its specified heading direction by a distance of snake_distance.
        Each segment between head and tail then moves forward by same snake_distance and adopts the heading of the
        segment in front of it.
        """
        for i in range(len(self.segments) - 1, 0, -1):
            # This loop iterates backwards through the snake's segments, starting from the tail and ending at the
            # segment just behind the head.
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)  # Moving each segment to the position of the next segment.

        # Update the headings of the segments
        for i in range(1, len(self.segments)):
            # This loop iterates forwards, starting from the first segment (just behind the head) to the tail. The goal
            # is to update the heading (orientation) of each segment to match the segment in front of it. The loop
            # starts at 1 (the second segment) because the first segment (the head) sets the direction for the rest, and
            # its heading doesn't need to be updated in this context.
            self.segments[i].setheading(self.segments[i - 1].heading())

        self.head.forward(self.snake_distance)  # Moving the head forward.

    def up(self):
        """
        Changes the snake's direction to upwards if not moving downwards.
        """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """
        Changes the snake's direction to downwards if not moving upwards.
        """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """
        Changes the snake's direction to left if not moving right.
        """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """
        Changes the snake's direction to right if not moving left.
        """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


# Unit Test
if __name__ == "__main__":
    from custom_game_screen import GameScreen
    import turtle

    game_screen = GameScreen()
    gameplay = GamePlay(game_screen)

    # Test Movement
    turtle.listen()
    turtle.onkey(gameplay.up, "Up")
    turtle.onkey(gameplay.down, "Down")
    turtle.onkey(gameplay.left, "Left")
    turtle.onkey(gameplay.right, "Right")

    while True:
        game_screen.screen.update()
        gameplay.move_snake()
