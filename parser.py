# -*- coding: utf8 -*-
from settings import *
from function import *

pd.set_option('display.max_columns', None)

nlp = spacy.load("ru_core_news_lg")

file_name="data/НСИ - закупки.xlsx"
rb = xlrd.open_workbook(file_name)
sheet = rb.sheet_by_index(1)

#Получаем список значений из всех записей
vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]


print_border('СИНТАКТИЧЕСКИЙ РАЗБОР SPACY')
text = []
for el in vals[1:]:
    el[1].replace('-', '')
    text.append(el[1].replace('\n', '').replace('-', '_'))
# print('text  -', text)
# print('len(text) -', len(text))
print_border('СОСТАВЛЕНИЕ ПРЕДЛОЖЕНИЙ')
test_text = reduce(lambda x, y: x + '. ' + y, text)

# print('test_text  -', test_text)
# print('type(test_text) -', type(test_text))

print_border('КОНЕЦ СИНТАКТИЧЕСКОГО РАЗБОРА SPACY')


#Создание словаря
def make_dict(array):
    dict_word = {}
    for el in array.split('.'):
        for symb in el.lower().split(' '):
            if symb not in dict_word.keys():
                if len(symb) > 3:
                    dict_word[symb] = [el + '.']
            else:
                dict_word[symb].append(el + '.')
    return dict_word



def change_list(array):
    dict_word = {}
    for el in array:
        # count_word = Counter(tmp)
        # # print(count_word)
        for symb in el.lower().split(' '):

            if symb.rstrip(".") not in dict_word.keys():
                if len(symb) > 3:
                    dict_word[symb.rstrip(".")] = [el]
            else:
                dict_word[symb.rstrip(".")].append(el)
    return dict_word


def change_list2(array):

    dict_word = {}
    for el in array:
        # count_word = Counter(tmp)
        # # print(count_word)
        for symb in el.lower().split(' '):

            if symb.rstrip(".") not in dict_word.keys():
                if len(symb) > 3:
                    dict_word[symb.rstrip(".")] = [el]
            else:
                dict_word[symb.rstrip(".")].append(el)
    return dict_word

# test_text = 'Дезинфицирующие салфетки для гигиенической обработки рук. Диспенсерная система с сухими салфетками. Дозатор. Жидкое мыло. Жидкое мыло антибактериальное. Кожный антисептик для гигиенической обработки рук. Кожный антисептик для обработки рук хирургов. Кожный антисептик окрашенный для операционного и инъекционного поля. Кондиционер для белья. Контроль качества предстерилизационной очистки изделий медицинского назначения. Контроль концентрации рабочего раствора ДС. Крем для рук. Обеззараживание медицинских отходов (объектов одноразового использования и биологического материала). Отбеливатель. Салфетки для обработки инъекционного поля. Сменный блок салфеток. Средство дезинфекции поверхностей (текущей и генеральных уборок, в том числе санитарно-технического оборудования). Средство для быстрой дезинфекции небольших поверхностей. Средство для ДВУ эндоскопов. Средство для дезинфекции белья ручным способом. Средство для дезинфекции и мытья посуды. Средство для дезинфекции ИМН, совмещенной с ПСО, ручным или механизированным способом. Средство для дезинфекции на пищеблоке. Средство для дезинфекции пищевого яйца. Средство для дезинфекции при особоопасных инфекциях. Средство для очистки воды бассейна. Средство для очистки медицинских изделий и эндоскопов на основе ферментов. Средство для химической стерилизации. Средство моющее для мытья посуды. Средство моющее для полов. Средство моющее для стекол. Средство чистящее для прочистки труб и канализации. Стиральный порошок.'
doc = nlp(test_text)

#Находим корневые существительные
def find_root_noun(text):
    set_root = set()
    for sent in doc.sents:
        for token in sent:
            if token.dep_ == 'ROOT' and token.pos_ == 'NOUN': #token.dep_ == 'ROOT' and token.pos_ == 'NOUN'
                # print(token.head.text, ' - ', token.dep_, ' - ', token.pos_, ' - ', token.text)
                set_root.add(token.text.lower())

    return set_root

