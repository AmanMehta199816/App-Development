import java.util.Scanner;

public class CovidTracker {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Prompt user to enter health status
        System.out.println("Welcome to COVID-19 Tracker App");
        System.out.println("Please enter your health status (Positive, Negative, Suspected):");
        String healthStatus = scanner.nextLine().trim().toLowerCase();

        // Check user's health status and display appropriate message
        switch (healthStatus) {
            case "positive":
                System.out.println("Please seek medical attention and self-isolate immediately.");
                break;
            case "negative":
                System.out.println("Stay vigilant and continue to follow safety guidelines.");
                break;
            case "suspected":
                System.out.println("Monitor your symptoms and consider getting tested.");
                break;
            default:
                System.out.println("Invalid input. Please enter either 'Positive', 'Negative', or 'Suspected'.");
                break;
        }

        scanner.close();
    }
}
