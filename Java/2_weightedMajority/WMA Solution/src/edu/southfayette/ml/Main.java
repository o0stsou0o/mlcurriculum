package edu.southfayette.ml;

import java.util.Scanner;
//ask quick question about comparators with the == stuff.

public class Main {

    public static void main(String[] args) {
        System.out.println("How many people are in your group? ");
        Scanner sc = new Scanner(System.in);
        int people = Integer.parseInt(sc.next());

        System.out.println("You entered " + people);



        double penalty = 0.5;
        //System.out.println("First Point");

        Expert[] experts = new Expert[people];


        //System.out.println("Second Point");



        //System.out.println("Please enter 5 movie names: ")

        //for (int i = 0; i < ; i++) {


        //}


        String[] oldMovies = {"Zootopia",
                "Big Hero 6",
                "Catching Fire",
                "Star Wars: The Phantom Menace",
                "Harry Potter and the Deathly Hallows"};


        //question about casting this sc.next into an int


        for (int i = 0; i < 5; i++) {  //looping through the movie first
            int like = 0;
            int dislike = 0;
            int verdict;
            int[] choices = new int[people]; //arrays of people

            for (int j = 0; j < people; j++) {  //looping through the experts


                //String critic = critic + i;

                System.out.println("Did you person, " + j + ", enjoy " + oldMovies[i] + " ? ");
                System.out.println("Answer y/n: ");
                Scanner word = new Scanner(System.in);
                String next = word.next();
                System.out.println("You entered " + next);
                if (next.equals("y")) {
                    System.out.println("Got Here ");

                    like += 1;
                    choices[j] = 1;
                } else if (next.equals("n")) {
                    System.out.println("Jiggles ");

                    dislike += 1;
                    choices[j] = 0;
                }
                System.out.println("Got Here ");


            }


            if (like > dislike) {
                verdict = 1;
            } else {
                verdict = 0;
            }

            for (int j = 0; j < people; j++) {
                if (choices[j] != verdict) {
                    experts[j].weight = experts[j].weight * penalty;
                }


            }



        }

    }
}
