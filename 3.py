s = input()

vowels_lower = 'aeiou'
vowels_upper = 'AEIOU'

count_lower = 0
count_upper = 0

for char in s:
    if char in vowels_lower:
        count_lower += 1
    elif char in vowels_upper:
        count_upper += 1

print(f"Строчных гласных: {count_lower}")
print(f"Заглавных гласных: {count_upper}")
