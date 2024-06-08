import java.util.Queue;
import java.util.Stack;

import org.w3c.dom.Node;

class node {
    node left;
    node right;
}

public class search {
    
    Queue<Node> q = new Queue<Node>();
    Stack<Node> s = new Stack<Node>();


    

    // BFS RECURSIVE
    Node function(node n){

        queue q.insert node n
    
    
    }
    recur(queue q){

        print(n); 
        
        if(n.left != null)
            q.insert(n.left) 
        if(n.right != null)
            q.insert(n.right)
        
        //check if empty
        return function(q.pop()); 
    }


    //BFS ITERIVE
    Node function(node n1){


        n = n1
        while(true){
            
            print(n); 
        if(n.left != null)
           q.insert(n.left)
        
        if(n.right != null)
           q.insert(n.right)
        
            if(q.isEmpty())
                break;
            n = q.pop()
        }
    }

    //DFS RECRUSIVE
    Node function(node n){

        print(n); 
        
        if(n.left != null)
            function(n.left)
        if(n.right != null)
            function(n.right)
        
    
    
    }


    //DFS ITERIVE
    Node function(node n1){
        
        boolean x = true; 
        n = n1
        while(x){
            
            print(n); 
        
        if(n.right != null)
           s.insert(n.right)
        
           if(n.left != null)
           s.insert(n.left)
        
            if(q.isEmpty())
                break;
            n = q.pop()
        }
    }

}

