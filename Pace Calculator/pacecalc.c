#include <stdio.h>

void calculatePace(double distance, int hours, int minutes, int seconds, int paceUnit) {
    int totalSeconds = hours * 3600 + minutes * 60 + seconds;
    double pace = totalSeconds / distance;
    int paceMinutes = (int)pace / 60;
    int paceSeconds = (int)pace % 60;

    if (paceUnit == 1) {
        printf("You need to run at an average pace of %d minutes and %d seconds per kilometer.\n", paceMinutes, paceSeconds);
    } else {
        printf("You need to run at an average pace of %d minutes and %d seconds per mile.\n", paceMinutes, paceSeconds);
    }
}

int main() {
    int choice;
    int unitChoice;
    int paceUnit;
    double distance;
    int hours, minutes, seconds;
    char anotherCalculation;

    printf("Select the distance you want to run:\n");
    printf("1. 100 meters\n");
    printf("2. 200 meters\n");
    printf("3. 400 meters\n");
    printf("4. 600 meters\n");
    printf("5. 800 meters\n");
    printf("6. 1 kilometer\n");
    printf("7. 1600 meters\n");
    printf("8. 1 mile\n");
    printf("9. 3 kilometers\n");
    printf("10. 5 kilometers\n");
    printf("11. 8 kilometers\n");
    printf("12. 10 kilometers\n");
    printf("13. Half Marathon (21.0975 kilometers)\n");
    printf("14. Marathon (42.195 kilometers)\n");
    printf("15. Custom distance\n");
    printf("Enter your choice: ");
    scanf("%d", &choice);

    switch (choice) {
        case 1:
            distance = 0.1; // 100 meters in kilometers
            break;
        case 2:
            distance = 0.2; // 200 meters in kilometers
            break;
        case 3:
            distance = 0.4; // 400 meters in kilometers
            break;
        case 4:
            distance = 0.6; // 600 meters in kilometers
            break;
        case 5:
            distance = 0.8; // 800 meters in kilometers
            break;
        case 6:
            distance = 1.0; // 1 kilometer
            break;
        case 7:
            distance = 1.6; // 1600 meters in kilometers
            break;
        case 8:
            distance = 1.609; // 1 mile in kilometers
            break;
        case 9:
            distance = 3.0; // 3 kilometers
            break;
        case 10:
            distance = 5.0; // 5 kilometers
            break;
        case 11:
            distance = 8.0; // 8 kilometers
            break;
        case 12:
            distance = 10.0; // 10 kilometers
            break;
        case 13:
            distance = 21.0975; // Half Marathon
            break;
        case 14:
            distance = 42.195; // Marathon
            break;
        case 15:
            printf("Enter the custom distance: ");
            scanf("%lf", &distance);
            do {
                printf("Select the unit of measurement for the custom distance:\n");
                printf("1. Kilometers\n");
                printf("2. Miles\n");
                printf("Enter your choice: ");
                if (scanf("%d", &unitChoice) != 1) {
                    printf("Invalid choice. Please enter 1 for Kilometers or 2 for Miles.\n");
                    while (getchar() != '\n'); // Clear the input buffer
                    unitChoice = 0; // Reset unitChoice to ensure the loop continues
                } else if (unitChoice == 2) {
                    distance *= 1.60934; // Convert miles to kilometers
                } else if (unitChoice != 1) {
                    printf("Invalid choice. Please enter 1 for Kilometers or 2 for Miles.\n");
                }
            } while (unitChoice != 1 && unitChoice != 2); // else if unitChoice is not 1 or 2, say it's an invalid choice and ask again
            break;
        default:
            printf("Invalid choice.\n");
            return 1;
    }

    do {
        printf("Select the unit for pace calculation:\n");
        printf("1. Kilometers\n");
        printf("2. Miles\n");
        printf("Enter your choice: ");
        if (scanf("%d", &paceUnit) != 1) {
            printf("Invalid choice. Please enter 1 for Kilometers or 2 for Miles.\n");
            while (getchar() != '\n'); // Clear the input buffer
            paceUnit = 0; // Reset paceUnit to ensure the loop continues
        } else if (paceUnit != 1 && paceUnit != 2) {
            printf("Invalid choice. Please enter 1 for Kilometers or 2 for Miles.\n");
        }
    } while (paceUnit != 1 && paceUnit != 2); // else if unitChoice is not 1 or 2, say it's an invalid choice and ask again

    do {
        printf("Enter your goal time (hours:minutes:seconds) - ");
        int result = scanf("%d:%d:%d", &hours, &minutes, &seconds);
        if (result != 3 || hours < 0 || minutes < 0 || minutes >= 60 || seconds < 0 || seconds >= 60) {
            printf("Invalid time entered. Please enter valid values for hours, minutes, and seconds.\n");
            while (getchar() != '\n'); // Clear the input buffer
        }
    } while (hours < 0 || minutes < 0 || minutes >= 60 || seconds < 0 || seconds >= 60);

    if (paceUnit == 2) {
        distance /= 1.60934; // Convert distance to miles for pace calculation
    }

    calculatePace(distance, hours, minutes, seconds, paceUnit);

    printf("Would you like to perform another calculation? (y/n): ");
    scanf(" %c", &anotherCalculation);
    if (anotherCalculation == 'y' || anotherCalculation == 'Y') {
        main(); // Restart the program
    } else if (anotherCalculation == 'n' || anotherCalculation == 'N') {
        printf("Thank you for using the pace calculator!\n");
    } else {
        printf("Invalid input. Exiting the program.\n");
    }

    return 0;
}