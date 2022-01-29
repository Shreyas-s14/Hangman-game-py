import colorama
from colorama import Style
import turtle 
import random
colorama.init()
Red = '\033[31m' 
Green="\033[0;32m"


#figure out if you guess a word DONE
#what to do if letters are repeated
l_sports=["basketball","football","cricket","tennis","soccer","badminton","hockey","squash","baseball","golf"]
l_animals=["bear","tiger","lion","deer","elephant","giraffe","flamingo","penguin","rhinoceros","gorilla","leopard"]
l_colours=["black","brown","blue","red","pink","purple","violet","indigo","yellow","orange"]

#smallest length is 3 then 4,5,6,7,8,9,10


#input user's choice of word
flag2=0
l=int(input("Which category would you like to choose from? Enter the number depending on your choice-\n1.Sports\n2.Animals\n3.Colours\n"))
if(l==1):   
    word=random.choice(l_sports)
    flag2=1
elif(l==2):
    word=random.choice(l_animals)
    flag2=1
elif(l==3):
    word=random.choice(l_colours)
    flag2=1
else:
    print(Red+"Wrong input")
flag3=0
while(flag2==0 and flag3==0):
    l=int(input("Which category would you like to choose from? Enter the number depending on your choice-\n1.Sports\n2.Animals\n3.Colours\n"))
    if(l==1):   
        word=random.choice(l_sports)
        flag3=1
    elif(l==2):
        word=random.choice(l_animals)
        flag3=1
    elif(l==3):
        word=random.choice(l_colours)
        flag3=1
    else:
        print(Red+"Wrong input!")
        continue
        
  

def w1():
    import turtle
    #from turtle import Screen
    #screen=Screen()
    t=turtle.Turtle()
    t.hideturtle()
    t.speed(100)
    t.penup()
    t.rt(90)
    t.fd(200)
    t.rt(90)
    t.pendown()
    t.fd(100)
    t.rt(90)
    t.fd(250)
    t.rt(90)
    t.fd(80)
    t.rt(90)
    t.fd(50)
    t.rt(90)
    t.fd(3)
    t.circle(20) 
    t.penup()
    t.rt(90)
    t.fd(100)
    t.write("Click your mouse to exit",font=16)
    turtle.exitonclick()
    turtle.TurtleScreen._RUNNING = True
def w2():
    
    t=turtle.Turtle()
    t.hideturtle()
    t.speed(200)
    t.penup()
    t.rt(90)
    t.fd(200)   
    t.rt(90)
    t.pendown()
    t.fd(100)
    t.rt(90)
    t.fd(250)
    t.rt(90)
    t.fd(80)
    t.rt(90)
    t.fd(50)
    t.rt(90)
    t.fd(3)
    t.circle(20)
    t.penup()
    t.rt(270)
    t.fd(40)
    t.pendown()
    t.fd(50)
    t.penup()
    t.rt(180)
    t.fd(190)
    t.write("Click your mouse to exit",font=16)
    turtle.exitonclick()
    turtle.TurtleScreen._RUNNING = True
def w3():
    t=turtle.Turtle()
    t.hideturtle()
    t.speed(200)
    t.penup()
    t.rt(90)
    t.fd(200)
    t.rt(90)
    t.pendown()
    t.fd(100)
    t.rt(90)
    t.fd(250)
    t.rt(90)
    t.fd(80)
    t.rt(90)
    t.fd(50)
    t.rt(90)
    t.fd(3)
    t.circle(20)
    t.penup()
    t.rt(270)
    t.fd(40)
    t.pendown()
    t.fd(50)
    t.bk(30)
    t.rt(135)
    t.fd(30)
    t.penup()
    t.bk(30)
    t.rt(45)
    t.fd(160)
    t.write("Click your mouse to exit",font=16)
    turtle.exitonclick()
    turtle.TurtleScreen._RUNNING = True
def w4():
    t=turtle.Turtle()
    t.hideturtle()
    t.speed(200)
    t.penup()
    t.rt(90)
    t.fd(200)
    t.rt(90)
    t.pendown()
    t.fd(100)
    t.rt(90)
    t.fd(250)
    t.rt(90)
    t.fd(80)
    t.rt(90)
    t.fd(50)
    t.rt(90)
    t.fd(3)
    t.circle(20)
    t.penup()
    t.rt(270)
    t.fd(40)
    t.pendown()
    t.fd(50)
    t.bk(30)
    t.rt(135)
    t.fd(30)
    t.bk(30)
    t.rt(90)
    t.fd(30)
    t.penup()
    t.bk(30)
    t.lt(45)
    t.fd(160)
    t.write("Click your mouse to exit",font=16)
    turtle.exitonclick()
    turtle.TurtleScreen._RUNNING = True
