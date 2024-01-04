package src;
// 2231번 분해합
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int res = 0;

        for (int i = N; i > 0; i--){
            int div = 1;
            int temp = i;
            while (div <= i){
                temp += i%(div*10)/div;
                div *= 10;
            }
            if (temp == N)
                res = i;
        }

        System.out.print(res);
    }
}