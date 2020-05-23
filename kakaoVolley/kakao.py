# 카카오 배구 게임
# 최소원, 박영준
import turtle
import math
import os
import time

screen = turtle.Screen()
screen.setup(1000, 622)  # 화면 크기

# 이미지 추가
screen.addshape("Ryan_jump.gif")
screen.addshape("Apeach_jump.gif")
screen.addshape("발리볼.gif")
screen.addshape("bar.gif")
os.system("BGM02.MID")

# Prayer, 벽 생성
player_A = turtle.Turtle()  # 1p
player_B = turtle.Turtle()  # 2p
wall = turtle.Turtle()      # 벽입니당
turtle.hideturtle()         # 거북이 숨기기
scoreA = turtle.Turtle()    # 점수 A
scoreB = turtle.Turtle()    # 점수 B
ball = turtle.Turtle()      # 공만들기
winAorB = turtle.Turtle()   # 이기는 텍스트 반환


# 점수 띄우기
def show_score():
    winAorB.undo()
    winAorB.hideturtle()
    score_A = 0
    scoreA.color("red")
    scoreA.undo()
    scoreA.penup()
    scoreA.hideturtle()
    scoreA.setposition(-400, 150)
    scorestring1 = "Score : %s" % score_A
    scoreA.write(scorestring1, False, align="left", font=("가비아 솔미체", 20, "bold"))
    score_B = 0
    scoreB.color("red")
    scoreB.undo()
    scoreB.penup()
    scoreB.hideturtle()
    scoreB.setposition(300, 150)
    scorestring2 = "Score : %s" % score_B
    scoreB.write(scorestring2, False, align="left", font=("가비아 솔미체", 20, "bold"))


# 1p가 왼쪽 오른쪽 이동
def a_left():
    if player_A.xcor() > -440:      # x 좌표 이동
        player_A.setheading(180)    # 방향전환
        player_A.forward(10)        # 앞으로 10 이동


def a_right():
    if player_A.xcor() < -40:       # x 좌표 이동
        player_A.setheading(0)      # 방향전환
        player_A.forward(10)        # 앞으로 10 이동


def a_jump():
    gravity1 = 0.2
    player_A.dy = 0
    while True:
        if ball_touch(ball, player_A):
            ball.dy *= -1
        player_A.dy += gravity1
        player_A.sety(player_A.ycor() + player_A.dy)
        if player_A.ycor() > 70:
            player_A.dy *= -1
            gravity1 *= -1
            print(gravity1)
        if player_A.ycor() <= -150:
            player_A.dy = 0
            player_A.sety(-150)
            break


# 2p가 왼쪽 오른쪽 이동하는거염
def b_left():
    if player_B.xcor() > 40:
        player_B.setheading(180)
        player_B.forward(10)


def b_right():
    if player_B.xcor() < 440:
        player_B.setheading(0)
        player_B.forward(10)


def b_jump():
    gravity2 = 0.2
    player_B.dy = 0
    while True:
        if ball_touch(ball, player_B):
            ball.dy *= -1
        player_B.dy += gravity2
        player_B.sety(player_B.ycor() + player_B.dy)
        if player_B.ycor() > 70:
            player_B.dy *= -1
            gravity2 *= -1
            print(gravity2)
        if player_B.ycor() <= -150:
            player_B.dy = 0
            player_B.sety(-150)
            break


# 테두리 만들기
def window_edge():
    turtle.setup(1000, 622)  # Turtle Size
    turtle.clear()
    turtle.penup()
    turtle.speed(0)
    turtle.pensize(7)
    turtle.color("black")
    turtle.goto(-490, 300)
    turtle.pendown()
    turtle.goto(482, 300)
    turtle.goto(482, -290)
    turtle.goto(-490, -290)
    turtle.goto(-490, 300)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.hideturtle()


# 충돌함수
def ball_touch(t1, t2):
    touch = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if touch < 100:
        return True
    else:
        return False


