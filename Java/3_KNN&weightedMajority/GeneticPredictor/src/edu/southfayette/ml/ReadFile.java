package edu.southfayette.ml;


import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class ReadFile {
    private Scanner x;


    public void openFile(){
        try {
            File inventoryFile = new File("/Users/stephentsou/IdeaProjects/GeneticPredictor/src/edu/southfayette/ml/data.txt");
            System.out.println("hello there 1");
            x = new Scanner(inventoryFile);

            //String nextLine = inventoryScanner.nextLine();
            //String[] venicleComponents = nextLine.split(",");
            //System.out.println("Next Line: " + nextLine);
            //int[] hello = new int[];//feed the data in.
            //BufferedReader br = new BufferedReader(new FileReader("file.txt"));

        }



        catch (FileNotFoundException ex){

            System.out.println("could not find file");
        }


    }

    public List<DnaString> readFile(){
        System.out.println("hello there 2");

        List<DnaString> data = new ArrayList<DnaString>();

        while(x.hasNext()){
            System.out.println("hello there 3");
            String strand = x.next();
            String survival = x.next();
            data.add(new DnaString(strand, survival));
        }
        return data;

        //File inventoryFile = new File("data.txt");
        //Scanner inventoryScanner = new Scanner(inventoryFile);

        //String nextLine = inventoryScanner.nextLine();
        //String[] venicleComponents = nextLine.split(",");
        //System.out.println("Next Line: " + nextLine);
        //int[] hello = new int[];//feed the data in.
        //BufferedReader br = new BufferedReader(new FileReader("file.txt"));

    }

    public void closeFile()
    {
        x.close();
    }

}

