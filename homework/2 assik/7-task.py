items = input().split()

# count freq
freq = {}
i = 0
while i < len(items):
    item = items[i]
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1
    i += 1

# output freq
print("Purchase frequency:")
keys = list(freq.keys())
i = 0
while i < len(keys):
    item = keys[i]
    print(item + ":", freq[item])
    i += 1

# popular product
keys = list(freq.keys())
max_item = keys[0]
i = 1
while i < len(keys):
    if freq[keys[i]] > freq[max_item]:
        max_item = keys[i]
    i += 1

print()
print("Most popular item:", max_item)

# product once
once = []
keys = list(freq.keys())
i = 0
while i < len(keys):
    if freq[keys[i]] == 1:
        once.append(keys[i])
    i += 1

print()
print("Purchased once:", " ".join(once))

# bubble sort
sorted_items = list(freq.items())
i = 0
while i < len(sorted_items):
    j = 0
    while j < len(sorted_items) - 1:
        if sorted_items[j][1] < sorted_items[j + 1][1]:
            sorted_items[j], sorted_items[j + 1] = sorted_items[j + 1], sorted_items[j]
        j += 1
    i += 1

print()
print("Sorted by frequency:")
i = 0
while i < len(sorted_items):
    print(sorted_items[i][0], sorted_items[i][1])
    i += 1