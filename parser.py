# -*- coding: utf8 -*-
from settings import *
from function import *
from itertools import *
from anytree import Node, NodeMixin, RenderTree


pd.set_option('display.max_columns', None)

nlp = spacy.load("ru_core_news_lg") # подключение русскоязычного модуля

# загрузка определнной страницы файла
file_name="data/НСИ - закупки.xlsx"
rb = xlrd.open_workbook(file_name)
sheet = rb.sheet_by_index(1)

#Получаем список значений из всех записей
vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
print(vals)

###########Создание файла исходнйо таблицы#######################

# преобразуем в кортеж код и имя полученных терминов
print_border('Загрузка данных из таблицы EXCEL')
tuple_text = []
for el in vals[1:]:
    tuple_text.append((el[0], el[1].replace('\n', '').replace('-', '_')))

print('text  -', tuple_text)

# сохраняем полученный кортеж в файл
with open('data/table_one.csv', mode='w', encoding='utf-8', newline='') as file:
    file_writer = csv.writer(file, delimiter=',', lineterminator='\n')
    file_writer.writerow(['id', 'code', 'name'])
    for i, el in enumerate(tuple_text):
        file_writer.writerow([i+1, el[0], el[1]])
print_border('Загрузка данных из таблицы EXCEL завершена')

# загружаем полученный из исходного файл в виде словаря
dict_data = []
with open('data/table_one.csv', encoding='utf-8', newline='') as csvfile:
    reader_dict = csv.DictReader(csvfile, delimiter=',')
    for row in reader_dict:
        print(row)
        dict_data.append(row)

# Составляем список наименований терминов
list_text = [el['name'] for el in dict_data]


# print_border('СОСТАВЛЕНИЕ ПРЕДЛОЖЕНИЙ')
all_text = reduce(lambda x, y: x + '. ' + y, list_text)
#


# print_border('СИНТАКТИЧЕСКИЙ РАЗБОР SPACY')

test_text = all_text
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

# #Находим связанные с корневем прилагательные
# def find_noun_adj(text):
#     set_root = set()
#     doc = nlp(text)
#     for token in doc:
#         if token.dep_ == 'ROOT' and token.pos_ == 'NOUN': #token.dep_ == 'ROOT' and token.pos_ == 'NOUN'
#             chunk = ''
#             # print('token -', token)
#             for w in token.children:
#                 if w.dep_ == 'amod' or w.pos_ == 'ADJ':
#                     chunk = chunk + w.text + ' '
#             chunk = chunk + token.text
#             set_root.add(chunk)
#
#     return set_root

#Находим связанные с корневем прилагательные дубль
def find_noun_adj(text):
    set_root = set()
    doc = nlp(text)
    list_word_comb = []
    for token in doc:
        if token.dep_ == 'ROOT' or token.pos_ == 'NOUN': #token.dep_ == 'ROOT' and token.pos_ == 'NOUN'
            # print('token -', token)
            for w in token.children:
                if w.dep_ == 'amod' or w.pos_ == 'ADJ':
                    chunk = ''
                    chunk = chunk + w.text.lower() + ' ' + token.text.lower()
                    list_word_comb.append(chunk)

    return list_word_comb

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

#Находи прилагательные связанные с существительными в предложении
list_noun_adj = find_noun_adj(test_text)
print(len(list_noun_adj))
set_noun_adj = set(list_noun_adj)
# print(len(set_noun_adj))
# for el in set_noun_adj:
#     print(el)



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


# Создаем датасет нового концепта в дереве
list_tupl_concepts = []
for i, elem1 in enumerate(set(set_root_noun)):
    for j, elem2 in enumerate(set(set_noun_adj)):
        if elem1 in elem2.split():
            list_tupl_concepts.append(((i+1)*10000+(j+1), elem2, (i+1)*100, elem1))
        else:
            list_tupl_concepts.append(((i+1)*100, elem1, 0, "Приборы и инструменты"))

