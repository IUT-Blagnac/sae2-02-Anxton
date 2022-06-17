import algos.Efficacite29;
import algos.Efficacite135;

import java.time.Duration;
import java.time.Instant;
import java.util.ArrayList;
import java.util.Random;

import algos.Efficacite135;

public class Analyse {
    public static void main(String[] args) {
        String alphabet = "abcdefghijklmnopqrstuvwxyz        ";
        StringBuilder sb = new StringBuilder();
        Random rand = new Random();

        int longueur = 200000;
        for (int i = 0; i < longueur; i++) {
            sb.append(alphabet.charAt(rand.nextInt(alphabet.length())));
        }
        String chaine = sb.toString();


        Instant inst1 = Instant.now();
        Efficacite29.erase(chaine);
        Instant inst2 = Instant.now();    
        
        System.out.println("Efficacite29 : "+ Duration.between(inst1, inst2).toString());
        
        inst1 = Instant.now();
        Efficacite135.erase(chaine);
        inst2 = Instant.now();

        System.out.println("Efficacite135 : "+ Duration.between(inst1, inst2).toString());
        
    }
}