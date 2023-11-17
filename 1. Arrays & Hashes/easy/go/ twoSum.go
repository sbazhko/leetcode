func twoSum(nums []int, target int) []int {
    remainMap := make(map[int]int)
	for i, num := range nums {
		if j, ok := remainMap[num]; ok {
			return []int{i, j}
		}
		remainMap[target - num] = i
	}
}