
vowels = {
    "a": 1,
    "e": 2,
    "i": 3,
    "o": 4,
    "u": 5,
}
sum = 0

for char in input():
    if char in 'aeiou':
        sum += vowels[char]

print(sum)