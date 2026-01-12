# open file and read lines
with open("text.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

# count num of lines
line_count = len(lines)

word_count = 0
freq = {}

i = 0
while i < len(lines):
    line = lines[i].lower()

    # delete , by hands
    clean_line = ""
    j = 0
    while j < len(line):
        ch = line[j]
        if ch.isalpha() or ch == " ":
            clean_line = clean_line + ch
        j = j + 1

    words = clean_line.split()

    k = 0
    while k < len(words):
        word = words[k]
        word_count = word_count + 1

        if word in freq:
            freq[word] = freq[word] + 1
        else:
            freq[word] = 1

        k = k + 1

    i = i + 1


# write results in file
with open("analysis.txt", "w", encoding="utf-8") as f:
    f.write("Total lines: " + str(line_count) + "\n")
    f.write("Total words: " + str(word_count) + "\n")
    f.write("Word frequency:\n")

    keys = list(freq.keys())
    i = 0
    while i < len(keys):
        word = keys[i]
        f.write(word + ": " + str(freq[word]) + "\n")
        i = i + 1
