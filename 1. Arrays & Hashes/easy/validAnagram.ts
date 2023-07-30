// https://leetcode.com/problems/valid-anagram/
// 1 <= s.length, t.length <= 5 * 10^4
function isAnagram(s: string, t: string): boolean {
    s = s.split("").sort().join("")
    t = t.split("").sort().join("")
    return s === t
};

// Time O(nlog(n))
// Space O(1)

console.log(isAnagram("", "r"))
console.log(isAnagram("cat", "rat"))
console.log(isAnagram("anagram", "nagaram"))