# print(len(list_tupl_concepts))
# print(len(set(list_tupl_concepts)))
#
#
#
# for el in sorted(set(list_tupl_concepts), key=lambda x: x[0]):
#     print(el)
#
# Сохраняем датасет нового концепта в дереве
with open('data/table_two.csv', mode='w', encoding='utf-8', newline='') as file:
    file_writer = csv.writer(file, delimiter=',', lineterminator='\n')
    file_writer.writerow(['id', 'name', 'parant_id', 'parant_name'])
    for el in sorted(set(list_tupl_concepts), key=lambda x: x[0]):
        file_writer.writerow([el[0], el[1], el[2], el[3]])
print_border('Создание датасета завершено')


#
data_mix = []
for elem1 in set(list_tupl_concepts):
    for elem2 in dict_data:
        if elem1[1] in elem2['name'].lower() or ' '.join(reversed(elem1[1].split())) in elem2['name'].lower():
            data_mix.append((elem1[0], elem1[1], elem2['id'], elem2['name']))
#
#         for el in elem1[3].split():
#             if el in elem2['name'].split():
#                 data_mix.append((elem1[1], elem1[3], elem2['id'], elem2['name']))
#

print(len(data_mix))
for el in data_mix:
    print(el)

with open('data/table_three.csv', mode='w', encoding='utf-8', newline='') as file:
    file_writer = csv.writer(file, delimiter=',', lineterminator='\n')
    file_writer.writerow(['id_class', 'name_class', 'id_termin', 'name_termin'])
    for el in data_mix:
        file_writer.writerow([el[0], el[1], el[2], el[3]])
print_border('Создание датасета завершено')

#
#
#
#
# itog_dict = {}
# for k, v in dict(sorted(noun_adj_dict.items(), key=lambda x: len(x[1]), reverse=False)).items():
#     # print(k, ' - ', len(v), ' - ', v)
#
#     itog_dict[k] = make_recurs_dict(v)

#*****************************************************************************************************


from treelib import Node, Tree

#
# def rec_tree(array):
#     tree = Tree()
#     for key, value in array.items():
#         tree.create_node(key, key)  # root node
#         if isinstance(value, list):
#             for el in value:
#                 return tree.create_node(el, el, parent=key)
#         else:
#             new_tree = rec_tree(value)
#             if isinstance(new_tree, Tree):
#                 return tree.paste(key, new_tree)
#             else:
#                 continue
#
#
# #
# tree = Tree()
# for key, value in itog_dict.items():
#     print(key, ' - ', len(value), ' - ', value)
#     tree.create_node(key, key)  # root node
#     if isinstance(value, list):
#         for el in value:
#             tree.create_node(el, el, parent=key)
#     else:
#         new_tree = rec_tree(value)
#         if isinstance(new_tree, Tree):
#             tree.paste(key, new_tree)
#         else:
#             continue
#
#     tree.show()


#
# tree = Tree()
# tree.create_node("Harry", "harry")  # root node
# tree.create_node("Jane", "jane", parent="harry")
# tree.create_node("Bill", "bill", parent="harry")
# tree.create_node("Diane", "diane", parent="jane")
# tree.create_node("Mary", "mary", parent="diane")
# tree.create_node("Mark", "mark", parent="jane")
# tree.show()
#
#
# new_tree = Tree()
# new_tree.create_node("n1", 1)  # root node
# new_tree.create_node("n2", 2, parent=1)
# new_tree.create_node("n3", 3, parent=1)
# tree.paste('bill', new_tree)
# tree.show()

#####################################################
#***************************************************
#
# for key, value in itog_dict.items():
#     print(key, ' - ', len(value), ' - ', value)
#     root = Node(key)
#     if type(value) == dict:
#         for k, v in value.items():
#             k = Node(k, parent=root)
#             if type(v) == dict and len(v) != 0:
#                 for t, m in v.items():
#                     t = Node(t, parent=k)
#                     if type(m) == dict and len(m) != 0:
#                         continue
#                     elif type(m) == list:
#                         for el in m:
#                             el = Node(el, parent=t)
#                     else:
#                         continue
#             elif type(v) == list:
#                 for el in v:
#                     el = Node(el, parent=k)
#             else:
#                 continue
#     else:
#         continue
#
#     for pre, fill, node in RenderTree(root):
#         print("%s%s" % (pre, node.name))
#*********************************************************************

