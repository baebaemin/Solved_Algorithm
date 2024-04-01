function isPrime(num) {
    if (num <= 1) return false;
    if (num <= 3) return true;
    if (num % 2 === 0 || num % 3 === 0) return false;
    for (let i = 5; i * i <= num; i += 6) {
        if (num % i === 0 || num % (i + 2) === 0) return false;
    }
    return true;
}

function solution(n, k) {
    const convertedNum = n.toString(k)
    const splitedList = convertedNum.split('0')
    let answer = 0;
    splitedList.map(n => {
    if (isPrime(Number(n))) {
        answer++;
    }}
    )
    return answer
}