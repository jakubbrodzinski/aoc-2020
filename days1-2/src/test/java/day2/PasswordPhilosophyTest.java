package day2;

import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.Test;
import utils.TestFileReader;

import java.io.IOException;
import java.util.List;
import java.util.function.Function;


class PasswordPhilosophyTest {

    @Test
    public void countValidSledEntriesTest() throws IOException {
        final var path = "day2/test-data";
        PasswordPhilosophy passwordPhilosophy = new PasswordPhilosophy(getInputData(path));

        Assertions.assertThat(passwordPhilosophy.countValidSledEntries())
                .isEqualTo(2);
    }

    @Test
    public void findSledSolution() throws IOException {
        final var path = "day2/actual-data";
        PasswordPhilosophy passwordPhilosophy = new PasswordPhilosophy(getInputData(path));

        System.out.println(passwordPhilosophy.countValidSledEntries());
    }

    @Test
    public void countValidTobogganEntriesTest() throws IOException {
        final var path = "day2/test-data";
        PasswordPhilosophy passwordPhilosophy = new PasswordPhilosophy(getInputData(path));

        Assertions.assertThat(passwordPhilosophy.countValidTobogganEntries())
                .isEqualTo(1);
    }

    @Test
    public void findTobogganSolution() throws IOException {
        final var path = "day2/actual-data";
        PasswordPhilosophy passwordPhilosophy = new PasswordPhilosophy(getInputData(path));

        System.out.println(passwordPhilosophy.countValidTobogganEntries());
    }

    private List<String> getInputData(String path) throws IOException {
        return TestFileReader.getInputLines(path, Function.identity());
    }
}