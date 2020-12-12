package day2.models;

import lombok.AccessLevel;
import lombok.AllArgsConstructor;
import lombok.Getter;

@Getter
@AllArgsConstructor(access = AccessLevel.PACKAGE)
public class TobogganPasswordPolicyEntry implements PasswordPolicyEntry{
    private final int leftIndex;
    private final int rightIndex;
    private final char policyCharacter;
    private final String password;

    public boolean validateEntry(){
        return password.charAt(leftIndex-1) == policyCharacter ^ password.charAt(rightIndex-1) == policyCharacter;
    }
}
