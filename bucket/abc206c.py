N = int(input())
numbers = map(int, input().split())

n = len(list(numbers))
print(n * (n - 1) // 2)
