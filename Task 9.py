M = list("ой, влезай - убьет")
def zabor(M):
    f = 0
    for i in range(0, len(M)):
        if M[i].isalpha():
            if (f% 2):
                M[i] = M[i].lower()
            else:
                M[i] = M[i].upper()
            f = f + 1
            print (f%2)
    return
zabor(M)
print (M)