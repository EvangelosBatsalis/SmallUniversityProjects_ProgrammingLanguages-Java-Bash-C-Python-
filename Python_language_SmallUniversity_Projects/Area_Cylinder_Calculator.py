print ("Welcome to area calculator this program calculates shapes of:")
print ("1. Cylinder")
print ("2. Pyramid")
print ("3. Box")

def Cylinder(R,H): #methodos embadon kilindrou brethike apo typo toy internet
    PI = 3.14
    CALC =2 * PI * R * (H + R)
    return CALC #epistrofh apotelesmatos ston arxiko mas programma

def Pyramid(L,H):
    CALC = 1 / 2 * BL * H * 4
    return CALC

def Box(BL,BW,H):
    CALC = (2*BL*BW) + (2*BL*H) + (2*BW*H)
    return CALC

#arxikopoihsh metablhths gia xrish pros ton elegxo ths eisodou toy xrhsth
CHOICE = 0;

while CHOICE > 3 or CHOICE <= 0:
    #i used try and except for exception handling to check user input for not using anything rather than interger 
    try:
        CHOICE = int(input("Please make enter a choice between 1 and 3: "))
    except ValueError:
        print("Please Characters are now allowed!!")
    
else:
    #diaforetika kanei elegxo ths eisodou toy xrhsth an einai h epilogh 1
    if CHOICE == 1:
        
        print("\nYou have choose the Cylinder area calculator") 
        #zhtaeu 2 eisagwges toy xrhsth radius kai height xrhsimopoihsa float gia eisodo me dekadika psifia
        R = float(input("Please enter Radius: "))
        H = float(input("Please enter Height: "))
        #stelnei sthn method Cylinder tis dyo eisagwges toy xrhsth
        CALC = float(Cylinder(R,H))

    elif CHOICE == 2:
        print("\nYou have choose the Pyramid area calculator")
        BL = float(input("Please enter base length: "))
        H = float(input("Please enter Height: "))
        CALC =float(Pyramid(BL,H))

    elif CHOICE == 3:
        print("\nYou have choose the Box area calculator")
        BL = float(input("please enter Box Length: "))
        BW = float(input("please enter Box Width: "))
        H = float(input("please enter Height: "))
        CALC = float(Box(BL,BW,H))  

#i used if option for more readable option of export
if CHOICE == 1:
    print("The area or Cylinder is: ",CALC)

elif CHOICE == 2:
    print("The area or Pyramid is: ",CALC)
elif CHOICE == 3:
    print("The area or Box is: ",CALC)
