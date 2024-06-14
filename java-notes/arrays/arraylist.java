package notes.arrays;
import java.util.List;
import java.util.ArrayList;

public class arraylist {
    public static void main(String[] args) {
        // Polymorphic initialization of List as ArrayList
        List<String> myList = new ArrayList<>();

        // Adding elements to the list
        myList.add("Apple");
        myList.add("Banana");
        myList.add("Orange");

        // Accessing elements using index
        String firstElement = myList.get(0);
        System.out.println("First element: " + firstElement);

        // Checking if the list contains an element
        boolean containsBanana = myList.contains("Banana");
        System.out.println("Contains 'Banana': " + containsBanana);

        // Removing an element by value
        boolean removed = myList.remove("Orange");
        System.out.println("Element 'Orange' removed: " + removed);

        // Getting the size of the list
        int size = myList.size();
        System.out.println("Size of the list: " + size);

        // Iterating over the elements in the list
        System.out.println("List elements:");
        for (String element : myList) {
            System.out.println(element);
        }

        // Clearing the list
        myList.clear();
        System.out.println("List cleared. New size: " + myList.size());
    }

    /*
        In this example, we import the List and ArrayList classes from the java.util package. 
        The List interface is the type declaration, while the ArrayList class is used for the actual object instantiation.

        We initialize the myList object as an ArrayList using polymorphism. 
        This means we can treat the myList object as a List (interface) type, allowing us to switch implementations without affecting the rest of the code.

        We then demonstrate various methods available in the List interface:

        * add() method is used to add elements to the list.
        * get() method retrieves an element at a specific index.
        * contains() method checks if the list contains a specific element.
        * remove() method removes an element from the list.
        * size() method returns the number of elements in the list.
        * Iteration over the list is done using a for-each loop.
        * clear() method empties the list.
        * By using polymorphism and programming to the List interface, we can switch the implementation to other classes that implement the List interface (such as LinkedList or Vector) without changing the rest of the code.
     
        */


}
