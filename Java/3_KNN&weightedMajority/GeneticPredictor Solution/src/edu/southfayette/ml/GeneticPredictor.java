package edu.southfayette.ml;
import java.util.*;

public class GeneticPredictor {
    public static void main(String[] args){

        double expertWeights[]= new double[]{1.0, 1.0, 1.0};
        ReadFile r = new ReadFile();
        r.openFile();
        List<DnaString> data = r.readFile();
        r.closeFile();

        //System.out.println(data);

        int divider = data.size()/2;
        List<DnaString> trainingData = data.subList(0, divider);
        List<DnaString> testData = data.subList(divider, data.size());
        System.out.println(Arrays.toString(expertWeights));


        double[] experts = knnMain(trainingData, testData, expertWeights);
        System.out.println(Arrays.toString(experts));



    }


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

    public static List<DnaString> getNeighbors(List<DnaString> trainingSet, DnaString testInstance, int k, int expertIndex)
    {

        String testDna = testInstance.strand;
        int length = trainingSet.size();
        DnaDistances[] dists = new DnaDistances[length];
        for (int i = 0; i < length; i++) {
            String curDna = trainingSet.get(i).strand;
            double thisDist = distance(testDna, curDna, expertIndex);
            dists[i] = new DnaDistances(thisDist, trainingSet.get(i));

        }

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

        for (int i = 0; i < k; i++) {
            double a = dists[i].distance;
            DnaString b = dists[i].dna;

            neighbors.add(b);
        }
        return neighbors;
    }

    public static String getLabel(List<DnaString> neighbors) {

        int[] typeVotes = new int[2];
        typeVotes[0] = 0;
        typeVotes[1] = 0;
        int length = neighbors.size();

        for (int i = 0; i < length; i++) {
            String curNeighbor = neighbors.get(i).survival;
            if (curNeighbor.equals("live")){
                typeVotes[0] += 1;
            }
            else{
                typeVotes[1] +=1;

            }}

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
        int expertLength = experts.length;
        int testLength = testSet.size();

        for (int i = 0; i < testLength; i++) {
            for (int j = 0; j < expertLength ; j++) {
                List<DnaString> neighbors = getNeighbors(trainingSet, testSet.get(i), k, j);
                String label = getLabel(neighbors);
                String actualLabel = testSet.get(i).survival;
                if (label != actualLabel){
                    experts[j] = experts[j]*penalty;
                }
            }
        }
        return experts;
    }

}