# 게임시작
def kakao():
    turtle.resetscreen()
    show_score()
    player_A.showturtle()
    player_B.showturtle()
    # 테두리 만들고 배경 넣기
    window_edge()
    screen.bgpic("푸른들판1.png")

    # prayer_A 설정
    player_A.penup()
    player_A.speed(0)
    player_A.goto(-200, -150)  # 1p 시작점
    player_A.shape("Ryan_jump.gif")

    player_B.penup()
    player_B.speed(0)
    player_B.goto(200, -150)  # 2p 시작점
    player_B.shape("Apeach_jump.gif")

    # wall 설정
    wall.penup()
    wall.speed(0)
    wall.goto(0, -120)
    wall.shape("bar.gif")
    wall.shapesize(15, 10, 2)

    # ball 설정
    ball.penup()
    ball.speed(0)
    ball.goto(0, 200)
    ball.shape("발리볼.gif")
    ball.dy = 0
    ball.dx = 5     # 포물선 궤적
    gravity = 0.7   # 중력
    score_A = 0     # 재시작 score 초기화
    score_B = 0     # 재시작 score 초기화
    count = 0       # ball 높이가 낮아지는 것을 막기위한 count

    # 앞뒤, 점프 함수
    screen.onkeypress(a_left, "a")
    screen.onkeypress(a_right, "d")
    screen.onkeypress(a_jump, "w")
    screen.onkeypress(b_left, "Left")
    screen.onkeypress(b_right, "Right")
    screen.onkeypress(b_jump, "Up")

    while True:
        winAorB.clear()  # 라이언 어피치 이긴 텍스트 clear
        if score_A >= 5 or score_B >= 5:  # 라이언과 어피치 중 5번 이기면 게임 종료
            gameover(score_A)
            ball.hideturtle()
        if count > 15:  # ball 바운드가 낮아질 경우
            ball.dy = 0  # 바운드 범위 회복
            count = 0
        ball.dy -= gravity  # ball 떨어지는 속력 계산 중력 만큼
        ball.sety(ball.ycor() + ball.dy)
        ball.setx(ball.xcor() + ball.dx)

        if ball.ycor() < -200:  # ball 좌표가 바닥에 떨어지는 경우
            # player A 가 이긴 경우
            if ball.xcor() > 0:
                scoreA.clear()  # score 새로 쓰기위해 이전 score clear
                score_A += 1
                scorestring1 = "Score : %s" % score_A
                scoreA.write(scorestring1, False, align="left", font=("가비아 솔미체", 20, "bold"))
                ball.goto(0, 200)
                ball.dy = 0
                winAorB.goto(0, 0)
                winAorB.color("red")
                winAorB.write("라이언 승!", align="center", font=("가비아 솔미체", 30, "bold"))
                time.sleep(1)

            # player B 가 이긴 경우
            elif ball.xcor() <= 0:
                scoreB.clear()
                score_B += 1
                scorestring2 = "Score : %s" % score_B
                scoreB.write(scorestring2, False, align="left", font=("가비아 솔미체", 20, "bold"))
                ball.goto(0, 200)
                ball.dy = 0
                winAorB.goto(0, 0)
                winAorB.color("red")
                winAorB.write("어피치 승!", align="center", font=("가비아 솔미체", 30, "bold"))
                time.sleep(1)

        # 벽에 닿을 때 방향 전환
        if ball.xcor() > 430 or ball.xcor() < -430:
            ball.dx *= -1

        # 배구 네트에 닿았을 경우 방향 전환
        if ball.ycor() < 30 and -50 < ball.xcor() < 50:
            if ball.ycor() > 20:  # 네트에 위쪽에 닿을 경우 위쪽으로 y축 방향전환
                ball.dy *= -1
            else:                 # 아래쪽 닿을 경우 x축 반대 방향전환
                ball.dx *= -1

        # 공이랑 1p랑 만나면
        if ball_touch(ball, player_A):
            ball.dy *= -1
        # 공이랑 2p라 만나면
        if ball_touch(ball, player_B):
            ball.dy *= -1


# 게임 첫화면
def start():
    scoreA = scoreB = 0  # scoreA, B 초기화
    turtle.resetscreen()

    player_A.reset()
    player_B.reset()
    screen.bgpic("Game start.png")
    turtle.hideturtle()
    turtle.clear()
    turtle.penup()

    turtle.title("Kakao VolleyBall")    # 실행 파일 이름
    screen.onkeypress(kakao, "a")
    screen.listen()  # a 입력받아서 피카게임으로 고고
    turtle.mainloop()


# 게임 오버
def gameover(score_A):
    turtle.speed(0)
    turtle.pu()   # penup
    turtle.goto(0, -30)
    turtle.hideturtle()
    turtle.color("red")
    turtle.write("GAME OVER", align="center", font=("가비아 솔미체", 125, "bold"))
    if score_A == 5:
        turtle.goto(0, -145)
        turtle.color("orange3")
        turtle.write("라이언 승", align="center", font=("가비아 솔미체", 100, "bold"))
    else:
        turtle.goto(0, -145)
        turtle.color("lightpink")
        turtle.write("어피치 승", align="center", font=("가비아 솔미체", 100, "bold"))
    turtle.goto(0, -170)
    turtle.color("midnightblue")
    turtle.write("다시 시작하려면 'r'을 누르세요", align="center", font=("가비아 솔미체", 40, "bold"))

    screen.onkeypress(kakao, "r")
    screen.listen()  # a 입력받아서 카카오게임으로 고고
    turtle.mainloop()


start()  # 게임 시작
