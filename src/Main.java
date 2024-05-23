package src;
// 2239번 스도쿠
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.*;

public class Main {
    static int[][] graph = new int[9][9];
	static boolean flag = false;
    public static void main(String[] args) throws IOException {
		BufferedReader br  = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		for(int i=0;i<9;i++) {
			char[] c = br.readLine().toCharArray();
			for(int j=0;j<9;j++) {
				graph[i][j] = c[j]-'0';
			}
		}

		solveSudoku(0);

        for(int[] a : graph) {
			for(int b : a) {
				sb.append(b);
			}
			sb.append("\n");
		}

		System.out.println(sb);
    }

	static void solveSudoku(int idx) {
		if (idx == 81){
			flag = true;
			return;
		}

		int r = idx / 9;
		int c = idx % 9;

		if (graph[r][c] != 0) {
			solveSudoku(idx + 1);
		}
		else {
			for (int nxtNum = 1; nxtNum < 10; nxtNum++) {
				// 만약 적절하지 않다면 continue
				if (!isValid(r, c, nxtNum)) continue;

				graph[r][c] = nxtNum;
				solveSudoku(idx + 1);
				if (flag) return;
				graph[r][c] = 0;
			}
		}
	}

	static boolean isValid(int row, int col, int num) {
		// 가로
		for (int i = 0; i < 9; i++){
			if (graph[row][i] == num) return false;
		}

		// 세로
		for (int i = 0; i < 9; i++){
			if (graph[i][col] == num) return false;
		}

		// 정사각형
		int box_row = (row / 3) * 3;
		int box_col = (col / 3) * 3;
		for (int i = box_row; i < box_row+3; i++){
			for (int j = box_col; j < box_col+3; j++){
				if (graph[i][j] == num) return false;
			}
		}

		return true;
	}
}