#
# def iteritems_recursive(itog_dict):
#   for k, v in itog_dict.items():
#     if isinstance(v, dict):
#       for k1, v1 in iteritems_recursive(v):
#         yield (k,)+k1, v1
#     else:
#       yield (k,),v
#
#
#
# for p, v in iteritems_recursive(itog_dict):
#     print(p, "->", v)
#



#
# class Tree(object):
#     "Generic tree node."
#     def __init__(self, name='root', children=None):
#         self.name = name
#         self.children = []
#         if children is not None:
#             for child in children:
#                 self.add_child(child)
#     def __repr__(self):
#         return self.name
#     def add_child(self, node):
#         assert isinstance(node, Tree)
#         self.children.append(node)
#


# #
# fieldnames = ['id', 'name', 'master_id', 'parent_id']
# with open('datas/table.csv', mode='w', encoding='utf-8', newline='') as file:
#     file_writer = csv.DictWriter(file, delimiter=',', fieldnames=fieldnames)
#     file_writer.writeheader()
#     for key, value in itog_dict.items():
#         if isinstance(value, list):
#             for i, el in enumerate(value):
#                 file_writer.writerow([i, key, j, value])
#
#
# with open('db/dataset_black/disease_symptoms_names2.csv', mode='w', encoding='utf-8', newline='') as file:
#     file_writer = csv.writer(file, delimiter=',', lineterminator='\n')
#     file_writer.writerow(['id_symptoms', 'name_symptoms'])
#     for key, value in itog_dict.items():
#         file_writer.writerow([key, value])


# all_list = []
# parent = []
#
# def inter_list(all_dict):
#     all_list = []
#     for key, value in all_dict.items():
#         if isinstance(value, dict):
#             all_list.append(key)
#             all_list.extend(inter_list(value))
#         else:
#             all_list.append(key)
#             all_list.extend(value)
#
#     return all_list
#
#
# all_array = inter_list(itog_dict)
# print(all_array)
# print(len(all_array))
#
# set_array = set(all_array)
# print(len(set_array))

#
# def iteritems_recursive(itog_dict):
#   for k, v in itog_dict.items():
#     if isinstance(v, dict):
#       for k1, v1 in iteritems_recursive(v):
#         yield (k,)+k1, v1
#     else:
#       yield (k,),v
#






# #Во-первых , найдите родителя по имени, используя anytrees find_by_attr
# from anytree import Node, RenderTree, find_by_attr
#
# with open('input.txt', 'r') as f:
#     lines = f.readlines()[1:]
#     root = Node(lines[0].split(" ")[0])
#
#     for line in lines:
#         line = line.split(" ")
#         Node("".join(line[1:]).strip(), parent=find_by_attr(root, line[0]))
#
#     for pre, _, node in RenderTree(root):
#         print("%s%s" % (pre, node.name))

# #Во-вторых , просто кэшируйте их в диктанте, пока мы их создаем:
# from anytree import Node, RenderTree, find_by_attr
#
# with open('input.txt', 'r') as f:
#     lines = f.readlines()[1:]
#     root = Node(lines[0].split(" ")[0])
#     nodes = {}
#     nodes[root.name] = root
#
#     for line in lines:
#         line = line.split(" ")
#         name = "".join(line[1:]).strip()
#         nodes[name] = Node(name, parent=nodes[line[0]])
#
#     for pre, _, node in RenderTree(root):
#         print("%s%s" % (pre, node.name))









# root = Node("root", children=[
# Node("sub0", children=[
#     Node("sub0B", bar=109, foo=4),
#     Node("sub0A", children=None),
# ]),
# Node("sub1", children=[
#     Node("sub1A"),
#     Node("sub1B", bar=8, children=[]),
#     Node("sub1C", children=[
#         Node("sub1Ca"),
#     ]),
# ]),
# ])



from anytree import NodeMixin, RenderTree

class MyBaseClass(object):  # Just an example of a base class
    foo = 4

class MyClass(MyBaseClass, NodeMixin):  # Add Node feature
    def __init__(self, name, length, width, parent=None, children=None):
        super(MyClass, self).__init__()
        self.name = name
        self.length = length
        self.width = width
        self.parent = parent
        if children:
            self.children = children





