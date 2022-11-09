import random

with open("normtext.txt", "r", encoding='utf-8') as f1:
    lines = f1.read()
ru_Down = list("абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz")
ru_Up = list("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯABCDEFGHIJKLMNOPQRSTUVWXYZ")
print(lines)
wordsPoints = lines.split(' ')
for ii, vv in enumerate(wordsPoints):
    wordsPoints[ii] = [vv]
for i1, v1 in enumerate(wordsPoints):
    check = True
    while check:
        check = False
        for i2, v2 in enumerate(wordsPoints[i1]):
            letters = list(v2)
            for i3, v3 in enumerate(letters):
                if (v3 == '\n' or v3 == '-' or v3 == '\t' or v3 == '#' or v3 == '(') and len(letters) != i3 + 1:
                    check = True
                    for ii, vv in enumerate(wordsPoints[i1]):
                        wordsPoints[i1][ii] = [vv]
                    wordsPoints[i1][i2] = ["".join(letters[:i3 + 1]), "".join(letters[i3 + 1:])]
                    wordsPoints[i1] = sum(wordsPoints[i1], [])
                    break
wordsPoints = sum(wordsPoints, [])
print(1, wordsPoints)
for index, word in enumerate(wordsPoints):
    count = 0
    for letter in word:
        if letter in ru_Up or letter in ru_Down:
            count += 1
    if count >= 4:
        center = list(word[1:count - 1])
        random.shuffle(center)
        temp = list(word[1:count - 1])
        while True:
            spec_count = 0
            for index_center, letter_temp in enumerate(temp):
                if letter_temp == center[index_center]:
                    spec_count += 1
            if spec_count == count - 2:
                random.shuffle(center)
            else:
                break
        wordsPoints[index] = word[0] + "".join(center) + word[count - 1:]
    else:
        continue
print(2, wordsPoints)
last_simb = 0
end = wordsPoints[0]
for i1, v1 in enumerate(wordsPoints):
    if v1[len(v1) - 1] == '-' or v1[-1] == '\n' or v1[-1] == '\t' or v1[-1] == '#' or v1[-1] == '(':
        if i1 < len(wordsPoints) - 1:
            end = end + wordsPoints[i1 + 1]
        else:
            break
    else:
        if i1 < len(wordsPoints) - 1:
            end = end + ' ' + wordsPoints[i1 + 1]
        else:
            break
print(f"\n{end}")
with open("izmentext.txt", "w", encoding='utf-8') as f2:
    f2.write(end)
