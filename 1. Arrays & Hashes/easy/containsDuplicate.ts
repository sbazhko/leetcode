// https://leetcode.com/problems/contains-duplicate/

function containsDuplicate(nums: number[]): boolean {
    let seenNums = new Set<number>()
    for(let i = 0; i < nums.length; i++) {
        if(!seenNums.has(nums[i])) {
            seenNums.add(nums[i])
        } else {
            return true
        }
    }
    return false
};

console.log(containsDuplicate([1]))
console.log(containsDuplicate([]))
console.log(containsDuplicate([1,1,2]))
console.log(containsDuplicate([1,2,3]))

// Time O(n)
// Space O(n)