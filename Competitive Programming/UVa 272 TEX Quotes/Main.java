import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        StringBuffer sb;
        boolean isOpen = true;
        while(scan.hasNextLine()) {
            sb = new StringBuffer();
            String str = scan.nextLine();
            for (int i = 0; i < str.length(); i++) {
                if (str.charAt(i) == '"') {
                    if (isOpen) {
                        sb.append("``");
                    } else {
                        sb.append("''");
                    }
                    isOpen = !isOpen;
                } else {
                    sb.append(str.charAt(i));
                }
            }
            System.out.println(sb.toString());
        }
    }
}