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

        System.out.println(knnMain(trainingData, testData, 3));



    }



    public static double distance (double x0, double y0, double x1, double y1){

        double dx = x1 - x0;
        double dy = y1 - y0;

        double temp = Math.pow(dx,2) + Math.pow(dy,2);


        return Math.sqrt(temp);
    }

    public static List<TestPoint> getNeighbors (List<TestPoint> trainingSet, TestPoint testInstance, int k){

        int size = trainingSet.size();

        Distances [] distanceArray = new Distances[size];

        for (int i = 0; i < size; i++) {
            double x1 = trainingSet.get(i).x;
            double y1 = trainingSet.get(i).y;

            double dist = distance(testInstance.x, testInstance.y, x1, y1);
            distanceArray[i] = new Distances(dist, x1, y1, trainingSet.get(i).supernova);


        }


        int len = distanceArray.length;

        for (int i = 0; i < len ; i++) {
            int minIndex = i;
            for (int j = i+1; j < len; j++) {
                if (distanceArray[j].dist < distanceArray[minIndex].dist)
                {
                    minIndex = j;
                }
            }
            //swap(distArray, i, minIndex);
            Distances temp = distanceArray[i];
            distanceArray[i] = distanceArray[minIndex];
            distanceArray[minIndex] = temp;
        }



        List<TestPoint> neighbors = new ArrayList<TestPoint>();


        for (int i = 0; i < k; i++) {
            double x = distanceArray[i].x;
            double y = distanceArray[i].y;
            boolean nova = distanceArray[i].supernova;
            neighbors.add(new TestPoint(x, y, nova));

        }

        return neighbors;

    }



    public static boolean getLabel (List<TestPoint> neighbors)
    {
        int[] typeVotes = new int[2];
        typeVotes[0] = 0;  //true
        typeVotes[1] = 0; // false
        int len = neighbors.size();
        for (int i = 0; i < len; i++) {

            boolean curNeighbor = neighbors.get(i).supernova;
            if (curNeighbor)
            {
                typeVotes[0] +=1;
            }
            else{
                typeVotes[1] +=1;
            }

        }
        if (typeVotes[0] >= typeVotes[1])
            return true;
        return false;

    }


    public static double knnMain(List<TestPoint> trainingSet, List<TestPoint> testSet, int k )
    {
        double total = testSet.size();
        double correct = 0;
        double accuracy = 0;

        for (int i = 0; i < total; i++) {

            List<TestPoint> neighbors = getNeighbors(trainingSet, testSet.get(i), k);
            boolean label = getLabel(neighbors);
            boolean actualLabel = testSet.get(i).supernova;
            if (label == actualLabel)
                correct +=1;

        }

        accuracy = (correct/total)*100;

        return accuracy;

    }
    


}
