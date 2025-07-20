import java.util.Scanner;
import java.io.FileInputStream;


class Solution{
    public static void main(String args[]){
        
        Scanner sc = new Scanner(System.in);

            int a = sc.nextInt();
            int b = sc.nextInt();

            if((a == 1 && b == 2) || (a == 2 && b == 3) || (a == 3 && b == 1)) {
                System.out.print("B");
        	}
            else{
                System.out.print("A");
            }
        sc.close();
    }
}
