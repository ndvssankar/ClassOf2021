import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        TreeMap<String, Integer> tm = new TreeMap<String, Integer>();
        scan.nextLine();
        while (scan.hasNextLine()) {
            String name = scan.next();
            // System.out.println(name);
            scan.nextLine();
            if (tm.get(name) != null) {
                int c = tm.get(name);
                c = c + 1;
                tm.put(name, c);
            } else {
                tm.put(name, 1);
            }
        }
        Set set = tm.entrySet();
        Iterator iter = set.iterator();
        while(iter.hasNext()) {
            Map.Entry entry = (Map.Entry)iter.next();
            System.out.println(entry.getKey() + " " + entry.getValue());
        }
    }
}