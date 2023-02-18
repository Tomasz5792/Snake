import turtle
import time
import random

score = 0
high_score = 0
delay = 0.1
speed = 20
back_ground_size = 29 #must be odd number
width = 595
height = width
start = (-4, 4)
low_boundary = back_ground_size * -10
high_boundary = back_ground_size * 10



#set up screen
window = turtle.Screen()
window.title('Snake Game')
window.bgcolor('darkgreen')
window.setup(width=width, height=height)
window.tracer(0) #turns off screen updates

#Back ground
#back_ground = turtle.Turtle()
#ack_ground.speed(0)
#back_ground.shape('square')
#back_ground.color('green')
#back_ground.penup()
#back_ground.goto(start)
#back_ground.turtlesize(stretch_wid=back_ground_size, stretch_len=back_ground_size)

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write('Score: 0  High Score: 0', align = 'center', font = ('Courier', 24, 'normal'))


#Snake head
head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('darkred')
head.penup()
head.goto(start)
head.direction = 'stop'
head.turtlesize(stretch_wid=1.1, stretch_len=1.1)

#Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('grey')
food.penup()
x = ((random.randint((-back_ground_size + 1) / 2, (back_ground_size - 1) / 2)) * 20) - 4
y = ((random.randint((-back_ground_size + 1) / 2, (back_ground_size - 1) / 2)) * 20) + 4
food.goto(x, y)

#Snake body
segments = []



#Functions
def go_up():
    if head.direction != 'down':
        head.direction = 'up'

def go_down():
    if head.direction != 'up':
        head.direction = 'down'

def go_left():
    if head.direction != 'right':
        head.direction = 'left'

def go_right():
    if head.direction != 'left':
        head.direction = 'right'

def move():
    if head.direction == 'up':
        head.sety(head.ycor() + speed)

    if head.direction == 'down':
        head.sety(head.ycor() - speed)

    if head.direction == 'left':
        head.setx(head.xcor() - speed)

    if head.direction == 'right':
        head.setx(head.xcor() + speed)

#Keyboard bindings
window.listen()
window.onkeypress(go_up, 'w')
window.onkeypress(go_down, 's')
window.onkeypress(go_left, 'a')
window.onkeypress(go_right, 'd')

#Main game loop
while True:
    window.update()

    #Check  for a colision with the border
    if head.xcor()>high_boundary or head.xcor()<low_boundary or head.ycor()>high_boundary or head.ycor()<low_boundary:
        time.sleep(2)
        head.goto(start)
        head.direction = 'stop'

        #Hide the segments:
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()

        #reset score
        score = 0
        pen.clear()
        pen.write(f'Score: {score}  High Score: {high_score}', align='center', font=('Courier', 24, 'normal'))

    if head.distance(food) < 20:
        #Move food to random spot
        x = ((random.randint((-back_ground_size + 1) / 2, (back_ground_size - 1) / 2)) * 20) - 4
        y = ((random.randint((-back_ground_size + 1) / 2, (back_ground_size - 1) / 2)) * 20) + 4
        food.goto(x, y)

        #Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color('red')
        new_segment.penup()
        new_segment.turtlesize(stretch_wid=1, stretch_len=1)
        segments.append(new_segment)

        #Increase score
        score += 1
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write(f'Score: {score}  High Score: {high_score}', align = 'center', font = ('Courier', 24, 'normal'))


    #Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    #Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    #Check for head collision with body
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(2)
            head.goto(start)
            head.direction = 'stop'

            score = 0
            pen.clear()
            pen.write(f'Score: {score}  High Score: {high_score}', align='center', font=('Courier', 24, 'normal'))

            #Hide segments
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()

    time.sleep(delay)

window.mainloop()