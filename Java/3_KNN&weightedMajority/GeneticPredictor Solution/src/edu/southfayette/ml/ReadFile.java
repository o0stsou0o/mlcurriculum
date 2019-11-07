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

            x = new Scanner(inventoryFile);



        }



        catch (FileNotFoundException ex){

            System.out.println("could not find file");
        }


    }

    public List<DnaString> readFile(){


        List<DnaString> data = new ArrayList<DnaString>();

        while(x.hasNext()){

            String strand = x.next();
            String survival = x.next();
            data.add(new DnaString(strand, survival));
        }
        return data;



    }

    public void closeFile()
    {
        x.close();
    }

}

