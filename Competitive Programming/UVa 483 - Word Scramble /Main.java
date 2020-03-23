import java.util.Scanner;

public class Main {
    public static void main(String args[]) {
        Scanner scan = new Scanner(System.in);
        String str;
        while(scan.hasNext()) {
            str=scan.nextLine();
            String[] tokens=str.split(" ");
            for(int i=0;i<tokens.length;i++) {
                StringBuffer tmp1=new StringBuffer(tokens[i]);
                if(i==tokens.length -1) {
                    System.out.print(tmp1.reverse().toString());
                    break;
                }
                tmp1.reverse().toString();
                System.out.print(tmp1+" ");
            }
            for (int i = str.length()-1; i >= 0; i--) {
                if (str.charAt(i) == ' ') {
                    System.out.print(' ');
                } else {
                    break;
                }
            }
            System.out.println();
        }
    }
}