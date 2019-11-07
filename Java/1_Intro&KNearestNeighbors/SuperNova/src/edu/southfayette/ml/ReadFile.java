package edu.southfayette.ml;


import java.io.BufferedReader;
import java.io.FileReader;
import java.util.*;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.io.File;
import java.util.logging.Level;
import java.util.logging.Logger;

public class ReadFile {
    private Scanner x;


    public void openFile(){
    try {

        File inventoryFile = new File("/Users/stephentsou/IdeaProjects/SuperNova/src/edu/southfayette/ml/data.txt");


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


    public List<TestPoint> readFile(){

            List<TestPoint> data = new ArrayList<TestPoint>();



            while(x.hasNext()){


                //get rid of commas?
                String a = x.next();
                String b = x.next();
                String c = x.next();
                double x = Double.parseDouble(a);
                double y = Double.parseDouble(b);
                boolean z = Boolean.parseBoolean(c);
                data.add(new TestPoint(x, y, z));
                //data[i].x = Double.parseDouble(a);
                //data[i].y = Double.parseDouble(b);
                //which one of these is correct?
                //data[i].supernova = Boolean.valueOf(c);
                //data[i].supernova = Boolean.parseBoolean(c);

                //System.out.printf("%d %d %s\n", a, b, c);

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