#
# tree = Tree()
# tree.create_node("Harry", "harry")  # root node
# tree.create_node("Jane", "jane", parent="harry")
# tree.create_node("Bill", "bill", parent="harry")
# tree.create_node("Diane", "diane", parent="jane")
# tree.create_node("Mary", "mary", parent="diane")
# tree.create_node("Mark", "mark", parent="jane")
#
#
#
# new_tree = Tree()
# new_tree.create_node("n1", 1)  # root node
# new_tree.create_node("n2", 2, parent=1)
# new_tree.create_node("n3", 3, parent=1)
# tree.paste('bill', new_tree)
# tree.show()
#
#
#
#
# def creat_tree(dicts, parent):
#     tree = Tree()
#     for key, value in dicts.items():
#         tree.create_node(key, parent)
#         if type(value) == dict:
#             tree.paste(key, creat_tree(value, key))
#               # root node
#         else:
#             for token in value:
#                 tree.create_node(token, parent=parent)
#
#     return tree
#


# new_tree = Tree()
# new_tree.create_node("n1", 1)  # root node
# new_tree.create_node("n2", 2, parent=1)
# new_tree.create_node("n3", 3, parent=1)
# tree.paste('bill', new_tree)
# tree.show()


# for key, value in itog_dict.items():
#     # print(k, ' - ', len(v), ' - ', v)
#     tree = Tree()
#     tree.create_node(key.title(), key)  # root node
#     for k, v in value.items():
#         if type(v) == dict:
#             tree = creat_tree(v, k)
#         else:
#             for token in v:
#                 tree.create_node(token, parent=k)
#     tree.paste(key, tree)
#     tree.show()

# from collections import defaultdict
#
# d = defaultdict(list)  # parent: List[children]
# for k, v in itog_dict.items():
#     d[v['parent']].append(k)
# root = d[None][0]
#
# tree = Tree()
# tree.create_node(root, root)
#
# agenda, seen = [root], set([root])
# while agenda:
#     nxt = agenda.pop()
#     for child in d[nxt]:
#         tree.create_node(child, child, parent=nxt)
#         if child not in seen:
#             agenda.append(child)
#             seen.add(child)



# from treelib import Node, Tree
#
# dict_ = itog_dict
#
# added = set()
# tree = Tree()
# while dict_:
#     for key, value in dict_.items():
#         if value['parent'] in added:
#             tree.create_node(key, key, parent=value['parent'])
#             added.add(key)
#             dict_.pop(key)
#             break
#         elif value['parent'] is None:
#             tree.create_node(key, key)
#             added.add(key)
#             dict_.pop(key)
#             break
#
# tree.show()


#
# tree = Tree()
# tree.create_node("Harry", "harry")  # root node
# tree.create_node("Jane", "jane", parent="harry")
# tree.create_node("Bill", "bill", parent="harry")
# tree.create_node("Diane", "diane", parent="jane")
# tree.create_node("Mary", "mary", parent="diane")
# tree.create_node("Mark", "mark", parent="jane")
# tree.show()
#
#
# new_tree = Tree()
# new_tree.create_node("n1", 1)  # root node
# new_tree.create_node("n2", 2, parent=1)
# new_tree.create_node("n3", 3, parent=1)
# tree.paste('bill', new_tree)
# tree.show()



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




#
# from anytree import NodeMixin, RenderTree
#
#
# class MyClass(NodeMixin):  # Add Node feature
#     def __init__(self, name, parent=None):
#         super(MyClass, self).__init__()
#         self.name = name
#         self.parent = parent
#
#
#
#
# def print_anytree(startnode):
#
#     for pre, _, node in RenderTree(startnode):
#         treestr = u"%s%s" % (pre, node.name)
#         print(treestr.ljust(8))
#
# def rec_tree(dict_arr, MyClass):
#     for k, v in value.items():
#         if isinstance(v, list):
#             for el in v:
#                 return MyClass(el, parent=k)
#         else:
#             NodeMixin(rec_tree(v, MyClass), k)
#
#
# if __name__ == '__main__':
#     for key, value in itog_dict.items():
#
#         print(key, ' - ', len(value), ' - ', value)
#         key = MyClass(key)
#         if isinstance(value, list):
#             for el in value:
#                 el = MyClass(el, parent=key)
#         else:
#             NodeMixin(rec_tree(value, MyClass), key)
#
#     print_anytree(key)
#



