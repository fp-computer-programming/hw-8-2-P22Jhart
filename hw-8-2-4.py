def letter (word,letter):
    amount=0
    for x in word:
        if x == letter:
            amount += 1
        return amount

letter("cat", "t") == 1
letter("apple", "p") == 2
letter("supercalifragilisticexpialidocious", "i") == 7