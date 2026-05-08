"""Modified Snake game.

Changes made:
1. The food moves randomly one step at a time.
2. The food does not leave the game window.
3. The snake and food get random colors each time the game starts.
4. The snake and food always have different colors.
5. The colors are selected from five colors, excluding red.
"""

from turtle import *
from random import choice, randrange
from freegames import square, vector

colors = ['green', 'blue', 'purple', 'orange', 'black']

snake_color = choice(colors)
food_color = choice(colors)

while food_color == snake_color:
    food_color = choice(colors)

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head is inside boundaries."""
   return -190 < head.x < 190 and -190 < head.y < 190


def move_food():
    """Move food randomly one step without leaving the window."""
    movement = choice([
        vector(10, 0),
        vector(-10, 0),
        vector(0, 10),
        vector(0, -10)
    ])

    new_food = food + movement

    if inside(new_food):
        food.x = new_food.x
        food.y = new_food.y


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'gray')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)
        move_food()

    clear()

    for body in snake:
        square(body.x, body.y, 9, snake_color)

    square(food.x, food.y, 9, food_color)
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()

onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')

move()
done()
