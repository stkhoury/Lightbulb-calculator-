def lightbulb_calculator():

    
    print ("INSTRUCTIONS:")
    print ("The following program will add 2 digits together for you.")
    print ("If the total is even, there will be a picture of a lighted bulb")
    print ("If the total is odd, there will be a picture of an unlit bulb")


    greeting = str(input("Hello, what is your name?"))
    print("Hello," + str(greeting))
      
    print("Enter digit 1 and enter digit 2 to add the numbers together")
    
    a = float(input("Enter digit #1:"))
    b = float(input("Enter digit #2:"))
    sum = a+b

    print ("The sum  of " + str("a" ) + " and " + str("b") + " is "+ str(sum))
    print ("The picture will pop up shortly")

    if sum % 2 == 0:   #even equation 
        import webbrowser 
        webbrowser.open ("file:///Users/s/Desktop/Lightbulb.jpeg")
        #enter the file name for your personal image on your computer here
    else:
        import webbrowser
        webbrowser.open ("file:///Users/s/Desktop/lightbulb%20turned%20off.jpg")
        #enter the file name for your personal image on your computer here

    print ("Thank you so much for running this program. I hope you enjoy it")
    
lightbulb_calculator()
