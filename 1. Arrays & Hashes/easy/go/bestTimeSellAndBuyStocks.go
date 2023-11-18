func maxProfit(prices []int) int {
    var i, j int
    var maxProfit int
    for j < len(prices) {
        maxProfit = max(maxProfit, prices[j] - prices[i])
        if prices[j] - prices[i] < 0 {
            i = j
        }
        j++
    }
    return maxProfit
}