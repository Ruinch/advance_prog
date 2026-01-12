def eq_list(strings):
    max_len = 0
    for s in strings:
        if len(s) > max_len:
            max_len = len(s)

    result = []
    for s in strings:
        diff = max_len - len(s)
        result.append(s + "_" * diff)

    return result

print(eq_list(["a", "bb", "ccc"]))