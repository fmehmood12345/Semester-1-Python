import java.util.Scanner;

public class ReportingIO {
    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);
        boolean continueRunning = true;

        do {
            int menuChoice = menu();
            switch (menuChoice) {
                case (1):
                    System.out.println("Choose from the options: \n" +
                            "1. Add Auction House Data \n" +
                            "2. Back to main menu \n");
                    int case1Options = keyboard.nextInt();

                    switch (case1Options) {
                        case (1):
                            System.out.println();
                        case (2):
                            //menu();
                    }//end case 1 switch
                    break;

                case (2):
                    System.out.println("Choose from the options: \n" +
                            "1. Add Item Data \n" +
                            "2. Back to main menu \n");
                    int case2Options = keyboard.nextInt();

                    switch (case2Options) {
                        case (1):
                            System.out.println();
                        case (2):
                            //menu();
                    }//end case 2 switch
                    break;
                case (3):
                    System.out.println(("Choose one of the following options:\n" +
                            "1. Auction House with the largest price in a given year\n" +
                            "2. Highest price ever reported\n" +
                            "3. Items sold with a price greater than a given price\n" +
                            "4. Back to main menu"));
                    int case3Options = keyboard.nextInt();

                    switch (case3Options) {
                        case (1):
                            System.out.println();
                        case (2):
                            System.out.println();
                        case (3):
                            System.out.println();
                        case (4):
                            //menu();
                            System.out.println();
                    }//end case 3 switch
                    break;

                case (4):
                    System.out.println("You are exiting main menu! Bye!");
                    System.exit(0);

            }//end menu switch
        }//end do
        while(continueRunning);

    }//end main
    public static int menu() {
        Scanner keyboard = new Scanner(System.in);
        System.out.println("Choose one of the following options:\n" +
                "1. Enter Auction House Data \n" +
                "2. Enter Item Data \n" +
                "3. Reporting  \n" +
                "4. Exit");
        int options = keyboard.nextInt();
        return options;
    }//end menu
}//end class