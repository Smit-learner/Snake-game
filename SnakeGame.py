import turtle

import time

import random



delay=0.1

score=0

high_score=0





window=turtle.Screen()

window.title('snake game by smit')

window.bgpic("bg.png")

window.setup(width=600,height=600)

window.tracer(0)



#snake head

head=turtle.Turtle()

head.speed(0)

head.shape('circle')

head.color('blue')

head.penup()

head.goto(0,0)

head.direction='stop'

#food

food=turtle.Turtle()

food.speed(0)

food.shape('circle')

food.color('red')

food.penup()

food.goto(0,100)



segments=[]

wlcm=turtle.Turtle()

wlcm.shape('square')

wlcm.penup()



wlcm.goto(-260,-260)

wlcm.write('Use W S D A for playing',font=('Courier',16,'bold'))

wlcm.hideturtle()

#pen

pen=turtle.Turtle()

pen.shape('square')

pen.penup()

pen.hideturtle()

pen.goto(0,260)

pen.write('Score:0 Highscore=0',align='center',font=('Courier',24,'normal'))















#FUNCTION

def go_up():

    if head.direction !='down':

        head.direction='up'

def go_down():

    if head.direction != 'up':

        head.direction='down'

def go_right():

    if head.direction != 'left':

        head.direction='right'

def go_left():

    if head.direction != 'right':

        head.direction='left'

















def move():

    if head.direction=='up':

        y=head.ycor()

        head.sety(y+20)

    if head.direction=='down':

        y=head.ycor()

        head.sety(y-20)

    if head.direction=='right':

        x=head.xcor()

        head.setx(x-20)

    if head.direction=='left':

        x=head.xcor()

        head.setx(x+20)



#keyboard

window.listen()

window.onkeypress(go_up,'w')

window.onkeypress(go_down,'s')

window.onkeypress(go_left,'d')

window.onkeypress(go_right,'a')





#main game loop

while True:

    window.update()

    #chek for collison

    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:

        time.sleep(1)

        head.goto(0,0)

        head.direction='stop'



        for segment in  segments:

            segment.goto(1000,1000)

        segments.clear()

        score=0

        pen.clear()

        pen.write('Score:{} High score:{}'.format(score, high_score),

                  align='center',

                  font=('Courier', 24, 'normal')

                  )



    if head.distance(food)<20:

        x=random.randint(-290,290)

        y=random.randint(-290,290)

        food.goto(x,y)



        new_seg=turtle.Turtle()

        new_seg.speed(0)

        new_seg.shape('square')

        new_seg.color('yellow')

        new_seg.penup()

        segments.append(new_seg)



        score+=1

        if score>high_score:

            high_score=score

        pen.clear()

        pen.write('Score:{} High score:{}'.format(score,high_score),

                  align='center',

                  font=('Courier',24,'normal')

                  )



    #move the end sagment

    for index in range(len(segments)-1,0,-1):

        x=segments[index-1].xcor()

        y=segments[index-1].ycor()

        segments[index].goto(x,y)

    #move 0 th seg to head

    if len(segments)>0:

        x=head.xcor()

        y=head.ycor()

        segments[0].goto(x,y)



    move()

    #after move



    for segment in segments:

        if segment.distance(head)<20:

            time.sleep(1)

            head.goto(0,0)

            head.direction='stop'

            for segment in segments:

                segment.goto(1000, 1000)

            segments.clear()

            score = 0

            pen.clear()

            pen.write('Score:{} High score:{}'.format(score, high_score),

                      align='center',

                      font=('Courier', 24, 'normal')

                      )





    time.sleep(delay)











window.mainloop()
