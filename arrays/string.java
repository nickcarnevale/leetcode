package arrays;
import java.lang.StringBuilder;

public class string {
    
    public static void main(String[] args){
        String str = "Hello, World!";

        // String length
        int length = str.length(); // 13

        // Concatenating strings
        String greeting = "Hello";
        String name = "John";
        String message = greeting + ", " + name + "!";

        // Substring extraction
        String substr = str.substring(7, 12); // "World"

        // String comparison
        boolean isEqual = str.equals("Hello"); // false

        // String searching
        int index = str.indexOf("World");
        if (index != -1) {
            System.out.println("Substring found at index: " + index);
        } else {
            System.out.println("Substring not found.");
        }

    }

    String deleteAndShiftStringCharacter(String str, int index) {
        // Create a StringBuilder from the input string
        StringBuilder sb = new StringBuilder(str);
    
        // Check if the index is valid
        if (index < 0 || index >= sb.length()) {
            throw new IllegalArgumentException("Invalid index!");
        }
    
        // Delete the character at the specified index
        sb.deleteCharAt(index);
    
        // Return the modified string
        return sb.toString();
    }

    /*
        USEFUL StringBuilder methods
    
        * append(String str) - Appends the specified string to the end of the StringBuilder.
        * insert(int offset, String str) - Inserts the specified string at the specified position.
        * delete(int start, int end) - Removes the characters between the specified start and end positions.
        * deleteCharAt(int index) - Removes the character at the specified index.
        * replace(int start, int end, String str) - Replaces the characters between the specified start and end positions with the specified string.
        * reverse() - Reverses the characters in the StringBuilder.
        * toString() - Converts the StringBuilder to a string.

     */
    

}
