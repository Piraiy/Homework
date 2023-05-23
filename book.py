f1, f2, f3 = open('1.txt', encoding='utf-8'), open('2.txt', encoding='utf-8'), open('3.txt', encoding='utf-8')

one = len(f1.readlines())
two = len(f2.readlines())
three = len(f3.readlines())

f1.close(), f2.close(), f3.close()
with open('1.txt', encoding='utf-8') as file_1, open('2.txt', encoding='utf-8') as file_2, open('3.txt',  encoding='utf-8') as file_3, open('result_book.txt', 'w', encoding='utf-8') as file_result:
    dict_len = {one: file_1,
            two: file_2,
            three: file_3
        }
    list_ = []
    for i in dict_len:
        list_.append(i)
        list_.sort()
    for j in list_:
        file_result.write(f'{dict_len.get(j).name}\n{j}\n{dict_len.get(j).read()}\n')
