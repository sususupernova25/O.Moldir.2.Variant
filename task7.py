numbers = list(map(int, input().split()))
result = [numbers[0]] if numbers else []

for i in range(1, len(numbers)):
    if numbers[i] != numbers[i - 1]:
        result.append(numbers[i])

print(*result)