def w5():
    t=turtle.Turtle()
    t.hideturtle()
    t.speed(200)
    t.penup()
    t.rt(90)
    t.fd(200)
    t.rt(90)
    t.pendown()
    t.fd(100)
    t.rt(90)
    t.fd(250)
    t.rt(90)
    t.fd(80)
    t.rt(90)
    t.fd(50)
    t.rt(90)
    t.fd(3)
    t.circle(20)
    t.penup()
    t.rt(270)
    t.fd(40)
    t.pendown()
    t.fd(50)
    t.bk(30)
    t.rt(135)
    t.fd(30)
    t.bk(30)
    t.rt(90)
    t.fd(30)
    t.bk(30)
    t.rt(135)
    t.fd(30)
    t.rt(45)
    t.fd(40)
    t.penup()
    t.bk(40)
    t.rt(135)
    t.fd(190)
    t.write("Click your mouse to exit",font=16)
    turtle.exitonclick()
    turtle.TurtleScreen._RUNNING = True
def w6():
    t=turtle.Turtle()
    t.hideturtle()
    t.speed(200)
    t.penup()
    t.rt(90)
    t.fd(200)
    t.rt(90)
    t.pendown()
    t.fd(100)
    t.rt(90)
    t.fd(250)
    t.rt(90)
    t.fd(80)
    t.rt(90)
    t.fd(50)
    t.rt(90)
    t.fd(3)
    t.circle(20)
    t.penup()
    t.rt(270)
    t.fd(40)
    t.pendown()
    t.fd(50)
    t.bk(30)
    t.rt(135)
    t.fd(30)
    t.bk(30)
    t.rt(90)
    t.fd(30)
    t.bk(30)
    t.rt(135)
    t.fd(30)
    t.rt(45)
    t.fd(40)
    t.bk(40)
    t.lt(90)
    t.fd(40)
    t.penup()
    t.bk(40)
    t.lt(135)
    t.fd(190)
    t.write("You lost! Click your mouse to exit",font=16)
    turtle.exitonclick()
    turtle.TurtleScreen._RUNNING = True
def main():
    new=[]
    flag=0
    flag1=0
    wrong=0
    cor=0
    b=0
    c=0
    rptd=[]
    print("The length of the word is:",len(word),"letters")
    for i in range(len(word)):
            new.append("_ ")
    while(wrong<=6 and flag!=1):
        l1=input("\nEnter your guess: ")
        if(l1 in rptd):
            print("\nRepeated!")
        else:
            rptd.append(l1)
            if(len(l1)>1):
                if(word==l1):
                    print(Green+"\nCorrect! You won!")
                    print(Style.RESET_ALL)
                    flag=1
                else:
                    print(Red+"\nWrong guess")
                    print(Style.RESET_ALL)
                    wrong+=1
                    if(wrong==1):
                        w1()
                    elif(wrong==2):
                        w2()
                    elif(wrong==3):
                        w3()
                    elif(wrong==4):
                        w4()
                    elif(wrong==5):
                        w5()
                    elif(wrong==6):
                        w6()
                        print(Red+"YOU LOST!")
                        flag=1
            
            if(l1 in word and len(l1)==1):
                flag1=1
                a=word.index(l1)
                if(word.count(l1)>1):  
                    b+=1
                    for i in range(len(word)):
                        if(word[i]==l1):
                            c=i
                    
                print(Green+"Correct guess!")
                print(Style.RESET_ALL)
                print("The word is now:",end="")
                
                for i in range(len(word)):
                    if(flag1==1):
                        new[a]=l1
                        if(b>=1):
                            new[c]=l1
                    else:
                        continue
                for i in new:
                    print(i,end="")
                if(b>=1):
                    cor+=2
                else:
                    cor+=1
                if(len(word)==cor):
                    print(Green+"\nCorrect! You won!")
                    print(Style.RESET_ALL)
                    flag=1
                flag1=0
                b=0
            elif(l1 not in word and len(l1)==1):
                print(Red+"\nWrong guess")
                print(Style.RESET_ALL)
                wrong+=1
                if(wrong==1):
                    w1()
                elif(wrong==2):
                    w2()
                elif(wrong==3):
                    w3()
                elif(wrong==4):
                    w4()
                elif(wrong==5):
                    w5()
                elif(wrong==6):
                    w6()
                    print(Red+"YOU LOST!")
                    flag=1
        
main()