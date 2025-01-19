import java.util.Arrays;
import java.util.Random;

// Fun Bogosort thingy from when I was on the train

public class BogosBinted {

    // Method to check if the array is sorted
    public static boolean isSorted(int[] array) {
        for (int i = 1; i < array.length; i++) {
            if (array[i - 1] > array[i]) {
                return false;
            }
        }
        return true;
    }

    // Method to shuffle the array
    public static void shuffle(int[] array) {
        Random rand = new Random();
        for (int i = 0; i < array.length; i++) {
            int j = rand.nextInt(array.length);
            // Swap array[i] and array[j]
            int temp = array[i];
            array[i] = array[j];
            array[j] = temp;
        }
        // Print the shuffled array
        System.out.println("Shuffled Array: " + Arrays.toString(array));
    }

    // Bogosort algorithm
    public static void bogosort(int[] array) {
        while (!isSorted(array)) {
            shuffle(array);
        }
    }

    // Test cases
    public static void main(String[] args) {
        // Test case 1: Already sorted array
        int[] testArray1 = {1, 2, 3, 4, 5};
        bogosort(testArray1);
        System.out.println("Test Case 1: " + Arrays.toString(testArray1)); // Expected: [1, 2, 3, 4, 5]

        // Test case 2: Reverse sorted array
        int[] testArray2 = {5, 4, 3, 2, 1};
        bogosort(testArray2);
        System.out.println("Test Case 2: " + Arrays.toString(testArray2)); // Expected: [1, 2, 3, 4, 5]

        // Test case 3: Random array
        int[] testArray3 = {3, 1, 4, 5, 2};
        bogosort(testArray3);
        System.out.println("Test Case 3: " + Arrays.toString(testArray3)); // Expected: [1, 2, 3, 4, 5]

        // Test case 4: Single element array
        int[] testArray4 = {42};
        bogosort(testArray4);
        System.out.println("Test Case 4: " + Arrays.toString(testArray4)); // Expected: [42]

        // Test case 5: Empty array
        int[] testArray5 = {};
        bogosort(testArray5);
        System.out.println("Test Case 5: " + Arrays.toString(testArray5)); // Expected: []

        // Test case 6: Massive dataset
        int massiveSize = 10000; // Size of the massive dataset
        int[] massiveArray = new int[massiveSize];
        for (int i = 0; i < massiveSize; i++) {
            massiveArray[i] = massiveSize - i; // Reverse order
        }
        bogosort(massiveArray);
        System.out.println("Test Case 6: First 10 elements: " + Arrays.toString(Arrays.copyOf(massiveArray, 10))); // Display first 10 elements, Expected: No idea, but it'll take a while
    }
}