
def topKFrequentFunctionality(nums, k):
    values = {}
    for i in range(len(nums)):
        if nums[i] not in values:
            values[nums[i]] = 1
        else:
            values[nums[i]] += 1
    sorted_dict_desc = dict(sorted(values.items(), key=lambda item: item[1], reverse=True))
    answer = []
    for i in sorted_dict_desc:
        answer.append(i)
    return answer[0:k]

def main(nums, k):
    result = topKFrequentFunctionality(nums, k)
    print(f"Array: {nums}")
    print(f"K: {k}")
    print(f"Top {k} frequent elements: {result}")
    
    # Show frequency breakdown
    values = {}
    for num in nums:
        values[num] = values.get(num, 0) + 1
    sorted_dict_desc = dict(sorted(values.items(), key=lambda item: item[1], reverse=True))
    print("Frequency breakdown:")
    for num, freq in sorted_dict_desc.items():
        print(f"  {num}: {freq} times")

# EXAMPLE
# main([1, 1, 1, 2, 2, 3], 2)
# main([4, 1, -1, 2, -1, 2, 3], 2)
