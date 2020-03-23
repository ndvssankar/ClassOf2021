import java.util.Scanner;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int count = 0;
        while (scan.hasNext()) {
            String nameOfTheProposalSelected = "";
            double priceWithTheProposal = Double.MAX_VALUE;
            double compliance = Double.MIN_VALUE;
            int numberOfRequirements = scan.nextInt();
            int numberOfProposals = scan.nextInt();
            if (numberOfRequirements == 0 && numberOfProposals == 0) {
                break;
            }
            if (count != 0) {
                System.out.println();
            }
            scan.nextLine();
            ArrayList<String> reqList = new ArrayList<String>();
            for (int i = 0; i < numberOfRequirements; i++) {
                reqList.add(scan.nextLine());
            }
            String nameOfTheProposal = "";
            double price = 0;
            int numberOfRequirementsMet = -1;
            int nr = -1;
            for (int i = 0; i < numberOfProposals; i++) {
                nameOfTheProposal = scan.nextLine();
                price = scan.nextDouble();
                numberOfRequirementsMet = scan.nextInt();
                scan.nextLine();
                for (int j = 0; j < numberOfRequirementsMet; j++) {
                    scan.nextLine();
                }
                if (numberOfRequirementsMet > nr) {
                    priceWithTheProposal = price;
                    nr = numberOfRequirementsMet;
                    nameOfTheProposalSelected = new String(nameOfTheProposal);
                    // System.out.println("In 1: nr : " + nr +  " : " + nameOfTheProposalSelected);
                } else {
                    if (numberOfRequirementsMet == nr && price < priceWithTheProposal) {
                        priceWithTheProposal = price;
                        nr = numberOfRequirementsMet;
                        nameOfTheProposalSelected = new String(nameOfTheProposal);
                        // System.out.println("In 2: nr : " + nr +  " : " + nameOfTheProposalSelected);
                    }
                }
            }
            System.out.println("RFP #" + (++count));
            System.out.println(nameOfTheProposalSelected);
        }
    }
}