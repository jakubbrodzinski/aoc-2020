package utils;


import java.io.IOException;
import java.util.Arrays;
import java.util.List;
import java.util.Objects;
import java.util.function.Function;
import java.util.stream.Collectors;

public class TestFileReader {
    public static <T> List<T> getInputLines(String path, Function<String,T> lineConverter) throws IOException {
        byte[] fileBytes = Objects.requireNonNull(TestFileReader.class.getClassLoader().getResourceAsStream(path))
                .readAllBytes();

        return Arrays.stream(new String(fileBytes).split("\n"))
                .map(lineConverter)
                .collect(Collectors.toList());
    }
}
