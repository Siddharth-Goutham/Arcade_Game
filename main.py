from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score_board import Score_board
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Arcade Game")
screen.tracer(0)

l_player=screen.textinput("Left Player","Name of the left player")
r_player=screen.textinput("Right Player","Name of the right player")
points_box=int(screen.textinput("Points","For how many points do you want to play"))


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score_board = Score_board()
write_won=Turtle()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()



    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score_board.l_point()

    #Detect L paddle misses:
    if ball.xcor() < -380:
        ball.reset_position()
        score_board.r_point()

    if score_board.l_score==points_box:
        write_won.color("white")
        write_won.hideturtle()
        screen.clear()
        screen.bgcolor("black")
        score_board.update_scoreboard()
        write_won.write(f"{l_player} Won🎉🎉",align="center", font=("Courier", 30, "normal"))
        break

    elif score_board.r_score==points_box:
        write_won.color("white")
        screen.clear()
        screen.bgcolor("black")
        score_board.update_scoreboard()
        write_won.write(f"{r_player} Won🎉🎉",align="center", font=("Courier", 30, "normal"))
        break



screen.exitonclick()