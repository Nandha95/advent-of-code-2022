import itertools


with open('a_input.txt') as file:
    data = file.read().splitlines()


# print(data)

'''
Part 1: Calculating the elf carrying the highest number of calories
'''
elfs = [list(y) for x,y in itertools.groupby(data, lambda z:z=='') if not x]

elf_sums = []

for elf in elfs:
    elf_sums.append(sum([int(x) for x in elf]))


elf_sums.sort(reverse=True)
print(f"Total Calories of elf with most calories: {max(elf_sums)}")


'''
Calculating the total calories of the top 3 elves
'''
print(elf_sums[:3])
print(f"Total Calories of top 3 elf with most calories: {sum(elf_sums[:3])}")