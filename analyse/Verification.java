import algos.Efficacite29;
import algos.Efficacite135;
import algos.Sobriete92;

public class Verification {
    
    public static void main(String[] args) {
        System.out.println("Efficacite29");
        try {
            boolean ok = true;
            if (!Efficacite29.erase("").equals("")) {
                ok = false;
            }
            if (!Efficacite29.erase("   06   07 65 19 70 ").equals("   06   07651970")) {
                ok = false;
            } 
            if (!Efficacite29.erase(" 666, the number of the beast  ").equals("666,thenumberofthebeast  ")) {
                ok = false;
            } 
            if (!Efficacite29.erase("  Cou cou  J M  B").equals("  Coucou  JM  B")) {
                ok = false;
            } 
            if (!Efficacite29.erase(" a a a a   ").equals("aaaa   ")) {
                ok = false;
            } 
            if (ok) {
                System.out.println("ok"); // Fonctionne !
            } 
            else {
                System.out.println("pas ok"); // Ne fonctionne pas comme attendu
            } 
        }
        catch (Exception e) {
            System.out.println(e.getMessage());
            System.out.println("Exception levee"); // Exception levée
        }
        System.out.println("Efficacite135");
        try {
            boolean ok = true;
            if (!Efficacite135.erase("").equals("")) {
                ok = false;
            }
            if (!Efficacite135.erase("   06   07 65 19 70 ").equals("   06   07651970")) {
                ok = false;
            } 
            if (!Efficacite135.erase(" 666, the number of the beast  ").equals("666,thenumberofthebeast  ")) {
                ok = false;
            } 
            if (!Efficacite135.erase("  Cou cou  J M  B").equals("  Coucou  JM  B")) {
                ok = false;
            } 
            if (!Efficacite135.erase(" a a a a   ").equals("aaaa   ")) {
                ok = false;
            } 
            if (ok) {
                System.out.println("ok"); // Fonctionne !
            } 
            else {
                System.out.println("pas ok"); // Ne fonctionne pas comme attendu
            } 
        }
        catch (Exception e) {
            System.out.println(e.getMessage());
            System.out.println("Exception levee"); // Exception levée
        }
        System.out.println("Sobriete92");
        try {
            boolean ok = true;
            if (!Sobriete92.erase("").equals("")) {
                ok = false;
            }
            if (!Sobriete92.erase("   06   07 65 19 70 ").equals("   06   07651970")) {
                ok = false;
            } 
            if (!Sobriete92.erase(" 666, the number of the beast  ").equals("666,thenumberofthebeast  ")) {
                ok = false;
            } 
            if (!Sobriete92.erase("  Cou cou  J M  B").equals("  Coucou  JM  B")) {
                ok = false;
            } 
            if (!Sobriete92.erase(" a a a a   ").equals("aaaa   ")) {
                System.out.println(Sobriete92.erase(" a a a a   "));
                ok = false;
            } 
            if (ok) {
                System.out.println("ok"); // Fonctionne !
            } 
            else {
                System.out.println("pas ok"); // Ne fonctionne pas comme attendu
            } 
        }
        catch (Exception e) {
            System.out.println(e.getMessage());
            System.out.println("Exception levee"); // Exception levée
        }
    }

}
