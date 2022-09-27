names = [
    'Paweł', 'Kewin', 'Ireneusz', 'Bolesław', 'Mateusz', 'Edward', 'Piotr',
    'Jan', 'Denis', 'Amir', 'Igor', 'Borys', 'Robert', 'Ariel', 'Kuba',
    'Rafał', 'Mateusz', 'Emanuel', 'Alfred', 'Artur', 'Jakub', 'Ludwik',
    'Bolesław', 'Remigiusz', 'Martin', 'Dobromił', 'Mariusz', 'Amadeusz',
    'Łukasz', 'Bolesław', 'Amir', 'Artur', 'Albert', 'Olgierd', 'Alek',
    'Kordian', 'Julian', 'Anastazy', 'Emanuel', 'Józef'
]

name_dict = {}
initial = set()

for name in names:
    initial.add(name[0])  #zrób set (lista bez powtórzeń) pierwszych liter

initial = list(initial)  #z seta listę zróbmy
list_of_sets = [
    set() for i in range(len(initial))
]  #robimy listę list, która ma tyle list w sobie, co jest pierwszych literek

for i in range(len(initial)):
    for name in names:
        if name[0] == initial[i]:
            list_of_sets[i].add(name)

name_dict = zip(initial, list_of_sets)
print(list(name_dict))

name_dict = {}
print('''


''')

for name in names:
    v = name_dict.setdefault(name[0], set())
    # v.add(name)
    v = v | {name}
    name_dict[name[0]] = v


print(name_dict["A"])
