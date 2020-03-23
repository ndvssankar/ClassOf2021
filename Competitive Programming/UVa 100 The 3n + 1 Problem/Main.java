import java.util.*;
public class Main {
    static int[] arr = new int[1000000];
    public static int findChainLength(int x) {
        int len = 1;
        // System.out.println("::" + x);
        while (x!=1) {
            // if (x < 1000000 && arr[x] != 0) {
            //     len = len + arr[x];
            //     return len;
            // }
            if (x%2 == 0) {
                x = x >> 1;
            } else {
                x = 3 * x + 1;
            }
            len++;
        }
        arr[x] = len;
        return len;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        long totalTime = 0;
        while (scan.hasNext()) {
            long st = System.currentTimeMillis();
            int x = scan.nextInt();
            int y = scan.nextInt();
            boolean flag = false;
            if (x > y) {
                int tmp = x;
                x = y;
                y = tmp;
                flag = true;
            }
            int length = 0;
            for (int i = x; i <= y; i++) {
                int lenI = findChainLength(i);
                if (length < lenI) {
                    length = lenI;
                }
            }
            long et = System.currentTimeMillis();
            totalTime += (et-st);
            if (!flag) {
                System.out.println(x + " " + y + " " + length + " " + (et-st));
            } else {
                System.out.println(y + " " + x + " " + length + " " + (et-st));
            }
        }
        System.out.println(totalTime);
    }
}
