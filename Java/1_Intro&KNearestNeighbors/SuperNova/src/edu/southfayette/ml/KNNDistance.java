package edu.southfayette.ml;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.*;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.io.File;
import java.util.logging.Level;
import java.util.logging.Logger;


import java.util.Comparator;
import java.util.Collections;

//////////////////////////////////////////////////////////////////////////////////
// Supernova
//
// Note: this week's coding activity is less structured than we've seen in the past.
// This time, we want you to translate the pseudocode you wrote to code with
// less help than before. It might be more challenging than before, so make sure you
// have good pseudocode!
//
// We have data on about 500 stars in the universe. We have the age at which
// they died in millions of years, and the temperature at which they died in
// millions of degrees. The other most important data point is whether or not
// that star supernova'd or not upon death.
//
// One at a time you are going to go through your test set to see whether you can
// correctly predict whether a star will supernova or not based on stars closest
// to it with the training set given, following the KNN algorithm. From
// the main function we will return how accurate our test set is at predicting
// whether a star will supernova or not given said information about the star.
//
///////////////////////////////////////////////////////////////////////////////////


public class KNNDistance {

    public static void main(String[] args) throws Exception
    {

        ReadFile r = new ReadFile();
        r.openFile();

        List<TestPoint> data = r.readFile();


        r.closeFile();

        int divider = data.size()/2;
        List<TestPoint> trainingData = data.subList(0, divider);
        List<TestPoint> testData = data.subList(divider, data.size());
        
////////////////////////////////////////////////////////
//  Challenge 0: Print out the testData and the trainingData.
//  Notice how the data is set up:
// [[ageOfStarAtDeath, tempOfStarAtDeath, superNova?].....]
//
//////////////////////////////////////////////////////////
        
        

        System.out.println(knnMain(trainingData, testData, 3));



    }
    
    ////////////////////////  KNN  //////////////////////////////


// Helper function to return the euclidean distance of the points on a 2-D grid.
    public static double distance (double x0, double y0, double x1, double y1){
        double dx = x1 - x0;
        double dy = y1 - y0;
        
        double temp = Math.pow(dx,2) + Math.pow(dy,2);
        
        
        return Math.sqrt(temp);

     
    }
    

    
    ////////////////////////////////////////////////////////////////////////
    // Challenge 1: The first step is to complete the function getNeighbors.
    // We are going to calculate the distance between the current test instance
    // and every point in the training instance, put them in a list, then sort them.
    // Then we will pick the top k elements from the list.
    /////////////////////////////////////////////////////////////////////////
    
    
    // Returns the K closest neighbors to |testInstance|, in order of distance
    // from the test instance.

    public static List<TestPoint> getNeighbors (List<TestPoint> trainingSet, TestPoint testInstance, int k){
        
        int size = trainingSet.size();
        
        Distances [] distanceArray = new Distances[size];
        
        //////////////////////////////////////////////////////////////////
        // Challenge 1.1: Fill the |distanceArray| array. Hint: use the distance
        // function from above.
        // YOUR CODE HERE:
        
        
        //////////////////////////////////////////////////////////////////
        
        
        
        // sorts the distanceArray array by distance //
        int len = distanceArray.length;
        
        for (int i = 0; i < len ; i++) {
            int minIndex = i;
            for (int j = i+1; j < len; j++) {
                if (distanceArray[j].dist < distanceArray[minIndex].dist)
                {
                    minIndex = j;
                }
            }
            
            Distances temp = distanceArray[i];
            distanceArray[i] = distanceArray[minIndex];
            distanceArray[minIndex] = temp;
        }

        
        
        List<TestPoint> neighbors = new ArrayList<TestPoint>();
      
        ///////////////////////////////////////////////////////////////////////
        // Challenge 1.2: Add the correct values to the |neighbors| list so that
        // we return the correct list. What should this function return?
        // YOUR CODE HERE:
        
        
        ///////////////////////////////////////////////////////////////////////
        
        

        return neighbors;

    }

    ///////////////////////////////////////////////////////////////////////////
    // Challenge 2: The next step is to complete the getLabel function. In this
    // function we are iterating through the returned neighbors, and getting the
    // True or False label and adding that label to our counts.  Tie goes to True
    //////////////////////////////////////////////////////////////////////////

    public static boolean getLabel (List<TestPoint> neighbors)
    {
       //////////////////////////////////////////////////////////////////////////
        // YOUR CODE HERE:
       
        
        return True;  //Delete this line when you're finished with challenge 2.
        /////////////////////////////////////////////////////////////////////////

    }
    
    
    //////////////////////////////////////////////////////////////////////////////
    // Challenge 3: The last step is to iterate through the test set in the knnMain
    // function. First gather your neighbors using the getNeighbors helper function.
    // Then, get the label using the getLabel helper function. Then check whether
    // the label retrieved matches the actual label and increment |correct|
    // accordingly.
    /////////////////////////////////////////////////////////////////////////////

    public static double knnMain(List<TestPoint> trainingSet, List<TestPoint> testSet, int k )
    {
        int correct = 0;
        double accuracy;
        
        ////////////////////////////////////////////////////////////////////////////
        // Challenge: For each instance in |testSet|, get our prediction and then
        // update the test set accuracy.
        // YOUR CODE HERE:
        
        
        /////////////////////////////////////////////////////////////////////////////
        

        
        return accuracy;

    }
    


}
