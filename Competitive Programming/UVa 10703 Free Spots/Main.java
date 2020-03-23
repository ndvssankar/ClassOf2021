import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        while(scan.hasNextLine()) {
            String line = scan.nextLine().trim();
            // System.out.println("First line : " + line);
            String[] tokens = line.split("\\s");
            int w = Integer.parseInt(tokens[0]);
            int h = Integer.parseInt(tokens[1]);
            int n = Integer.parseInt(tokens[2]);
            if (w == 0 && h == 0 && n == 0)
                break;
            boolean board[][] = new boolean[h][w];
            for (int i = 0; i < n; i ++) {
                line = scan.nextLine().trim();
                tokens = line.split("\\s");
                int x1 = Integer.parseInt(tokens[0]);
                int y1 = Integer.parseInt(tokens[1]);
                int x2 = Integer.parseInt(tokens[2]);
                int y2 = Integer.parseInt(tokens[3]);
                // System.out.println("Inner line : " + x1 + y1 + x2 + y2);
                if (x1 > x2) {
                    int t = x1;
                    x1 = x2;
                    x2 = t;
                }
                if (y1 > y2) {
                    int t = y1;
                    y1 = y2;
                    y2 = t;
                }
                for (int y = y1 - 1; y < y2; y++) {
                    for (int x = x1 - 1; x < x2; x++) {
                        board[y][x] = true;
                    }
                }
            }
            int count = 0;
            for (int y = 0; y < h; y++) {
                for (int x = 0; x < w; x++) {
                    if (!board[y][x]) {
                        count++;
                    } else {
                        board[y][x] = false;
                    }
                }
            }
            if (count == 0) {
                System.out.println("There is no empty spots.");
            } else if (count == 1) {
                System.out.println("There is one empty spot.");
            } else {
                System.out.println("There are " + count + " empty spots.");
            }
            line = scan.nextLine();
        }
    }
}