from turtle import Turtle ,Screen
import random


turtles=[]
color=["yellow","green","red","blue","grey","pink"] #"purple","orange","violet","pink","brown","grey"]
movement=[10,20,30]
pos=[-100,-60,-20,20,60,100]
screen=Screen()
screen.setup(width=500,height=400)


ui=screen.textinput(title="Make your Bet",prompt="Which color Turtle wins the race :")




for i in range(0,6):
    t=Turtle(shape="turtle")
    t.color(color[i])
    t.penup()
    t.goto(x=-230,y=pos[i])
    turtles.append(t)
if ui:
    race=True
i=0
while race:
    for tur in turtles:
       if tur.xcor()>230:
           race=False 
           wc=tur.pencolor()
           if wc==ui:
               print(f"your color {ui} have won !!")
           else:
               print(f"your color {ui} has Lost  !!")

       tur.forward(random.randint(0,10))
    
    





screen.exitonclick()