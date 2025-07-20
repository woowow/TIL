import java.util.Scanner;
import java.io.FileInputStream;

class Solution
{
	public static void main(String args[]) throws Exception
	{
        Scanner sc = new Scanner(System.in);
        
        int N = sc.nextInt();
        
        boolean check = true;
        int sum = 0;
        
        while(check==true){
            if (N>10){
                sum += (N%10);
                N = N/10;
            }
            else{
                sum += N;
                check = false;
            }
        }
        System.out.println(sum);
    
	}
}