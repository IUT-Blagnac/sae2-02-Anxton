package eraser;

import java.lang.reflect.Field;

public class Eraser {

    public static String erase(String str) {
        String result = "";
        int size = str.length();

        for (int i = 0 ; i < size ; ++i) {
            char car = str.charAt(i);
            // On a trouvé un espace
            if (car == 32) {
                int cpt = 1;
                while(i+cpt < size && str.charAt(i+cpt) == 32) {
                    result += ' ';
                    cpt++;
                }

                if(cpt != 1) {
                    result += ' ';
                    i+=cpt-1;
                }


            }

            else {
                result += str.charAt(i);
            }

        }

        return result;
    }
}
