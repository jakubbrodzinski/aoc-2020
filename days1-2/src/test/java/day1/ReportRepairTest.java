package day1;

import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.Test;
import utils.TestFileReader;

import java.io.IOException;
import java.util.Arrays;
import java.util.List;
import java.util.Objects;
import java.util.stream.Collectors;

class ReportRepairTest {

    @org.junit.jupiter.api.Test
    void findPairTest() throws IOException {
        final String path = "day1/rr";

        ReportRepair reportRepair = new ReportRepair(2020, getInputData(path));

        Assertions.assertThat(reportRepair.findPair())
                .isPresent()
                .get()
                .isEqualTo(514579);
    }

    @org.junit.jupiter.api.Test
    void actualFindPair() throws IOException {
        final String path = "day1/actual-data";

        ReportRepair reportRepair = new ReportRepair(2020, getInputData(path));

        System.out.println(reportRepair.findPair());
    }

    @Test
    void findTripletTest() throws IOException {
        final String path = "day1/rr";

        ReportRepair reportRepair = new ReportRepair(2020, getInputData(path));

        Assertions.assertThat(reportRepair.findTriplet())
                .isPresent()
                .get()
                .isEqualTo(241861950);
    }

    @org.junit.jupiter.api.Test
    void actualTriplet() throws IOException {
        final String path = "day1/actual-data";

        ReportRepair reportRepair = new ReportRepair(2020, getInputData(path));

        System.out.println(reportRepair.findTriplet());
    }

    private List<Integer> getInputData(String path) throws IOException {
        return TestFileReader.getInputLines(path,Integer::valueOf);
    }
}