func containsDuplicate(nums []int) bool {
    duplicates := make(map[int]struct{}{})
	for _, v:= range nums {
		if _, ok := duplicates[v]; ok {
			return true
		}
        duplicates[v] = struct{}{}
	}
	return false
}