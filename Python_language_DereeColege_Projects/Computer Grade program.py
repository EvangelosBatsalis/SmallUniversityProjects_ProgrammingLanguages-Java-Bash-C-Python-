print("Welcome to Computer Grade program")

#efoson kai eksasfalisei thn eisodo toy xrhsth na einai akeraios arithmos ginetei elegxow me if gia to ean oo xrhsths exei balei eisodo metaksu 0 kai 100 diaforetika bgazei sfalma eksodoy
def computergrade(user_input):
    if ((user_input >=0) and (user_input <=100)):
        if ((user_input >=70) and (user_input <=100)):
            print("A")
        elif ((user_input >=65) and (user_input <=69)):
            print("A-")
        elif ((user_input >=60) and (user_input <=64)):
            print("B+")
        elif ((user_input >=50) and (user_input <=59)):
            print("B")
        elif ((user_input >=45) and (user_input <=49)):
            print("C+")
        elif ((user_input >=40) and (user_input <=44)):
            print("C")
        elif ((user_input >=0) and (user_input <=39)):
            print("F")
        
    else:
        print("Not in range value, Please Enter value beetween 0 and 100")
    return user_input




# ginetai loopa while monimis true me eksodo to break kai elegxei gia to ean o xrhsths exei balei arithmo h ton sundismo plhktron to OK, ok, Ok, oK anti giana kanw 4 syndiasmous xrhsimopoihsa thn synarthsh string .lower()
while True:
    user_input = input("Please enter computer grade 0 to 100 or press OK to quit: ")
    if user_input.lower()== "ok":
        print("\nThank you for using computer grade program")
        break;
    else:
        try:
            user_input=int(user_input)
            computergrade(user_input)
        except ValueError:
            print("\nIncorrect input. Please enter 0 to 100 for computer grade or OK to quit")

