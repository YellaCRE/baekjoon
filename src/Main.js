// 9020번 골드바흐의 추측
const Cyrene = (n, m) => {
    let prime = []
    for (let i = n; i<=m; i++){
        prime[i] = i;
    }
    for (let i = 2; i<=m; i++){
        if (prime[i]===0) continue;
        for (let j= i + i; j<=m; j+=i){
            prime[j] = 0
        }
    }
    prime = prime.filter(n => n !== 0)

    return prime;
}

const solution = () => {
    const file = process.platform === "linux" ? "dev/stdin" : "test.txt";
    const input = require('fs').readFileSync(file).toString().trim().split('\n');

    const n = 2;
    const m = 10000;
    let prime = Cyrene(n, m)

    for (let i = 0; i < input.length; i++){
        const num = Number(input[i]);
        let answer = [];

        for (let j = 0; prime[j] < num/2 + 1; j++) {
            const index = prime.indexOf(num - prime[j])

            if (index !== -1) {
                answer.push([prime[j], prime[index]])
            }
        }

        if (answer.length !== 0){
            const a = answer.pop();
            console.log(`${a[0]} ${a[1]}`);
        }
    }
}

solution()
