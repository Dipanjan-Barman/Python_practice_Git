num = input("Please enter a number: ") # inputs are always string

numint = int(float(num))

if numint != float(num):
    print(num + " is a fraction")
else:
    if  (numint % 4) == 0:
         print(num + " is an even number and mulptiple of 4 ")
    elif (numint % 2) == 0:
        print(num + " is an even number ")
    else:
        print(num + " is an odd number ")
