N = int(input())
nums = list(map(int, input().split()))
nums_set = set(nums)

print("YES" if len(nums) == len(nums_set) else "NO")
