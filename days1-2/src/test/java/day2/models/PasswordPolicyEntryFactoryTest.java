package day2.models;

import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class PasswordPolicyEntryFactoryTest {

    @Test
    void createSledPwPolicyEntry() {
        final String singleEntry = "1-3 a: abcde";

        Assertions.assertThat(PasswordPolicyEntryFactory.createSledPwPolicyEntry(singleEntry))
                .usingRecursiveComparison()
                .isEqualTo(new SledPasswordPolicyEntry(1,3,'a',"abcde"));
    }

    @Test
    void createTobogganPwPolicyEntry() {
        final String singleEntry = "1-3 b: cdefg";

        Assertions.assertThat(PasswordPolicyEntryFactory.createTobogganPwPolicyEntry(singleEntry))
                .usingRecursiveComparison()
                .isEqualTo(new SledPasswordPolicyEntry(1,3,'b',"cdefg"));
    }
}