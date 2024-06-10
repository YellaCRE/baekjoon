package src;
// 1436번 영화감독 숌
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.*;

public class Main {
	static int N;
    public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());

		int num = 666;
		int idx = 0;
		while (true){
			if (Integer.toString(num).contains("666")){
				idx++;
			}
			if (idx == N){
				System.out.println(num);
				return;
			}
			num++;
		}
	}
}