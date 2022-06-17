package eraser;

public class EraserRegex {
    public static String erase(String str) {
        return str.replaceAll("(?<! ) (?! )", "");
    }
}
