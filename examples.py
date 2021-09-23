#задание 1
print(type(15*3))
print(type(15 / 3))
print(type(15 // 2))
print(type(15 ** 2))


#задание 2
word_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
word_list_new = list()
for word in word_list:
    tmp = word.replace('+', '').replace('-', '')
    if tmp.isdigit():
        word_list_new.append('"')
        if len(tmp) == 1:
            word_list_new.append(word[:len(word) - 1] + '0' + word[len(word) - 1:])
        else:
            word_list_new.append(word)
        word_list_new.append('"')
    else:
        word_list_new.append(word)
print(word_list_new)
res_str = ''
open_tap = False
for word in word_list_new:
    res_str += word
    if word != '"':
        res_str += ' '
    elif open_tap:
        res_str = res_str[:-2]
        res_str += '" '
        open_tap = False
    else:
        open_tap = True
print(res_str)

#задание 4

name_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for name in name_list:
    print('Привет, {0}!'.format(name.split(' ')[-1].capitalize()))


#задание 5

import random
random.seed()
price_list = list()
for i in range(10):
    price_list.append(random.randint(1, 9999) / 100)
# print(price_list)
price_list.sort()
# print(price_list)
price_list_rev = price_list.copy()
price_list_rev.sort(reverse=True)
# print(price_list_rev)
print('Отсортированный список цен')
for price in price_list:
    # print('{0} руб {1:02d} коп'.format(int(price // 1), int(round(price % 1, 2) * 100)))
    tmp = int(round(price % 1, 2) * 100)
    if tmp == 0:
        tmp = '00'
    elif tmp > 0 and tmp < 10:
        tmp = '0' + str(tmp)
    print('{0} руб {1} коп'.format(int(price // 1), tmp))
print('Обратно отсортированный список цен')
for price in price_list_rev:
    # print('{0} руб {1:02d} коп'.format(int(price // 1), int(round(price % 1, 2) * 100)))
    tmp = int(round(price % 1, 2) * 100)
    if tmp == 0:
        tmp = '00'
    elif tmp > 0 and tmp < 10:
        tmp = '0' + str(tmp)
    print('{0} руб {1} коп'.format(int(price // 1), tmp))