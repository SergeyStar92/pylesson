def krypt(n, m):
    n = n.lower()
    alf = 'яабвгдеёжзийклмнопрстуфхцчшщьыъэюяа'
    res = []
    for i in n:
        if i in alf:
            conv = alf[alf.find(i) + m]
            res.append(conv.upper())

        if i in ' ':
            res.append(i)
        if i in '!?.,-_/*-+=0123456789':
            res.append(i)

    return ''.join(res)



# def ankrypt(n, m):
#     n = n.lower()
#     alf = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя'
#     res = []
#     for i in n:
#         if i in alf:
#             conv = alf[alf.find(i) + m]
#             res.append(conv.upper())
#
#         if i in ' ':
#             res.append(i)
#
#     return ''.join(res)

# text = input()
# sdvig = int(input())
# krypt(text, sdvig)
#
# textc = input()
# sdvigc = int(input())
# ankrypt(textc, sdvigc)