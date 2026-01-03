with open("05.txt", encoding="utf-8") as f:
    puzzle_input = f.read().strip()

date_ranges, products = puzzle_input.split("\n\n")
date_ranges = [
    range(int(s), int(e) + 1)
    for line in date_ranges.splitlines()
    for s, e in [line.split("-")]
]
products = [int(i) for i in products.splitlines()]

fresh_products_count_pt1 = 0
for product in products:
    if any(product in date_range for date_range in date_ranges):
        fresh_products_count_pt1 += 1

print(fresh_products_count_pt1)

        
date_ranges.sort(key=lambda x: x.start)

merged_date_ranges = [date_ranges[0]]
for current in date_ranges[1:]:
    last = merged_date_ranges[-1]
    
    if current.start <= last.stop:
        # extend last range
        merged_date_ranges[-1] = range(last.start, max(last.stop, current.stop))
    else:
        # append new range
        merged_date_ranges.append(current)

fresh_products_count_pt2 = 0
for r in merged_date_ranges:
    fresh_products_count_pt2 += r.stop - r.start

print(fresh_products_count_pt2)
