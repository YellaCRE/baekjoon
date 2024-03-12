// 2577번 숫자의 개수
const solution = () => {
    const file = process.platform === "linux" ? "dev/stdin" : "test.txt";
    let input = require('fs').readFileSync(file).toString().trim().split('\n')
    let res = input[0] * input[1] * input[2]
    let count_list = res
        .toString()
        .split('')
        .reduce((acc, ele) => {
            acc[ele] = (acc[ele]||0) + 1
            return acc
        }, {})

    for (let i = 0; i<10; i++){
        console.log(count_list[i] ? count_list[i] : 0)
    }
}

solution()
