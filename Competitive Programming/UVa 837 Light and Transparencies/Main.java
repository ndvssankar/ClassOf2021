import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;
import java.text.DecimalFormat;

class Point {
    float x, y;
    public Point(float x, float y) {
        this.x = x;
        this.y = y;
    }
    public String toString() {
        return "Point : X = " + this.x;
    }
    public boolean compare(Point point) {
        if (this.x < point.x) {
            return true;
        }
        return false;
    }
}

class LineSegment {
    Point p1;
    Point p2;
    float te;
    public LineSegment(Point p1, Point p2, float te) {
        this.p1 = p1;
        this.p2 = p2;
        this.te = te;
    }
    public String toString() {
        return p1 + " " + p2;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        while (scan.hasNextLine()) {
            int t = Integer.parseInt(scan.nextLine());
            DecimalFormat df = new DecimalFormat("#.##");

            for (int i = 0; i < t; i++) {
                scan.nextLine();
                int n = Integer.parseInt(scan.nextLine());
                ArrayList<LineSegment> ls = new ArrayList<LineSegment>();
                Point[] pts = new Point[2 * n];
                int count = 0;
                for (int j = 0; j < n; j++) {
                    String[] tokens = scan.nextLine().split(" ");
                    pts[count++] = new Point(Float.parseFloat(df.format(Float.parseFloat(tokens[0]))), Float.parseFloat(df.format(Float.parseFloat(tokens[1]))));
                    pts[count++] = new Point(Float.parseFloat(df.format(Float.parseFloat(tokens[2]))), Float.parseFloat(df.format(Float.parseFloat(tokens[3]))));
                    ls.add(new LineSegment(
                        new Point(Float.parseFloat(df.format(Float.parseFloat(tokens[0]))), Float.parseFloat(df.format(Float.parseFloat(tokens[1])))),
                        new Point(Float.parseFloat(df.format(Float.parseFloat(tokens[2]))), Float.parseFloat(df.format(Float.parseFloat(tokens[3])))),
                        Float.parseFloat(df.format(Float.parseFloat(tokens[4])))));
                }
                Arrays.sort(pts, new Comparator<Point>() {
                    @Override
                    public int compare(Point p1, Point p2) {
                        if (p1.x < p2.x) {
                            return -1;
                        } else if (p1.x > p2.x) {
                            return 1;
                        }
                        return 0;
                    }
                });
                if (pts.length == 0) {
                    System.out.println(1);
                    System.out.println("-inf +inf 1.000");
                } else {
                    System.out.println(2 * n + 1);
                    System.out.printf("-inf %.3f 1.000\n", pts[0].x);
                    for (int k = 0; k < pts.length-1; k++) {
                        float x1 = pts[k].x;
                        float x2 = pts[k+1].x;
                        System.out.printf("%.3f %.3f %.3f\n", x1, x2, elevatedLight(ls, x1, x2));
                    }
                    if (pts.length != 0)
                        System.out.printf("%.3f +inf 1.000", pts[pts.length-1].x);
                }
                System.out.println();
                System.out.println();
            }
        }
    }
    public static float elevatedLight(ArrayList<LineSegment> ls, float x1, float x2) {
        float p = 1.000f;
        // System.out.println("=================" + x1 +  " :: " + x2);
        for (LineSegment line : ls) {
            if (line.p1.x < line.p2.x) {
                if (x1 >= line.p1.x && x2 <= line.p2.x) {
                    // System.out.println(line + " :: " +p);
                    p = p * line.te;
                }
            } else {
                if (x1 < line.p1.x && x2 > line.p2.x) {
                    // System.out.println(line + " :: " +p);
                    p = p * line.te;
                }
            }
        }
        return p;
    }
}