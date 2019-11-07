package edu.southfayette.ml;

public class DnaString {
    public final String strand;
    public final String survival;

    public DnaString(String strand, String survival ){
        this.strand = strand;
        this.survival = survival;
    }

    @Override
    public String toString() {
        return String.format("%s %s", strand, survival);
    }
}
