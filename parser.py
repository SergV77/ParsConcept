# -*- coding: utf8 -*-
from settings import *
from function import *
from itertools import *


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
    doc = nlp(text)
    for sent in doc.sents:
        for token in sent:
            if token.dep_ == 'ROOT' and token.pos_ == 'NOUN': #token.dep_ == 'ROOT' and token.pos_ == 'NOUN'
                # print(token.head.text, ' - ', token.dep_, ' - ', token.pos_, ' - ', token.text)
                set_root.add(token.text.lower())

    return set_root

#Находим корневыые прилагательные
def find_root_adj(text):
    set_root = set()
    doc = nlp(text)
    for sent in doc.sents:
        for token in sent:
            if token.dep_ == 'ROOT' and token.pos_ == 'ADJ': #token.dep_ == 'ROOT' and token.pos_ == 'NOUN'
                # print(token.head.text, ' - ', token.dep_, ' - ', token.pos_, ' - ', token.text)
                set_root.add(token.text.lower())

    return set_root

#Находим связанные с корневем прилагательные
def find_noun_adj(text):
    set_root = set()
    doc = nlp(text)
    for token in doc:
        if token.dep_ == 'ROOT' and token.pos_ == 'NOUN': #token.dep_ == 'ROOT' and token.pos_ == 'NOUN'
            chunk = ''
            # print('token -', token)
            for w in token.children:
                if w.dep_ == 'amod' or w.pos_ == 'ADJ':
                    chunk = chunk + w.text + ' '
            chunk = chunk + token.text
            set_root.add(chunk)

    return set_root

def find_adj(text):
    doc = nlp(text)
    for token in doc:
        if token.dep_ == 'ROOT' and token.pos_ == 'NOUN': #token.dep_ == 'ROOT' and token.pos_ == 'NOUN'
            chunk = [w.text for w in token.children if w.dep_ == 'amod' and w.pos_ == 'ADJ']
            if len(chunk) > 0:
                return chunk, token.text
        elif token.dep_ == 'ROOT' and token.pos_ == 'ADJ':
            chunk = [w.text for w in token.children if w.dep_ == 'amod' and w.pos_ == 'ADJ']
            if len(chunk) > 0:
                return chunk, token.text

        else:
            continue




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

def take_dict(array):
    tmp_dict = {}
    for el in array:
        tup_el = find_adj(el)
        if tup_el:
            list_adj, root = tup_el
            if len(list_adj) > 1:
                for word in list_adj:
                    if word.lower() + ' ' + root not in tmp_dict.keys():
                        tmp_dict[word.lower() + ' ' + root] = [el]
                    else:
                        tmp_dict[word.lower() + ' ' + root].append(el)
            elif len(list_adj) == 1:
                if list_adj[0].lower() + ' ' + root not in tmp_dict.keys():
                    tmp_dict[list_adj[0].lower() + ' ' + root] = [el]
                else:
                    tmp_dict[list_adj[0].lower() + ' ' + root].append(el)
            else:
                continue

    return tmp_dict

#Формируем рекурсивно слвоарь словаре
def make_recurs_dict(dict_item):
    word_comb = {}
    for key, value in dict_item.items():
        if type(value) == dict:
            make_recurs_dict(value)

        elif type(value) == list:
            if len(value) > 2:
                word_comb[key] = take_dict(value)
            else:
                word_comb[key] = value
        else:
            continue

    return word_comb



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

tmp_list = []
tmp_dict = {}
tmp_set = set()

for el in set_noun_adj:
    if len(el.split(" ")) > 1:
        if len(el.lower().split(" ")) > 2:
            tmp_list.extend(el.lower().split(" "))
        # com_set = itertools.combinations(el.lower().split(" "), 2)
        tmp_set = set(tmp_list)
        com_set = itertools.combinations(tmp_set, 2)
        # print(el)
        # print(tmp_list)
        # print(list(com_set))
# print(set_noun_adj)
# print(len(set_noun_adj))
# print(len(tmp_list))
# print(len(tmp_set))

#Создаем словарь существительных в предложении
dict_noun = make_dict_sent(test_text, list(set_root_noun))
# print(dict_noun)
# print(len(dict_noun))

#Создаем словарь прилагательных в предложении
dict_adj = make_dict_sent(test_text, list(set_root_adj))
# print(dict_adj)
# print(len(dict_adj))

# #Существительное + прилагательное
noun_adj_dict = {}
for key, value in dict(sorted(dict_noun.items(), key=lambda x: len(x[1]), reverse=False)).items():
    if len(mix_noun_adj(" ".join(value), list(set_root_adj))) != 0:
        noun_adj_dict[key] = mix_noun_adj(" ".join(value), list(set_root_adj))


