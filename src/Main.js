// 11050번 이항 계수 1
const solution = () => {
    let [N, K] = require('fs').readFileSync('/dev/stdin').toString().trim().split(' ').map(Number)
    let numerator = 1;   // 분자
    let denominator = 1; // 분모

    for (let i = 0; i < K; i++) {
        numerator *= N - i;
        denominator *= K - i;
    }

    console.log(numerator / denominator);
}

solution()
