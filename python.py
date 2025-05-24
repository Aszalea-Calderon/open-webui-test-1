import sys
import time
import random

def print_slowly(text, delay=0.05):
    """Prints text character by character with a delay."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def create_snake(length=3):
    """Creates a snake represented as a list of (x, y) coordinates."""
    return [(random.randint(0, 9), random.randint(0, 9)) for _ in range(length)]

def place_snake(snake, food):
    """Places the snake at the head of the snake in the given food coordinates."""
    snake.insert(0, food[0])

def check_collision(snake):
    """Checks if the snake has collided with itself or the walls."""
    head = snake[0]
    if (
        head[0] < 0
        or head[0] >= 10
        or head[1] < 0
        or head[1] >= 10
    ):
        return True
    for segment in snake[1:]:
        if (
            segment[0] == head[0]
            and segment[1] == head[1]
        ):
            return True
    return False

def move_snake(snake, direction):
    """Moves the snake in the given direction."""
    head = snake[0]
    dx, dy = 0, 0
    if direction == "right":
        dx = 1
    elif direction == "left":
        dx = -1
    elif direction == "up":
        dy = -1
    elif direction == "down":
        dy = 1

    new_head = (head[0] + dx, head[1] + dy)
    snake.insert(0, new_head)
    if check_collision(snake):
        snake.pop()  # Remove the tail if collision occurs
    return snake

def main():
    snake = create_snake(length=3)
    food = (random.randint(0, 9), random.randint(0, 9))
    direction = "right"
    game_over = False
    score = 0
    delay = 0.1

    print_slowly("Welcome to Snake!")
    print_slowly("Use 'w' (up), 's' (down), 'a' (left), 'd' (right) to control the snake.")
    print_slowly("Press 'q' to quit.")

    while not game_over:
        # Move the snake
        snake = move_snake(snake, direction)

        # Check for food collision
        if snake[0] == food:
            food = (random.randint(0, 9), random.randint(0, 9))
            score += 1
            print_slowly(f"You ate food! Score: {score}")
        else:
            print_slowly(f"Score: {score}")

        # Print the game state
        print_slowly("  ^" * 9 + "  " + "  " + "  " + "  " + "  " + "  " + "  " + "  " + "  " + "  " + "  " + "  " + "  ")
        for segment in snake:
            print("  " + "  " * segment[0] + segment[1] + "  " + "  " + "  " + "  " + "  ")
        print_slowly("  ^" * 9 + "  " + "  " + "  " + "  " + "  " + "  " + "  " + "  " + "  " + "  " + "  " + "  " + "  ")


        time.sleep(delay)

        # Check for game over (collision with itself or wall)
        if check_collision(snake):
            game_over = True
            print_slowly("Game Over!")

    print_slowly("Thanks for playing!")

if __name__ == "__main__":
    main()