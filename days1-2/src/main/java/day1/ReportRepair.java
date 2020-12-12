package day1;

import day1.models.Pair;
import lombok.AllArgsConstructor;

import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

@AllArgsConstructor
public class ReportRepair {
    private final int year;
    private final List<Integer> entries;

    public Optional<Integer> findPair() {
        return findPairThatSumEqualsTo(entries, this.year)
                .map(pair -> pair.combine((x, y) -> x * y));
    }

    public Optional<Integer> findTriplet() {
        List<Integer> sortedEntries = entries.stream()
                .sorted()
                .collect(Collectors.toList());

        for (int i = 0; i < sortedEntries.size() / 2; i++) {
            List<Integer> subList = sortedEntries.subList(i+1, sortedEntries.size());
            final int iElement = sortedEntries.get(i);
            final int remainingSum = this.year - iElement;

            final var result = findPairThatSumEqualsTo(subList, remainingSum)
                    .map(pair -> pair.combine((x, y) -> iElement * x * y));
            if (result.isPresent())
                return result;
        }
        return Optional.empty();
    }

    private Optional<Pair> findPairThatSumEqualsTo(List<Integer> sortedEntries, int expectedSum) {
        int indexLeft = 0;
        int indexRight = sortedEntries.size() - 1;
        while (indexLeft < indexRight) {
            int elementLeft = sortedEntries.get(indexLeft);
            int elementRight = sortedEntries.get(indexRight);
            final int actualSum = elementLeft + elementRight;

            if (actualSum == expectedSum) {
                return Optional.of(new Pair(elementLeft, elementRight));
            } else if (actualSum < expectedSum) {
                indexLeft += 1;
            } else {
                indexRight -= 1;
            }
        }
        return Optional.empty();
    }
}
