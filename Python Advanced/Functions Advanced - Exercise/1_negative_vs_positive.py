def negative_vs_positive(*lst_with_numbers):
    positive_sum = 0
    negative_sum = 0
    for number in lst_with_numbers:
        if number > 0:
            positive_sum += number
        else:
            negative_sum += number

    return positive_sum, negative_sum
numbers = [int(num) for num in input().split()]

pos_sum, neg_sum = negative_vs_positive(*numbers)
print(neg_sum)
print(pos_sum)

if pos_sum > abs(neg_sum):
    print("The positives are stronger than the negatives")
else:
    print("The negatives are stronger than the positives")
