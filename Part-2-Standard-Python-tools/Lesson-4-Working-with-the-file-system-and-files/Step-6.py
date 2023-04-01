# Вам дана в архиве (ссылка) файловая структура, состоящая из директорий и файлов.
#
# Вам необходимо распаковать этот архив, и затем найти в данной в файловой структуре все директории, в которых есть хотя бы один файл с расширением ".py".
#
# Ответом на данную задачу будет являться файл со списком таких директорий, отсортированных в лексикографическом порядке.
#
# Для лучшего понимания формата задачи, ознакомьтесь с примером.
# Пример архива: https://stepik.org/media/attachments/lesson/24465/sample.zip
# Пример ответа: https://stepik.org/media/attachments/lesson/24465/sample_ans.txt


import os
import os.path
with open('rez.txt', 'w') as rezFile:
    for currentDir, dirs, files in os.walk('main'):
        for tmpFile in files:
            if tmpFile.endswith('.py'):
                rezFile.write(currentDir)
                rezFile.write('\n')
                break
