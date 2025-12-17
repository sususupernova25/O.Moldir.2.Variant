s = input()
vowels = 'aeiouAEIOU'
count = sum(1 for c in s if c in vowels)
print(count)