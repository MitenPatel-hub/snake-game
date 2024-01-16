from game_configuration import GamePlay, Food
from scoreboard import Scoreboard


class SnakeGame:
    """
    A class to manage the overall gameplay of the snake game.

    Attributes:
        game_screen (GameScreen): An instance of the game screen.
        game_play (GamePlay): Manages the gameplay settings and mechanics.
        score_board (Scoreboard): Manages the game's scoreboard.
        food (Food): Manages the food for the snake.
        game_is_on (bool): Indicates whether the game is currently active.
        """
    def __init__(self, game_screen):
        """
        Initializes the SnakeGame with the provided game screen.

        Args:
            game_screen (GameScreen): The game screen to be used for the game.
        """
        self.game_is_on = True
        self.game_screen = game_screen
        self.game_play = GamePlay(game_screen)
        self.score_board = Scoreboard(game_screen)
        self.food = Food(game_screen)
        self._initialize_movement_controls()

    def _initialize_movement_controls(self):
        """
        Sets up keyboard bindings for controlling the snake's movement.
        """
        self.game_screen.screen.listen()
        self.game_screen.screen.onkey(self.game_play.up, "Up")
        self.game_screen.screen.onkey(self.game_play.down, "Down")
        self.game_screen.screen.onkey(self.game_play.left, "Left")
        self.game_screen.screen.onkey(self.game_play.right, "Right")

    def play(self):
        """
        Executes game logic for a single iteration of the game loop.
        """
        # self.game_screen.screen.update()
        self.game_play.move_snake()

        # Check for food collision
        if self.game_play.head.distance(self.food) < 15:
            self.food.refresh()
            self.game_play.extend_snake()
            self.score_board.increase_score()

        # Check for wall collision
        if (abs(self.game_play.head.xcor()) > self.game_screen.get_width_boundary() or
                abs(self.game_play.head.ycor()) > self.game_screen.get_height_boundary()):
            self.game_is_on = False
            self.score_board.game_over()

        # Check for tail collision
        for segment in self.game_play.segments[1:]:
            if self.game_play.head.distance(segment) < 10:
                self.game_is_on = False
                self.score_board.game_over()



