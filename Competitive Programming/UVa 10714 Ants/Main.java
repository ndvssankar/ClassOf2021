import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int t = scan.nextInt();
        while (t-- > 0) {
            int l = scan.nextInt();
            int n = scan.nextInt();
            int min = 0, max = 0;
            while(n-- > 0) {
                int x = scan.nextInt();
                x = x < l-x ? x : l-x;
                if (x > min)
                    min = x;
                if (l-x > max)
                    max = l - x;
            }
            System.out.println(min + " " + max);
        }
        scan.close();
    }
}