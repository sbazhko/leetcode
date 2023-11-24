func kthFactor(n int, k int) int {
    // n = a * b
    // b = n / a
    // n = a * n / a
    // find max a*a, such that a < n
    // find all n/a guys

    d := 1
    for ; d * d <= n; d++ { // all divisors < sqrt(n), since ceil(sqrt(n)) * ceil(sqrt(n)) > n
        if n % d == 0 {
            k--;
            if k == 0 {
                return d
            }
        }
    }
    // if the pair to the lower counterpart is higher
    for d = d - 1; d > 0; d-- {
        // skip because we accounted for that in the first loop
        if d * d == n {
            continue;
        }
        if n % d == 0 {
            k--;
            if k == 0 {
                return n / d
            }
        }
    }
    return -1
}