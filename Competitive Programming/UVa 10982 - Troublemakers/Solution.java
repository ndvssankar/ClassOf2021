import java.util.ArrayList;
import java.util.Scanner;

class Pair {
    int x;
    int y;
    public Pair(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public int getX() {
        return this.x;
    }

    public void setX(int x) {
        this.x = x;
    }

    public int getY() {
        return this.y;
    }

    public void setY(int y) {
        this.y = y;
    }

    public Pair x(int x) {
        this.x = x;
        return this;
    }

    public Pair y(int y) {
        this.y = y;
        return this;
    }

    @Override
    public String toString() {
        return "{" +
            " x='" + getX() + "'" +
            ", y='" + getY() + "'" +
            "}";
    }
}

public class Solution {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int t = scan.nextInt();
        for (int k = 0; k < t; k++) {
            int n = scan.nextInt();
            int m = scan.nextInt();
            // System.out.printf("t = %d :: n = %d :: m = %d\n", t, n ,m);
            Pair[] pairs = new Pair[m];
            for (int j = 0; j < m; j++) {
                pairs[j] = new Pair(scan.nextInt(), scan.nextInt());
                // System.out.println(pairs[j]);
            }
            int[] graph = new int[n+1];
            for (int i = 1; i <= n; i++) {
                int[] cnt = new int[2];
                for (int j = 0; j < m; j++) {
                    if (pairs[j].x <= i && pairs[j].y <= i && (pairs[j].x == i || pairs[j].y == i)) {
                        // System.out.println("Here....");
                        if (pairs[j].x == i) {
                            cnt[graph[pairs[j].y]] += 1;
                        } else {
                            cnt[graph[pairs[j].x]] += 1;
                        }
                    }
                    // System.out.printf("Iter :: i : %d, j : %d, cnt[0] : %d, cnt[1] : %d", i, j, cnt[0], cnt[1]);
                    // System.out.println();
                }
                
                // if (cnt[0] > cnt[1]) {
                //     graph[i] = 1;
                // }
            }
            ArrayList<Integer> lst = new ArrayList<Integer>();
            for (int i = 1; i <= n; i++) {
                System.out.println(i + " :: " + graph[i]);
                if (graph[i] == 1) {
                    lst.add(i);
                }
            }
            System.out.printf("Case #%d: %d\n", k+1, lst.size());
            for (int i = 0; i < lst.size(); i++) {
                System.out.print(lst.get(i) + " ");
            }
            System.out.println();
        }
        scan.close();
    }
}