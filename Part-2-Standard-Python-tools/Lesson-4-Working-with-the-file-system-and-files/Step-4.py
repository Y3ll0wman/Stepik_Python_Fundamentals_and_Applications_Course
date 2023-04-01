# Вам дается текстовый файл, содержащий некоторое количество непустых строк.
# На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном порядке.
#
# Пример входного файла:
# ab
# c
# dde
# ff
#
# Пример выходного файла:
# ff
# dde
# c
# ab


listTmp = []
with open('dataset_24465_4.txt') as r:
    for line in r:
        line = line.strip()
        listTmp.append(line)
listTmp.reverse()
with open('w.txt', 'w') as w:
    w.write('\n'.join(listTmp))
    