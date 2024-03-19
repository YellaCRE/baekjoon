// 2665번 미로만들기
const fs = require('fs');
const filePath = process.platform === "linux" ? "dev/stdin" : "test.txt"
const stdin = fs.readFileSync(filePath).toString().trim().split("\n")
// console.log(stdin)

const n = Number(stdin.shift())
// console.log(n)

const dr = [1, 0, -1, 0]
const dc = [0, 1, 0, -1]
const visited = Array(n)
for (let i = 0; i<n; i++){
    visited[i] = Array(n).fill(0)
}
// console.log(visited)

const BFS = () => {
    let q = []
    q.push([[0, 0], 0])
    visited[0][0] = 1

    while (q){
        let [[currentRow, currentCol], count] = q.shift()

        for (let i = 0; i < 4; i++){
            let nextRow = currentRow + dr[i]
            let nextCol = currentCol + dc[i]
            if (nextRow === n-1 && nextCol === n-1) return count;

            if (nextRow < 0 || n <= nextRow || nextCol < 0 || n <= nextCol) continue;
            if (visited[nextRow][nextCol] === 1) continue

            visited[nextRow][nextCol] = 1
            if (stdin[nextRow][nextCol] === '0'){
                q.push([[nextRow, nextCol], count+1])
            } else {
                q.unshift([[nextRow, nextCol], count])
            }
        }
    }
}

console.log( BFS() )