s = input()
words = s.split()

for w in words:
    if w.endswith("I"):
        print(w)
