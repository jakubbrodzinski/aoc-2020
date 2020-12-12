package day2.models;

import lombok.AccessLevel;
import lombok.AllArgsConstructor;
import lombok.Getter;

@Getter
@AllArgsConstructor(access = AccessLevel.PACKAGE)
public class SledPasswordPolicyEntry implements PasswordPolicyEntry {
    private final int minOccurrences;
    private final int maxOccurrences;
    private final char policyCharacter;
    private final String password;

    public boolean validateEntry(){
        int occurrencesCounter = 0;
        for (char pwElement : password.toCharArray()) {
            if ( pwElement == policyCharacter)
                occurrencesCounter ++;

            if(occurrencesCounter > maxOccurrences)
                return false;
        }
        if(occurrencesCounter < minOccurrences)
            return false;
        else
            return true;
    }
}
