def takeInput():
    x = int(input ("Enter 1st number: "))
    y = int(input ("Enter 2nd number: "))
    o= (input ("Enter operator: "))
   
    displayResult(x, y, o)
 
 
def displayResult(x, y, o):
    if o == "+":
        result = x+y
        print ("Answer",result)

    elif o == "-":
        result = x-y
        print ("Answer",result)

    elif o == "*":
        result = x*y
        print ("Answer",result)
        

    elif o == "/":
        result = x/y
        print ("Answer",result)
       
 
takeInput()


    

    



    