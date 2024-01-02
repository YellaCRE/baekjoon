package src;
// 1269번 대칭 차집합
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int cntA = Integer.parseInt(st.nextToken());
        int cntB = Integer.parseInt(st.nextToken());

        Set<Integer> setA = new HashSet<>();
        Set<Integer> setB = new HashSet<>();

        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < cntA; i++) {
            setA.add(Integer.parseInt(st.nextToken()));
        }
        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < cntB; i++) {
            setB.add(Integer.parseInt(st.nextToken()));
        }

        int result = count(setA, setB) + count(setB, setA);
        System.out.print(result);
    }

    public static int count(Set<Integer> a, Set<Integer> b){
        Set<Integer> temp = new HashSet<>(a);
        temp.removeAll(b);
        return temp.size();
    }
}