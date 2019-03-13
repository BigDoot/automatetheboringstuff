def print_abacus(value):
    stringnum = list(str(value))
    while len(stringnum) < 11:
        stringnum.insert(0, '0')
    listy = ["|00000*****   |","|00000****   *|","|00000***   **|","|00000**   ***|","|00000*   ****|","|00000   *****|","|0000   0*****|","|000   00*****|","|00   000*****|","|0   0000*****|"]
    for digit in stringnum:
        print(listy[int(digit)])

print_abacus(1337)
print_abacus(0)
print_abacus(12345678)

