package eraser;

public class Eraser {
    public static String erase(String str) {
        return str.replaceAll("(?<! ) (?! )", "");
    }
}
