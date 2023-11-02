function getSum(a: number, b: number): number {
    let sum = a
    while (b != 0) {
        const tmp = (sum & b) << 1
        sum = sum ^ b
        b = tmp 
    }
    return sum
}
