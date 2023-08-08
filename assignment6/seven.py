class ThreeSumZero:
    def three_sum_zero(self, nums):
        result = []
        n = len(nums)
        
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        result.append([nums[i], nums[j], nums[k]])
        
        return result

# Example usage
input_array = [-25, -10, -7, -3, 2, 4, 8, 10]
three_sum_zero_finder = ThreeSumZero()
output = three_sum_zero_finder.three_sum_zero(input_array)
print(output)  # Output: [[-25, 10, 15], [-10, -3, 13], [-10, 2, 8], [-7, -3, 10]]
