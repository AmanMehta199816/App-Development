import java.util.Scanner;

// Class for dental consultant
class DentalConsultant {
    private String name;
    private String specialization;

    // Constructor
    public DentalConsultant(String name, String specialization) {
        this.name = name;
        this.specialization = specialization;
    }

    // Method to display details of the consultant
    public void displayDetails() {
        System.out.println("Consultant Name: " + name);
        System.out.println("Specialization: " + specialization);
    }
}

// Class for Video Call functionality
class VideoCall {
    private DentalConsultant consultant;
    private boolean callActive;

    // Constructor
    public VideoCall(DentalConsultant consultant) {
        this.consultant = consultant;
        this.callActive = false;
    }

    // Method to start the video call
    public void startCall() {
        if (!callActive) {
            System.out.println("Video call with " + consultant.name + " started.");
            callActive = true;
        } else {
            System.out.println("A call is already in progress.");
        }
    }

    // Method to end the video call
    public void endCall() {
        if (callActive) {
            System.out.println("Video call with " + consultant.name + " ended.");
            callActive = false;
        } else {
            System.out.println("No active call to end.");
        }
    }
}

// Main class to demonstrate the app
public class DentalConsultationApp {
    public static void main(String[] args) {
        // Create a dental consultant
        DentalConsultant consultant = new DentalConsultant("Dr. John Doe", "Orthodontist");

        // Create a video call object
        VideoCall videoCall = new VideoCall(consultant);

        // Menu for user interaction
        Scanner scanner = new Scanner(System.in);
        int choice;
        do {
            System.out.println("\nDental Consultation App");
            System.out.println("1. Start Video Call");
            System.out.println("2. End Video Call");
            System.out.println("3. View Consultant Details");
            System.out.println("4. Exit");
            System.out.print("Enter your choice: ");
            choice = scanner.nextInt();
            switch (choice) {
                case 1:
                    videoCall.startCall();
                    break;
                case 2:
                    videoCall.endCall();
                    break;
                case 3:
                    consultant.displayDetails();
                    break;
                case 4:
                    System.out.println("Exiting the application.");
                    break;
                default:
                    System.out.println("Invalid choice. Please try again.");
                    break;
            }
        } while (choice != 4);

        scanner.close();
    }
}