itog_dict = {}
for k, v in dict(sorted(noun_adj_dict.items(), key=lambda x: len(x[1]), reverse=False)).items():
    # print(k, ' - ', len(v), ' - ', v)

    itog_dict[k] = make_recurs_dict(v)


for key, value in itog_dict.items():
    print(key, ' - ', len(value), ' - ', value)




tree = Tree()
tree.create_node("Harry", "harry")  # root node
tree.create_node("Jane", "jane", parent="harry")
tree.create_node("Bill", "bill", parent="harry")
tree.create_node("Diane", "diane", parent="jane")
tree.create_node("Mary", "mary", parent="diane")
tree.create_node("Mark", "mark", parent="jane")



new_tree = Tree()
new_tree.create_node("n1", 1)  # root node
new_tree.create_node("n2", 2, parent=1)
new_tree.create_node("n3", 3, parent=1)
tree.paste('bill', new_tree)
tree.show()




def creat_tree(dicts, parent):
    tree = Tree()
    for key, value in dicts.items():
        tree.create_node(key, parent)
        if type(value) == dict:
            tree.paste(key, creat_tree(value, key))
              # root node
        else:
            for token in value:
                tree.create_node(token, parent=parent)

    return tree



# new_tree = Tree()
# new_tree.create_node("n1", 1)  # root node
# new_tree.create_node("n2", 2, parent=1)
# new_tree.create_node("n3", 3, parent=1)
# tree.paste('bill', new_tree)
# tree.show()


for key, value in itog_dict.items():
    # print(k, ' - ', len(v), ' - ', v)
    tree = Tree()
    tree.create_node(key.title(), key)  # root node
    for k, v in value.items():
        if type(v) == dict:
            tree = creat_tree(v, k)
        else:
            for token in v:
                tree.create_node(token, parent=k)
    tree.paste(key, tree)
    tree.show()




tree = Tree()
tree.create_node("Harry", "harry")  # root node
tree.create_node("Jane", "jane", parent="harry")
tree.create_node("Bill", "bill", parent="harry")
tree.create_node("Diane", "diane", parent="jane")
tree.create_node("Mary", "mary", parent="diane")
tree.create_node("Mark", "mark", parent="jane")
tree.show()


new_tree = Tree()
new_tree.create_node("n1", 1)  # root node
new_tree.create_node("n2", 2, parent=1)
new_tree.create_node("n3", 3, parent=1)
tree.paste('bill', new_tree)
tree.show()









# for k, v in dict(sorted(noun_adj_dict.items(), key=lambda x: len(x[1]), reverse=False)).items():
#     # print(k, ' - ', len(v), ' - ', v)
#     for t, m in v.items():
#         print(k, ' - ', len(v), ' - ', t, ' - ', len(m), ' - ', m)
#         if len(m) == reduce(lambda a, b: a if (a > b) else b, m):
#             pass


# adj_noun_dict = {}
# for k, v in dict(sorted(noun_adj_dict.items(), key=lambda x: len(x[1]), reverse=False)).items():
#     # print(k, ' - ', len(v), ' - ', v)
#     tree = Tree()
#     tree.create_node(k.title(), k)  # root node
#     for key, value in v.items():
#         tree.create_node(k.title() + " " + key, key, parent=k)
#         for token in value:
#             tree.create_node(token, parent=key)
#     tree.show()


# # Прилагательное + Существительное
# adj_noun_dict = {}
# for key, value in dict(sorted(dict_adj.items(), key=lambda x: len(x[1]), reverse=False)).items():
#     if len(mix_noun_adj(" ".join(value), list(set_root_noun))) != 0:
#         adj_noun_dict[key] = mix_noun_adj(" ".join(value), list(set_root_noun))
#
#
# for k, v in dict(sorted(adj_noun_dict.items(), key=lambda x: len(x[1]), reverse=False)).items():
#     print(k, ' - ', len(v), ' - ', v)
#
#
#
# def make_tree(adj_noun_dict):
#     for k, v in dict(sorted(adj_noun_dict.items(), key=lambda x: len(x[1]), reverse=False)).items():
#         # print(k, ' - ', len(v), ' - ', v)
#         tree = Tree()
#         tree.create_node(k.title(), k)  # root node
#         for key, value in v.items():
#             tree.create_node(k.title() + " " + key, key, parent=k)
#             for token in value:
#                 tree.create_node(token, parent=key)
#     return tree
#
# tree = make_tree(adj_noun_dict)
# tree.show()

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