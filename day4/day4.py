import pathlib


root_path = pathlib.Path(__file__).parent.resolve()
filename = 'input.txt'
# print((pathlib.Path(__file__).parent).joinpath(filename))
with open((pathlib.Path(__file__).parent).joinpath(filename)) as file:
    data = file.read().splitlines()


def calculate_pair_ranges(pair:str):
    start, end = pair.split('-')
    return [i for i in range(int(start), int(end)+1)]

total_overlapping_sections = 0
for sections in data:
    pairs = sections.split(',')
    pair_ranges = [calculate_pair_ranges(pair) for pair in pairs]
    if all(x in pair_ranges[1] for x in pair_ranges[0]) or all(x in pair_ranges[0] for x in pair_ranges[1]):
        total_overlapping_sections += 1
    

print(f"Total Overlapping Sections: {total_overlapping_sections}")

overlapping_sections = 0
for sections in data:
    pairs = sections.split(',')
    pair_ranges = [calculate_pair_ranges(pair) for pair in pairs]
    if len(set(pair_ranges[0]) & set(pair_ranges[1])):
        print(pair_ranges)
        overlapping_sections += 1
    

print(f"Overlapping Sections: {overlapping_sections}")
