package day2.models;

public class PasswordPolicyEntryFactory {

    public static SledPasswordPolicyEntry createSledPwPolicyEntry(String entry){
        String[] splitEntry = parse(entry);
        return new SledPasswordPolicyEntry(Integer.parseInt(splitEntry[0]), Integer.parseInt(splitEntry[1]),
                splitEntry[2].charAt(0), splitEntry[3]);
    }

    public static TobogganPasswordPolicyEntry createTobogganPwPolicyEntry(String entry) {
        String[] splitEntry = parse(entry);
        return new TobogganPasswordPolicyEntry(Integer.parseInt(splitEntry[0]), Integer.parseInt(splitEntry[1]),
                splitEntry[2].charAt(0), splitEntry[3]);
    }

    private static String[] parse(String entry){
        return entry.split("-|: | ");
    }
}
