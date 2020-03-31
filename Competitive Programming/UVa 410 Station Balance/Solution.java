import java.util.Scanner;
import java.util.Arrays;

public class Solution {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        while(scan.hasNext()) {
            int c = scan.nextInt();
            int s = scan.nextInt();
            int[] a = new int[s];
            int[][] sets = new int[c][2];
            for (int i = 0; i < s; i++) {
                a[i] = scan.nextInt();
            }
            Arrays.sort(a);
            int n = 0;
            sets[0][0] = a[a.length-1];
            for (int i = 1; i < c; i++) {
                sets[i][0] = a[n++];
                if (n >= a.length) {
                    break;
                }
            }
            int N = n;
            n = a.length-2;
            for (int i = 1; i < c; i++) {
                sets[i][1] = a[n--];
                if (n == N-1) {
                    break;
                }
            }
            int am = 0;
            float imbalance = 0.0;
            for (int i = 0; i < s; i++) {
                am += a[i];
            }
            for (int i = 0; i < c; i++) {
                
            }

            // System.out.println(Arrays.deepToString(sets));
        }
    }
}