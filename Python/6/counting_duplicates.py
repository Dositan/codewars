
def duplicate_count(text):
    duplicates = []
    for x in text.lower():
        if (cnt := text.count(x)) > 1:
            duplicates.append(cnt)

    return 0 if not duplicates else min(duplicates)


print(duplicate_count('Indivisibilities'))
