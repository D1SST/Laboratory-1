print("Введите количество цифр, которое натуральное число не должно превышать: ")
K = int(input())

with open("rand.txt") as f:
    s = f.read()
    l = len(s)
    sequence = []
    i = 0
    while i < l:
        s_int = ''
        a = s[i]
        while '0' <= a <= '9':
            s_int += a
            i += 1
            if i < l:
                a = s[i]
            else:
                break
        i += 1
        if s_int != '':
            sequence.append(int(s_int))

numbers_dict = {"0": "ноль ", "1": "один ", "2": "два ", "3": "три ", "4": "четыре ", "5": "пять ", "6": "шесть ", "7": "семь ", "8": "восемь ", "9": "девять "}

def multiple_replace(target_str, replace_values):
    for i, j in replace_values.items():
        target_str = target_str.replace(i, j)
    return target_str

for i in range(len(sequence)):
    if (sequence[i] != 0) and (sequence[i] % 2 == 0) and (len(str(sequence[i])) <= K):
        if (i % 2 != 0):
            sequence[i] = multiple_replace(str(sequence[i]), numbers_dict)
            print(sequence[i], "| индекс числа -", i)

        else:
            print(sequence[i], "| индекс числа -", i)
        i += 1