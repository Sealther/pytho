# hidden Number
num=20
# No. of Chances = 9
n=1
strt="Welcome Player\nYou have 9 Chances to guess the Number between 1-100"
print(strt)
# var1=input("Are you ready?\nReply with Y or N: ")
while (n<10):
    var1 = int(input("Enter the number: "))
    if var1 > num and (var1-num)<=5 and n<9:
       var2 = "You are close. Decrease your number by smaller number"
       print(var2)
    elif var1 > num and (var1-num)>5 and n<9:
       var2 = "Decrease your number by higher number"
       print(var2)
    elif var1<num  and (num-var1)<=5 and n<9:
       var2 = "You are close.Increase your number by smaller number"
       print(var2)
    elif var1<num  and (num-var1)>5 and n<9:
       var2 = "Increase your number by higher number"
       print(var2)
    elif var1==num :
       var2 = "Congrats you got the number!!"
       print(var2,"\nYou got the number in",n," chances")
       break
    else :
        var2 = "You have exhausted all your chances.\nBetter luck next time."
        print(var2)
    n= n+1




