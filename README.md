# Snake Game

## Overview

This is a simple Snake game implemented in Python using the Pygame library. The game features a snake that moves around the screen, eats food, and grows in size. The game ends when the snake collides with the walls or itself.

## Features

- **Snake Movement**: The snake moves continuously in the direction specified by the arrow keys.
- **Food**: Randomly placed on the screen; the snake grows and the score increases when the snake eats the food.
- **Score Display**: Shows the current score in the top-left corner of the screen.
- **Game Over Screen**: Displays the final score and a game over message when the snake collides with the walls or itself.

## Installation

1. **Clone the repository** or download the code to your local machine.

2. **Install Pygame**:
   Ensure you have Python installed, then install Pygame using pip:
   ```bash
   pip install pygame

3. **Run Game**:
   ```bash
   <br>
    python snake_game.py
</br>



## Code Explanation

### Initialization
- **Setup**: Initializes Pygame and sets up the game window with dimensions of 600x400 pixels.
- **Game Variables**: Defines constants for the snake size, frame rate, and colors. Initializes the snake, its direction, the food position, and the score.
- **Font and Clock**: Sets up the font for rendering the score and initializes the game clock to control the frame rate.

### Game Loop
- **Event Handling**: Listens for key presses to change the snake's direction and checks for quit events to close the game.
- **Snake Movement**: Updates the position of the snake based on its current direction. Adds a new head to the snake and removes the last segment unless the snake has eaten food.
- **Collision Detection**: Checks if the snake has collided with the walls or itself. If a collision is detected, the game is reset.
- **Food Consumption**: Checks if the snake's head has collided with the food. If so, increments the score, grows the snake, and spawns a new piece of food.
- **Rendering**: Clears the screen and redraws the snake, food, and score each frame. Updates the display with the current game state.

### Game Over
- **Final Display**: When the game ends, clears the screen and displays a game over message along with the final score. Waits for a few seconds before closing the game.
