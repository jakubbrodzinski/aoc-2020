package day2;

import day2.models.PasswordPolicyEntry;
import day2.models.PasswordPolicyEntryFactory;
import day2.models.SledPasswordPolicyEntry;
import lombok.AllArgsConstructor;

import java.util.List;
import java.util.function.Function;

@AllArgsConstructor
public class PasswordPhilosophy {
    private final List<String> entries;

    public long countValidTobogganEntries(){
        return countValidEntries(PasswordPolicyEntryFactory::createTobogganPwPolicyEntry);
    }

    public long countValidSledEntries(){
        return countValidEntries(PasswordPolicyEntryFactory::createSledPwPolicyEntry);
    }

    private long countValidEntries(Function<String, PasswordPolicyEntry> factoryFunction){
        return entries.stream()
                .map(factoryFunction)
                .filter(PasswordPolicyEntry::validateEntry)
                .count();
    }
}
