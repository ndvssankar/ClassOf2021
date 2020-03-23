import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        boolean isOpen = true;
        while(scan.hasNextLine()) {
            String str = scan.nextLine();
            for (int i = 0; i < str.length(); i++) {
                if (str.charAt(i) == '"') {
                    if (isOpen) {
                        System.out.print("``");
                    } else {
                        System.out.print("''");
                    }
                    isOpen = !isOpen;
                } else {
                    System.out.print(str.charAt(i));
                }
            }
            System.out.println();
        }
    }
}