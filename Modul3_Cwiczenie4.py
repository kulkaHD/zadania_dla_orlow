dice = {}

# for name in names:
#     v = name_dict.setdefault(name[0], set())
#     v.add(name)
#     name_dict[name[0]] = v
print('''

''')

rzuty = set()

for i in range(1, 7):
    for j in range(1, 7):
        suma = (i + j)
        rzuty = i, j
        v = dice.setdefault(suma, set())
        v.add(rzuty)
        dice[suma] = v

print(dice)
print('''

''')
print(dice[7])
