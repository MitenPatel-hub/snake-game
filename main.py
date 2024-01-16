from custom_game_screen import GameScreen
from snake_game import SnakeGame
import time


def main():
    """
    Main function to set up the game and start the gameplay loop.
    """
    game_screen = GameScreen()
    snake_game = SnakeGame(game_screen)

    while snake_game.game_is_on:
        game_screen.screen.update()
        snake_game.play()
        time.sleep(snake_game.game_play.snake_speed)

    game_screen.screen.exitonclick()


if __name__ == "__main__":
    main()
