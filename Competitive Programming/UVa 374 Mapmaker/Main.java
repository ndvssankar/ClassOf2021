import java.util.*;

public class Main {

    public static int findPhysicalAddress(String[] tokens, String[] refs) {
        int baseAddress = Integer.parseInt(tokens[0]);
        int size = Integer.parseInt(tokens[1]);
        int dimn = Integer.parseInt(tokens[2]);
        Vector<Integer> ll = new Vector<Integer>();
        Vector<Integer> ul = new Vector<Integer>();
        int[] cVal = new int[dimn];
        int k = 3;
        for (int i = 0; i < dimn; i++) {
            ll.add(Integer.parseInt(tokens[k]));
            ul.add(Integer.parseInt(tokens[k+1]) - Integer.parseInt(tokens[k]) + 1);
            k += 2;
        }
        int c0 = baseAddress;
        int pos = dimn - 1;
        cVal[pos] = size;
        c0 -= cVal[pos] * ll.get(pos);
        System.out.println("cVal[" + pos + "]" + " = " + cVal[pos]);
        for (pos--; pos >= 0; pos--) {
            cVal[pos] = cVal[pos+ 1] * ul.get(pos + 1);
            System.out.println("cVal[" + pos + "]" + " = " + cVal[pos]);
            c0 -= (cVal[pos] * ll.get(pos));
        }
        int ans = c0;
        for (int i = 0; i < refs.length; i++) {
            int ref = Integer.parseInt(refs[i]);
            ans += (cVal[i] * ref);
        }
        return ans;
    }
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String[] tokens = scan.nextLine().trim().split("\\s+");
        int n = Integer.parseInt(tokens[0]);
        int r = Integer.parseInt(tokens[1]);
        Hashtable<String, String> ht = new Hashtable<String, String>();
        for (int i = 0; i < n; i++) {
            ht.put(scan.next().trim(), scan.nextLine().trim());
        }
        StringBuffer output;
        for (int i = 0; i < r; i++) {
            output = new StringBuffer();
            String arrName = scan.next().trim();
            tokens = scan.nextLine().trim().split("\\s+");
            output.append(arrName + "[");
            for(int j = 0; j < tokens.length-1; j++) {
                output.append(tokens[j] + ", ");
            }
            int ans = findPhysicalAddress(ht.get(arrName).split("\\s+"), tokens);
            output.append(tokens[tokens.length-1] + "] = " + ans);
            System.out.println(output.toString());
        }
    }
}