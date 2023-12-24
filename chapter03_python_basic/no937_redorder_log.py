def reorderLogFiles_my(logs):
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    let_sorted = sorted(letters, key=lambda x: (x.split()[1:], x.split()[0]))
    return let_sorted + digits

print(reorderLogFiles_my(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]))



