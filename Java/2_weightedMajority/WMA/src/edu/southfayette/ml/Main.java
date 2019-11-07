package edu.southfayette.ml;

import java.util.Scanner;


public class Main {

    public static void main(String[] args) {
        System.out.println("How many people are in your group? ");
        Scanner sc = new Scanner(System.in);
        int people = Integer.parseInt(sc.next());

        System.out.println("You entered " + people);

        double penalty = 0.5;
       
        Expert[] experts = new Expert[people];

        ////////////////////////////////////////////////////////////////////////////
        // Challenge 0: Change the movieInputs list below to contain up to 10 movies that you
        // and your friends all know.
        ///////////////////////////////////////////////////////////////////////////////////
        String[] oldMovies = {"Zootopia",
                "Big Hero 6",
                "Catching Fire",
                "Star Wars: The Phantom Menace",
                "Harry Potter and the Deathly Hallows"};

        int len = oldMovies.length;

//run this with the size as a variable.
        for (int i = 0; i < len; i++) {
            int like = 0;
            int dislike = 0;
            int verdict;
            int[] choices = new int[people];

            for (int j = 0; j < people; j++) {


                System.out.println("Did you person, " + j + ", enjoy " + oldMovies[i] + " ? ");
                System.out.println("Answer y/n: ");
                Scanner word = new Scanner(System.in);
                String next = word.next();
                System.out.println("You entered " + next);
                
                ///////////////////////////////////////////////////////////////////////////
                // Challenge 1: The first step is to use the expert labels and weights to
                // determine which label to predict (True or False).
                //////////////////////////////////////////////////////////////////////////
                
                // Write your code here!
                
                // These lines contain variables that haven't been initialized.
                // You might want to initialize them to elsewhere in the program.
                
                
                

            }

            if (like > dislike) {
                verdict = 1;
            } else {
                verdict = 0;
            }
            
            ////////////////////////////////////////////////////////////////////////////
            // Challenge 2: Use the actualLabel variable (which represents whether or not
            //you liked the movie), the next step is to adjust the expert weights based
            // on whether or not their label was accurate.
            ///////////////////////////////////////////////////////////////////////////
            
            // Write your code here!


        }

    }
}
