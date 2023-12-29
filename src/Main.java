package src;
// 11653번 소인수분해
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int primeNumber = 2;

        while (N > 1){
            if (N % primeNumber == 0) {
                N = N / primeNumber;
                System.out.println(primeNumber);
            }
            else{
                primeNumber++;
            }
        }
    }
}