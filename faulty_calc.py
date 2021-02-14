# faulty result for following calculation
""" 54 * 56 = 555
 38 + 65 = 99
 31/14 = 31"""

vartemp = "Want to proceed with calculation"
print(vartemp)
varin = input("Answer with Y or N")
while (varin =="Y"):
    if  varin == "Y" :
        var1 = int(input("Enter your first number:"))

        var2 = int(input("Enter your second number:"))
        var3 = input("Enter the functions:")

        if var3 == "*":
            if var1 not in (54, 56) and var2 not in (54, 56):
                var4 = var1 * var2
                print(var4)
            else:
                print("555")
        elif var3 == "+":
            if var1 not in (38, 65) and var2 not in (38, 65):
                var4 = var1 + var2
                print(var4)
            else:
                print("99")
        elif var3 == "/":
            if var1 not in (31, 14) and var2 not in (31, 14):
                var4 = var1 / var2
                print(var4)
            else:
                print("31")
        else:
            print("Cannot Calculate the number")

        vartemp = "Want to proceed with calculation"
        print(vartemp)
        varin = input("Answer with Y or N")

ending = print("Thanks for coming.")
print(ending)