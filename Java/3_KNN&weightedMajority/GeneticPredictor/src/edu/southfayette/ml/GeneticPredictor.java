package edu.southfayette.ml;
import java.util.*;

// Weighting Mesopotamia

// You are a government leader of Mesopotamia, and Mesopotamia is facing an
// influx of immigrants, many of whom die, and you want to determine what
// factors contribute to people dying so that immigrants can make an informed
// decision.
//
// The initial settlement is conducting the first 5 year experiment. At the
// end of the five years, they have their data telling them,the DNA sequence
// of each individual and whether they survived for five years or not. The
// data may look something like the following (training set). Note:
// Mesopotamians had different symbols to represent a DNA strand.
//
// After the first five years, a new group of settlers come in (test set).
// Their DNA sequence is written down, and the settlers predict whether they
// will live or die based on the DNA sequences and results of the previous
// experiment. (explained below)
//
// The results are looked at, after five years, and weights are given to
// each expert depending on whether it predicted correctly.
// This civilization has the following type of data: [“MYDNASTRANDS”, “live”]


///////////////////////////////////////////////////////////////////////////







public class GeneticPredictor {
    public static void main(String[] args){
        
        double expertWeights[]= {1, 1, 1};
        ReadFile r = new ReadFile();
        r.openFile();
        List<DnaString> data = r.readFile();
        r.closeFile();

        System.out.println(data);

        int divider = data.size()/2;
        List<DnaString> trainingData = data.subList(0, divider);
        List<DnaString> testData = data.subList(divider, data.size());

        double[] experts = knnMain(trainingData, testData, expertWeights);
        System.out.println(experts);


    }

    ///////////// KNN to get weights of branches ////////////////
    

    // This distance formula is using the four letters of a string starting at
    // the expert's index to calculate the distance between DNA strings.
    // For example ABCD, TYUY we would have Character.getNumericValue(A)-Character.getNumericValue(T) + Character.getNumericValue(B)-Character.getNumericValue(Y) ...
    
    public static double distance(String dna1, String dna2, int expertIndex){

        String newDna1 = dna1.substring(expertIndex*4, (expertIndex +1)*4);

        String newDna2 = dna2.substring(expertIndex*4, (expertIndex+1 )*4);

        int total = 0;

        int length = newDna1.length();

        for (int i = 0; i < length ; i++) {

            char a = newDna1.charAt(i);
            char b = newDna2.charAt(i);
            total += Math.abs(Character.getNumericValue(a) - Character.getNumericValue(b));

        }

        return total;

    }

    // Returns the K closest neighbors to the current test instance
    public static List<DnaString> getNeighbors(List<DnaString> trainingSet, DnaString testInstance, int k, int expertIndex)
    {

        String testDna = testInstance.strand;
        int length = trainingSet.size();
        DnaDistances[] dists = new DnaDistances[length];
        
        // Here we want to calculate the distance between our current point, and
        // the test point. (Use the helper function)
        // Note, the distance function doesn't require x, y points but the
        // dna strands and expert index.
        
        //////////////////////////////////////////////////////////////
        // Fill in here
       //////////////////////////////////////////////////////////////////
        
        // For our design we will be storing the distances in an array of DnaDistances dists so we
        // can easily sort them below
   

        // Sorting the dists array below.
        for (int i = 0; i < length; i++) {
            int minIndex = i;
            for (int j = i+1; j < length; j++) {
                if (dists[j].distance < dists[minIndex].distance)
                {
                    minIndex = j;
                }

            }
            DnaDistances temp = dists[i];
            dists[i] = dists[minIndex];
            dists[minIndex] = temp;

        }

        
        List<DnaString> neighbors = new ArrayList<DnaString>();

        // Here we would like to return only the k closest training instances.
        // So we will be appending the top 3 distances
        
        //////////////////////////////////////////////////
        // Fill in here
        //////////////////////////////////////////////////
        return neighbors;
    }
    
    
    // Returns True, if the majority of the closest neighbors live,
        // false otherwise
    public static String getLabel(List<DnaString> neighbors) {

        int[] typeVotes = new int[2]; 
        typeVotes[0] = 0;  //live
        typeVotes[1] = 0;  //die
        
        // Here we will iterate through neighbors and retrieve the true or false
        // type of each neighbor and add it to the dictionary type votes.
        
        ////////////////////////////////////////////////////////////////
        // Fill in here
        ////////////////////////////////////////////////////////////
        
        if (typeVotes[0] >= typeVotes[1]){
            return "live";

        }
        else{
            return "die";

            }
        }


    public static double[] knnMain(List<DnaString> trainingSet, List<DnaString> testSet, double[] experts)
    {

        int k = 3;
        double penalty = .5;
        // Iterate through each instance in the testSet. For each testInstance, we
        // will also iterate through each expert. From there we will find the
        // neighbors, labels, and actual label based on that testInstance-expert
        // scenario, and downweight the current expert if the label came back
        //incorrect.
            
            //////////////////////////////////////////////////////////////
            // Fill in here
            //////////////////////////////////////////////////////////////

        
        return experts;
    }

}
