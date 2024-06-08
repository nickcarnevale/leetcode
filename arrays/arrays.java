package arrays;
import java.util.Arrays;

class arrays{

    public static void main(String[] args){
        // Array initialization
        int[] numbers = { 5, 2, 8, 1, 9 };

        // Accessing array elements
        int firstElement = numbers[0];

        // Modifying array elements
        numbers[1] = 10;

        // Array length
        int length = numbers.length;

        // Array traversal
        for (int i = 0; i < numbers.length; i++) {
            System.out.println(numbers[i]);
        }

        // Sorting an array (using Arrays.sort)
        Arrays.sort(numbers);

        // Arrays.binarySearch(int[] arr, k key)
        int index = Arrays.binarySearch(numbers, 8);
        if (index >= 0) {
            System.out.println("Element found at index: " + index);
        } else {
            System.out.println("Element not found.");
        }
    }

    static void deleteAndShiftArrayElement(int[] arr, int index) {
        int n = arr.length; 
    
        // Check if the index is valid
        if (index < 0 || index >= n) {
            throw new IllegalArgumentException("Invalid index!");
        }
    
        // Shift the elements after the deleted element
        for (int i = index; i < n - 1; i++) {
            arr[i] = arr[i + 1];
        }
    
        // Reduce the length of the array by 1
        arr[n - 1] = 0; // Optional: Set the last element to a default value
    }
        
    /*
        USEFUL java.util.Arrays Methods

        * sort(T[] arr) - Sorts the elements of the array in ascending order. It uses the natural ordering of the elements or the custom ordering defined by the element's Comparable implementation.
        * binarySearch(T[] arr, T key) - Searches for the specified element in the sorted array using binary search. Returns the index of the element if found, or a negative value if not found.
        * copyOf(T[] original, int newLength) - Copies the specified array, truncating or padding with default values to obtain the specified length.
        * fill(T[] arr, T value) - Assigns the specified value to every element in the array.
        * equals(T[] arr1, T[] arr2) - Checks if two arrays are equal, i.e., if they have the same length and corresponding elements are equal.
        * asList(T... arr) - Returns a fixed-size list backed by the specified array.
        * toString(T[] arr) - Returns a string representation of the array.

     */

}