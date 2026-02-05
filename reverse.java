import java.util.*;
public class reverse{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number");
        int n = sc.nextInt();
        int revNum = 0;
        while(n>0){
            int ld = n%10;
            revNum = (revNum*10) + ld;
            n = n/10;
        }
        System.out.println("Reverse = " + revNum);
    }
}