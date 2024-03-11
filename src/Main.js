// 10816번 숫자 카드 2
const solution = () => {
    const file = process.platform === "linux" ? "dev/stdin" : "test.txt";
    let input = require('fs').readFileSync(file).toString().trim().split('\n')

    let cards = input[1]
        .split(' ')
        .map(Number)
        .reduce((dict, num) => {
            dict[num] = (dict[num]||0) + 1
            return dict
        }, {})

    let cardCount = input[3]
        .split(' ')
        .map(Number)
        .map((num) => {
            return cards[num] ? cards[num] : 0
        })
        .join(' ')

    console.log(cardCount)
}

solution()
