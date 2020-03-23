import java.util.Scanner;
import java.text.*;
public class Main {
    public static void main(String args[]) {
        Scanner scan = new Scanner(System.in);
        while(scan.hasNext()) {
            int h = scan.nextInt();
            if (h == 0) {
                break;
            }
            float u = (float)scan.nextInt();
            float d = (float)scan.nextInt();
            float f = (float)scan.nextInt();
            int days = 0;
            float initialHeight = 0.0f;
            float distanceClimbed = u;
            float fatigueFactor = u * (f / 100.0f);
            float heightAfterClimbing = initialHeight + u;
            float heightAfterSliding = heightAfterClimbing - d;
            DecimalFormat df = new DecimalFormat("#.##");
            do {
                days++;
                if (days == 1) {

                } else {
                    initialHeight = heightAfterSliding;
                    distanceClimbed = Float.parseFloat(df.format(distanceClimbed - fatigueFactor));
                    if (distanceClimbed <= 0.0f) {
                        distanceClimbed = 0;
                    }
                    heightAfterClimbing = Float.parseFloat(df.format(initialHeight + distanceClimbed));
                    heightAfterSliding = Float.parseFloat(df.format(heightAfterClimbing - d));
                }
                System.out.println(days + " :: " + initialHeight + " :: " + distanceClimbed + " :: " + heightAfterClimbing + " :: " + heightAfterSliding);
                
                if (heightAfterClimbing > h) {
                    System.out.println("success on day " + days);
                    break;
                }
                // heightAfterSliding = Float.parseFloat(df.format(heightAfterClimbing - d));
                if (heightAfterSliding < 0) {
                    System.out.println("failure on day " + days);
                    break;
                }
            } while(true);
        }
        scan.close();
    }
}