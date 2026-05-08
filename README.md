# Modified Snake Game - Python Project

## General Description

This project consists of modifying the Snake game from the Python freegames package. The main objective was to understand the original code and implement new required features related to movement, colors, and documentation.

The game was developed and tested using Python, Turtle Graphics, Git, GitHub, and WSL Ubuntu.

---

# Original Game

The original Snake game was copied using the following command:

freegames copy snake

---

# Required Modifications

The activity required the following changes:

1. The food must move randomly one step at a time.
2. The food must not leave the game window.
3. Each time the game runs, the snake and the food must have different random colors.
4. The colors must be selected from a group of five colors.
5. Red must not be used as one of the random colors.

---

# Changes Made

The following modifications were implemented:

- A list of five colors was created: green, blue, purple, orange, and black.
- The snake color is randomly selected when the game starts.
- The food color is also randomly selected when the game starts.
- A validation was added to make sure the snake and food colors are always different.
- The food was modified so it moves randomly one step at a time.
- The food movement was restricted so it cannot leave the game window.
- The code was documented using comments and function descriptions.

---

# Controls

- Right arrow = move right
- Left arrow = move left
- Up arrow = move up
- Down arrow = move down

---

# Technologies Used

- Python 3
- Turtle Graphics
- Freegames
- Git
- GitHub
- WSL Ubuntu
- Nano Editor

---

# Commands Used

Copy the original game:

freegames copy snake

Run the game:

python3 snake.py

Git commands:

git add .
git commit -m "Modified snake game"
git push

---

# Conclusion

The Snake game was successfully modified to meet the required features. The food now moves randomly without leaving the window, and the snake and food use random colors from a predefined list of five colors, excluding red. The final version was tested and uploaded to GitHub with proper documentation and commit history.

---

# Author

Ivan Hernandez
