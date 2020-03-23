import java.util.Scanner;
import java.util.Queue;
import java.util.LinkedList;

class Cache {
    int size;
    Queue<Integer> queue; 
    int missCount = 0;
    public Cache(int size) {
        this.size = size;
        queue = new LinkedList<Integer>();
    }

    public void accessAddress(int addr) {
        if (queue.contains(addr)) {
            boolean flag = queue.remove(addr);
            queue.add(addr);
        } else if (queue.size() == this.size) {
            missCount += 1;
            int item = queue.remove();
            queue.add(addr);
        } else {
            missCount += 1;
            queue.add(addr);
        }
    }
    public int getMissCount() {
        return missCount;
    }
    public void setMissCount(int count) {
        this.missCount = count;
    }
}

public class Main {
    public static void main(String args[]) {
        Scanner scan = new Scanner(System.in);
        int numberOfCaches = Integer.parseInt(scan.nextLine());
        String[] tokens = scan.nextLine().split(" ");
        Cache[] cache = new Cache[numberOfCaches];
        for (int i = 0; i < tokens.length; i++) {
            cache[i] = new Cache(Integer.parseInt(tokens[i]));
        }
        while(scan.hasNextLine()) {
            tokens = scan.nextLine().split(" ");
            switch(tokens[0]) {
                case "RANGE":
                    int b = Integer.parseInt(tokens[1]);
                    int y = Integer.parseInt(tokens[2]);
                    int n = Integer.parseInt(tokens[3]);
                    for (int i = 0; i < numberOfCaches; i++) {
                        for (int j = 0; j < n; j++)
                            cache[i].accessAddress(b + y * j);
                    }
                    break;
                case "ADDR":
                    for (int i = 0; i < numberOfCaches; i++)
                        cache[i].accessAddress(Integer.parseInt(tokens[1]));
                    break;
                case "STAT":
                    StringBuffer sb = new StringBuffer();
                    for (int i = 0; i < numberOfCaches; i++) {
                        sb.append(cache[i].getMissCount() + " ");
                        cache[i].setMissCount(0);
                    }
                    System.out.println(sb.toString().trim());
                    break;
                default:
                    return;
            }
        }
    }
}