#Находим корневыые прилагательные
def find_root_adj(text):
    set_root = set()
    for sent in doc.sents:
        for token in sent:
            if token.dep_ == 'ROOT' and token.pos_ == 'ADJ': #token.dep_ == 'ROOT' and token.pos_ == 'NOUN'
                # print(token.head.text, ' - ', token.dep_, ' - ', token.pos_, ' - ', token.text)
                set_root.add(token.text.lower())

    return set_root

#Находим корневыые прилагательные
def find_noun_adj(text):
    set_root = set()
    for sent in doc.sents:
        for token in sent:
            if token.dep_ == 'ROOT' and token.pos_ == 'NOUN': #token.dep_ == 'ROOT' and token.pos_ == 'NOUN'
                chunk = ''
                for w in token.children:
                    if w.dep_ == 'amod' or w.pos_ == 'ADJ':
                        chunk = chunk + w.text + ' '
                chunk = chunk + token.text
                set_root.add(chunk)

    return set_root




def make_dict_sent(array, root):
    dict_word = {}
    for token in root:
        for el in array.split('.'):
            for symb in el.lower().split(' '):
                if token == symb:
                    if token not in dict_word.keys():
                        dict_word[token] = [el.lstrip() + '.']
                    else:
                        dict_word[token].append(el.lstrip() + '.')
    return dict_word


def mix_noun_adj(text, list_adj):
    dict_word = {}
    for token in list_adj:
        for el in text.split('.'):
            for symb in el.lower().split(' '):
                if token == symb:
                    if token not in dict_word.keys():
                        dict_word[token] = [el.lstrip() + '.']
                    else:
                        dict_word[token].append(el.lstrip() + '.')
    return dict_word

#Находи корни существительные в предложении
set_root_noun = find_root_noun(test_text)
# print(set_root_noun)
# print(len(set_root_noun))

#Находи корни прилагательные в предложении
set_root_adj = find_root_adj(test_text)
# print(set_root_adj)
# print(len(set_root_adj))


set_noun_adj = find_noun_adj(test_text)
for el in set_noun_adj:
    if len(el.split(" ")) > 1:
        print(el)
# print(set_noun_adj)
# print(len(set_noun_adj))


#Создаем словарь существительных в предложении
dict_noun = make_dict_sent(test_text, list(set_root_noun))
# print(dict_noun)
# print(len(dict_noun))

#Создаем словарь прилагательных в предложении
dict_adj = make_dict_sent(test_text, list(set_root_adj))
# print(dict_adj)
# print(len(dict_adj))

# #Существительное + прилагательное
# noun_adj_dict = {}
# for key, value in dict(sorted(dict_noun.items(), key=lambda x: len(x[1]), reverse=False)).items():
#     if len(mix_noun_adj(" ".join(value), list(set_root_adj))) != 0:
#         noun_adj_dict[key] = mix_noun_adj(" ".join(value), list(set_root_adj))
#
#
# for k, v in dict(sorted(noun_adj_dict.items(), key=lambda x: len(x[1]), reverse=False)).items():
#     # print(k, ' - ', len(v), ' - ', v)
#     tree = Tree()
#     tree.create_node(k.title(), k)  # root node
#     for key, value in v.items():
#         tree.create_node(k.title() + " " + key, key, parent=k)
#         for token in value:
#             tree.create_node(token, parent=key)
#     tree.show()
#
#
# # Прилагательное + Существительное
# adj_noun_dict = {}
# for key, value in dict(sorted(dict_adj.items(), key=lambda x: len(x[1]), reverse=False)).items():
#     if len(mix_noun_adj(" ".join(value), list(set_root_noun))) != 0:
#         adj_noun_dict[key] = mix_noun_adj(" ".join(value), list(set_root_noun))
#
#
# for k, v in dict(sorted(adj_noun_dict.items(), key=lambda x: len(x[1]), reverse=False)).items():
#     # print(k, ' - ', len(v), ' - ', v)
#     tree = Tree()
#     tree.create_node(k.title(), k)  # root node
#     for key, value in v.items():
#         tree.create_node(k.title() + " " + key, key, parent=k)
#         for token in value:
#             tree.create_node(token, parent=key)
#     tree.show()