import java.io.BufferedReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;
import java.io.FileReader;

public class MainClass {

    static ArrayList<Integer> CSVReader(int userChoice, String userMonthChoice) {//method which reads the data from file into an array using splitting method.

        String fileName = "data.csv";
        String line;
        String[] splitedOutput;
        ArrayList<Integer> finalArrayOutput = new ArrayList<>();

        try (BufferedReader br = new BufferedReader(new FileReader(fileName))) { //buffer reader and file reader
            line = br.readLine();
            if (userChoice == 1) { // simple message output
                System.out.println("Month Expenses: ");
            }

            while ((line = br.readLine()) != null) {
                splitedOutput = line.split(",");
                if (userChoice == 1) { //first choice of my program which prints the csv using | as delimiter
                    System.out.println("January: " + splitedOutput[0] + " Euro" + " | " + "February: " + splitedOutput[1] + " Euro" + " | " + "March: " + splitedOutput[2] + " Euro" + " | " + "April: " + splitedOutput[3] + " Euro" + " | " + "May: " + splitedOutput[4] + " Euro" + " | " + "June: " + splitedOutput[5] + " Euro");
                } else {
                    switch (userMonthChoice) {
                        case "january":
                            finalArrayOutput.add(Integer.parseInt(splitedOutput[0]));
                            break;
                        case "february":
                            finalArrayOutput.add(Integer.parseInt(splitedOutput[1]));
                            break;
                        case "march":
                            finalArrayOutput.add(Integer.parseInt(splitedOutput[2]));
                            break;
                        case "april":
                            finalArrayOutput.add(Integer.parseInt(splitedOutput[3]));
                            break;
                        case "may":
                            finalArrayOutput.add(Integer.parseInt(splitedOutput[4]));
                            break;
                        case "june":
                            finalArrayOutput.add(Integer.parseInt(splitedOutput[5]));
                            break;
                    }


                }


            }
        } catch (Exception e) {
            System.out.println("Error"+e);
        }

        return finalArrayOutput; //returns ArrayList
    }

    static ArrayList<Integer> MonthSearching(int userChoice) {
        Scanner in = new Scanner(System.in);
        System.out.println("Please select a month from January to June");
        String userMonthChoice = in.next();
        userMonthChoice = userMonthChoice.toLowerCase();
        ArrayList<Integer> returnstatement = new ArrayList<>();

        switch (userMonthChoice) {
            case "january":
            case "february":
            case "march":
            case "April":
            case "May":
            case "June":
                returnstatement = CSVReader(userChoice, userMonthChoice);
                break;
            default:
                System.out.println("Error. Incorrect month input. Please re-enter: ");
        }
        return returnstatement;
    }

    static void monthSelectedSorted(ArrayList<Integer> returnStatement) { //monthSelectedSorted this method it sorts using collections.sort to ascending order
        Collections.sort(returnStatement);
        System.out.println("Sorted expense output is: " + returnStatement);
    }

    static ArrayList<Integer> monthSelectionSummarized(ArrayList<Integer> returnStatement) { //monthSelectedSorted this method it sorts using collections.sort to ascending order

        int count = 0;
        int sum = 0;
        int average = 0;

        for (int i : returnStatement) {
            sum = sum + i;
            count++;
        }
        average = sum / count;

        System.out.println("Summarized expenses for the selected month is: " + sum + " Euro");
        System.out.println("count Expenses of the selected month are: " + count);
        System.out.println("The Average of the expenses are: " + average + " Euro");
        return returnStatement;
    }

    static void monthSelectedSearchData(ArrayList<Integer> returnStatement){
        Scanner in = new Scanner(System.in);
        System.out.println("please enter data to search: ");

        int UserImportedNumber = in.nextInt();
        boolean answer = returnStatement.contains(UserImportedNumber);

        if(answer){
            System.out.println("The expense contains in my month's list");
        }else{
            System.out.println("The expense does not contains in my month's list");
        }

    } //monthSelectedSorted this method it sorts using collections.sort to ascending order

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        System.out.println("Welcome to my expense calculation program");
        System.out.println("please select: ");
        System.out.println("1. CSV Print output: "); //display all data
        System.out.println("2. CSV sorted month selection output: ");//select month and display the expenses sorted in ascending order
        System.out.println("3. CSV month selection and search data: ");//search month and display the data of that month. Search for value if in that month exists
        System.out.println("4. CSV month selection and display summarized data statistics: ");//select month and display summarized, average and total count.
        System.out.println("5. To exit my program");//program exit
        System.out.println("Enter value from menu 1 to 5: \n");

        int userChoice; //arxikopoihsh metablhths epiloghs toy xrhsth

        userChoice = in.nextInt();
        ArrayList<Integer> returnStatement = new ArrayList<>();

        while (userChoice > 5 || userChoice < 0) {
            System.out.println("Invalid user input");
            System.out.println("Please make a choice from menu 1 to menu 4: ");
            userChoice = in.nextInt();
        }

        switch (userChoice) {
            case 1:
                CSVReader(userChoice, null);
                break;
            case 2:
                returnStatement = MonthSearching(userChoice);
                monthSelectedSorted(returnStatement);
                break;
            case 3:
                returnStatement = MonthSearching(userChoice);
                monthSelectedSearchData(returnStatement);
                break;
            case 4:
                returnStatement = MonthSearching(userChoice);
                monthSelectionSummarized(returnStatement);
                break;
            case 5:
                System.out.println("Thank you for using my program");
        }


    }

}
