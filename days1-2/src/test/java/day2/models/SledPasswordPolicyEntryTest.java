package day2.models;

import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.Test;

class SledPasswordPolicyEntryTest {

    @Test
    public void validateCorrectEntryTest(){
        SledPasswordPolicyEntry invalidEntry = new SledPasswordPolicyEntry(2, 9, 'c', "ccccccccc");

        Assertions.assertThat(invalidEntry.validateEntry())
                .isTrue();
    }

    @Test
    public void validateInvalidEntryTest(){
        SledPasswordPolicyEntry invalidEntry = new SledPasswordPolicyEntry(1, 3, 'b', "cdefg");

        Assertions.assertThat(invalidEntry.validateEntry())
                .isFalse();
    }
}