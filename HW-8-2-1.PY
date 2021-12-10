def count_odds(lst):
odd = 0
for odd in lst:
    if odd % 2 ! = 0:
        odd += 1
return odd

print(count_odds([1, 2, 3, 4, 5, 6]) == 3)
print(count_odds([1, 3, 5, 7, 9]) == 5)
print(count_odds([2, 4, 6, 8, 10]) == 0)