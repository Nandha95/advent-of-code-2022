import pathlib
import string
import textwrap

root_path = pathlib.Path(__file__).parent.resolve()
filename = 'input.txt'
# print((pathlib.Path(__file__).parent).joinpath(filename))
with open((pathlib.Path(__file__).parent).joinpath(filename)) as file:
    data = file.read().splitlines()

def divide_chunks(l, n):
     
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]

priority = dict(zip(string.ascii_letters, range(1, len(string.ascii_letters)+1)))
priority_sum = 0

for bag in data:
    print(len(bag))
    mid = int(len(bag)/2)
    compartments = [bag[i:i+int(mid)] for i in range(0, len(bag), int(mid))]
    common_elements = list(set(compartments[0]) & set(compartments[1]))
    priority_score = sum(list(map(priority.get, common_elements)))
    priority_sum += priority_score


print(f"sum of the priorities of those item types: {priority_sum}")

groups = list(divide_chunks(data, 3))
group_priority_sum = 0
for group in groups:
    common_elements = list(set(group[0]) & set(group[1]) & set(group[2]))
    priority_score = sum(list(map(priority.get, common_elements)))
    group_priority_sum += priority_score

print(f"Sum of the priorities of groups: {group_priority_sum}")