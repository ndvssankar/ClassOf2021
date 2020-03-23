import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int count = 0;
        while(scan.hasNextLine()) {
            count = count + 1;
            String line = scan.nextLine();
            // System.out.println("Line is : " + line);
            String[] tokens = line.split("\\s");
            int n = Integer.parseInt(tokens[0]);
            int m = Integer.parseInt(tokens[1]);
            int c = Integer.parseInt(tokens[2]);
            if (n == 0) {
                break;
            }
            int[] amps = new int[n+1];
            boolean[] isOn = new boolean[n+1];
            for (int i = 0; i < n; i++) {
                amps[i+1] = Integer.parseInt(scan.nextLine());
                // System.out.print(" :: " + amps[i+1]);
                isOn[i+1] = false;
            }
            // System.out.println();
            int maxAmps = -99999999;
            int totalCapacity = 0;
            boolean output = true;
            for (int i = 0; i < m; i++) {
                int device = Integer.parseInt(scan.nextLine());
                // System.out.print(" :: " + device);
                if (isOn[device]) {
                    isOn[device] = false;
                    totalCapacity -= amps[device];
                } else {
                    isOn[device] = true;
                    totalCapacity += amps[device];
                }
                // System.out.println(amps[device] + " : Total amps : " + totalCapacity);
                if (maxAmps < totalCapacity) {
                    maxAmps = totalCapacity;
                }
                if (totalCapacity > c && output) {
                    output = false;
                    System.out.println("Sequence " + count);
                    System.out.println("Fuse was blown.");
                    System.out.println();
                }
            }
            // System.out.println();
            if (totalCapacity <= c && output) {
                System.out.println("Sequence " + count);
                System.out.println("Fuse was not blown.");
                System.out.println("Maximal power consumption was " + maxAmps + " amperes.");
                System.out.println();
            }
        }
    }
}