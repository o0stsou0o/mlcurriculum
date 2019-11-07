package edu.southfayette.ml;

public class Distances{

    public double dist;
    public double x;
    public double y;
    public boolean supernova;

    public Distances(double dist, double x, double y, boolean supernova)

    {
        this.dist = dist;
        this.x = x;
        this.y = y;
        this.supernova = supernova;

    }

    public double getDist(){
        return dist;

    }



}
