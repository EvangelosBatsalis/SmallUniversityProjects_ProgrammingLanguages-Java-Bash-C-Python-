import random
# random Function 
# η συνάρτηση random καλείται από την main όπου και δημιουργεί έναν τυχαίο ακέραιο αριθμό μεταξύ 1 και 100
# και ακολούθως καλεί τη συνάρτηση game όπου είναι και η κεντρική συνάρτηση του παιχνιδιού
def randomFunction():
    randomNum=random.randint(1,100)
    print("H timh rand einai: ",randomNum)
    
    game(randomNum)

#Game Funcion
#καλείται από random function και φέρει και τον τυχαίο αριθμό όπου και ξεκινάει το παιχνίδι
#Πρώτα ζητάει από τον χρήστη έναν αριθμό από το 1 έως το 100 ή τη λέξη quit για έξοδο
#έπειτα γίνεται έλεγχος αμυντικού προγραμματισμού ώστε να σιγουρέψουμε ότι ο χρήστης εισάγει τον ζητούμενο σωστό αριθμό και γίνεται και έλεγχος για το εαν ο χρήστης εισάγει τη λέξη 
#quit ωστε να τερματιστεί το πρόγραμμα
#


def game(randomFunction):
    count=0
    while True:
        num = input("Δώσε έναν αριθμό από το 1 έως το 100 διαφορετικά γράψτε quit για έξοδο: ")
        if num.upper() == "QUIT":break
        if not num.isnumeric():continue
        num = int(num)
        if not num >= 1 or not num <= 100:continue
        if num < randomFunction:
            print("Ο κρυμμένος αριθμός είναι μεγαλύτερος")
            count+=1
        if num > randomFunction:
            print("Ο κρυμμένος αριθμός είναι μικρότερος")
            count+=1
        if num == randomFunction:break
    count+=1
    score=10-count
    if count > 10: score = 0
    print("Το βρήκατε μετά από {} προσπάθειες, και κερδίσατε {} πόντους".format(count,score))

#main function
#ακολουθεί μήνυμα οδηγιών όπως και αναφέρεται στο βήμα 1 την εργασίας και ακολούθως καλέι τη συνάρτηση random
print("Καλώς ήρθατε στο παιχνίδι μάντεψε έναν αριθμό. Υπάρχουν δύο τρόποι τερματισμού από το παιχνίδι\n")
print("α) με την εύρεση του αριθμού\n")
print("β) εκούσιος τερματισμός ανα πάσα στιγμή εισάγωντας quit για έξοδο\n")
print("παρακαλώ ακολουθήστε τις κάτωθι οδηγίες. Καλή διασκέδαση!\n")

randomFunction()

#loop εξόδου
while True:
    exodos = input("θέλετε να ξαναπαίξετε (ΝΑΙ/ΟΧΙ): ")
    if exodos.upper() == "ΟΧΙ":
        print("Ευχαριστούμε, αντίο σας!")
        break
    if exodos.upper() == "ΝΑΙ":
        randomFunction()
    else:
        print("Λάθος εισαγωγή...!!\nΠαρακαλώ πληκτρολογήστε ΝΑΙ ή ΟΧΙ")
        continue


