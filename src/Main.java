package src;
// 10815번 숫자 카드
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());
        StringTokenizer stN = new StringTokenizer(br.readLine());
        ArrayList<Integer> nCards = new ArrayList<>();
        for (int i = 0; i<N; i++){
            nCards.add(Integer.parseInt(stN.nextToken()));
        }
        Collections.sort(nCards);

        int M = Integer.parseInt(br.readLine());
        StringTokenizer stM = new StringTokenizer(br.readLine());
        ArrayList<Integer> mCards = new ArrayList<>();
        for (int i = 0; i<M; i++){
            mCards.add(Integer.parseInt(stM.nextToken()));
        }

        for (int card : mCards){
            sb.append(bisect(card, N-1, nCards));
            sb.append(" ");
        }
        System.out.print(sb);
    }

    public static int bisect(int card, int N, ArrayList<Integer> cards){
        int left = 0;
        int right = N;
        int mid;

        while (left <= right){
            mid = (left + right) / 2;
            if (card == cards.get(mid)){
                return 1;
            }

            if (card < cards.get(mid)){
                right = mid-1;
            } else {
                left = mid+1;
            }
        }
        return 0;
    }
}