import random
restart = True
while restart:
    Computer=(random.randrange(1,7))
    #print(Computer)
    ooe=" "
    oe= ooe.lower()
    #print(oe)
    oe= ooe.lower()
    while True:
        if oe in["even" , "odd"]:
            break
        else:
            print("\nPlease enter odd or even")
            ooe=input("Odd or Even:")
            oe= ooe.lower()
    print("\nYou choose",oe)
    User_input=input("\nChoose a number from 1 to 6:")
    Ut=User_input.isdigit()
    while True:
       if Ut == True:
        Pt = float(User_input)
        if Pt in[1.0 , 2.0 ,3.0 , 4.0 , 5.0 , 6.0] :
           #print(Pt)
           break
        else:
           print("\nPlease choose a number from 1 to 6")
           User_input=input("Choose a number from 1 to 6:")
           Ut=User_input.isdigit()

       else:
           print("\nPlease choose a number from 1 to 6")
           User_input=input("Choose a number from 1 to 6:")
           Ut=User_input.isdigit()
    y=Pt + Computer
    yi=int(y)
    #print(y,yi)
    oey=yi%2
    a=" "
    #print(oey)
    if oey == 1:
       a="odd"
    else:
       a="even"
    bobc = random.choice(["bat", "ball"])
    bobu=" "
    print("\nThe computer choose",Computer,"\nSum of computer's and your number is",a)
    bobul= bobu.lower()
    if a == oe:
        print("\nYou won the toss by choosing",oe)
        bobu=input("Do you want to bat or ball:")
        bobul= bobu.lower()
        while True:
          if bobul in["bat" , "ball"]:
            print("\nYou choose to",bobul)
            break
          else:
            print("\nPlease enter bat or ball")
            bobu=input("Do you want to bat or ball:")
            bobul= bobu.lower()
    else:
        print("\nYou lost the toss by choosing",oe)
        print("\nThe computer chooses to",bobc)
        if bobc == "bat":
            bobul="ball"
        else:
            bobul="bat"
    Computer=(random.randrange(1,7))
    total=0
    Runs=0
    pt=0
    matchOver = False
    if bobul == "bat":
       while not matchOver:
           User_input=input("\nChoose a number from 1 to 6:")
           if not User_input.isdigit():
               print("Please enter a number between 1 to 6:")
               continue

           pt=int(User_input)
           if pt < 1 or pt > 6:
               print("\nPlease enter a number between 1 to 6:")
               continue

           Computer=(random.randrange(1,7))
           if Computer == pt:
               print("\nYou are out!You and the computer entered",pt,". Total score:",Runs)
               total=Runs+1
               print("\nThe target is",total,"\nYou are now bowling.")
               Runs=0
               while not matchOver:
                User_input=input("\nChoose a number from 1 to 6:")
                if not User_input.isdigit():
                 print("Please enter a number between 1 to 6:")
                 continue
                pt=int(User_input)
                if pt < 1 or pt >6:
                 print("\nPlease enter a number between 1 to 6:")
                 continue
                Computer=(random.randrange(1,7))
                if Computer == pt:
                 print("\nComputer is out!You and the computer entered",pt)
                 if Runs == total-1:
                  print("You tied!You both scored",Runs)
                 print(" You won and defended the target of :",total,".")
                 matchOver = True
                 break
                if Runs < total:
                 Runs += Computer
                 print("\nComputer scored",Computer,". Total score:",Runs)
                if Runs >= total:
                 print("\nComputer won the match by achieving the target of",total,".")
                 matchOver = True
                 break
           else:
               Runs += pt
               print("\nYou scored",pt,". Total score:",Runs)


    if bobul == "ball":
       while not matchOver:
           User_input=input("\nChoose a number from 1 to 6:")
           if not User_input.isdigit():
               print("Please enter a number between 1 to 6:")
               continue

           pt=int(User_input)
           if pt < 1 or pt > 6:
               print("\nPlease enter a number between 1 to 6:")
               continue

           Computer=(random.randrange(1,7))
           if Computer == pt:
               print("\nComputer is out!You and the computer entered",pt,". Total score:",Runs)
               total=Runs+1
               print("\nThe target is",total,"\nYou are now batting.")
               Runs=0
               while not matchOver:
                User_input=input("\nChoose a number from 1 to 6:")
                if not User_input.isdigit():
                 print("Please enter a number between 1 to 6:")
                 continue
                pt=int(User_input)
                if pt < 1 or pt >6:
                 print("\nPlease enter a number between 1 to 6:")
                 continue
                Computer=(random.randrange(1,7))
                if Computer == pt:
                 print("\nYou are out!You and the computer entered",pt)
                 if Runs == total-1:
                  print("You tied!You both scored",Runs)
                 print(" Computer won and defended the target of :",total,".")
                 matchOver = True
                 break
                if Runs < total:
                 Runs += pt
                 print("\nYou scored",pt,". Total score:",Runs)
                if Runs >= total:
                 print("\nYou won the match by achieving the target of",total,".")
                 matchOver = True
                 break
           else:
               Runs += Computer
               print("\nComputer scored",Computer,". Total score:",Runs)
    re=input('DO YOU WANT TO PLAY AGAIN(YES OR NO):')
    rei=re.lower()
    while True:
     if rei in["yes" , "no"]:
        if rei == "yes":
           restart = True
        else :
           restart = False
        break
     else:
        print("Please enter yes or no")
        re=input('DO YOU WANT TO PLAY AGAIN(YES OR NO):')
        rei=re.lower()




