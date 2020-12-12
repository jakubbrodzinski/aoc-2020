package day1.models;

import lombok.Data;

import java.util.function.BiFunction;

@Data
public class Pair {
    private final int x;
    private final int y;

    public <T> T combine(BiFunction<Integer,Integer,T> biFunction) {
        return biFunction.apply(x, y);
    }
}
