# -*- coding: utf8 -*-
from settings import *
from function import *
from itertools import *
from anytree import Node, NodeMixin, RenderTree


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
# test_text = 'Мышечная защита, накопление экссудата и болевой синдром; функциональные расстройства работы органов пищеварения и мочевыведения; общие признаки, обусловленные интоксикацией. Острая боль в животе – наиболее типичный признак развивающегося воспаления брюшины. Особенно сильно она проявляется при перфоративных перитонитах. При воспалении, не связанном с нарушением целостности стенок внутренних органов, боли менее выражены, усиливаются постепенно. Разрыв (перфорация) стенки полого органа обычно отдаёт резкой, простреливающей болью, которая похожа на колющий удар или выстрел из пистолета. После такого больной стремится лечь и не двигаться, так как малейшее движение причиняет сильною боль. Болезненно также сотрясание брюшины, дыхание, прикосновения к передней стенке живота. Иногда боль резка и сильна настолько, что пострадавший теряет сознание, а его пульс становится нитевидным.'
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



#
# from treelib import Node, Tree
#
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



for key, value in itog_dict.items():
    print(key, ' - ', len(value), ' - ', value)
    root = Node(key)
    if type(value) == dict:
        for k, v in value.items():
            k = Node(k, parent=root)
            if type(v) == dict and len(v) != 0:
                for t, m in v.items():
                    t = Node(t, parent=k)
                    if type(m) == dict and len(m) != 0:
                        continue
                    elif type(m) == list:
                        for el in m:
                            el = Node(el, parent=t)
                    else:
                        continue
            elif type(v) == list:
                for el in v:
                    el = Node(el, parent=k)
            else:
                continue
    else:
        continue

    for pre, fill, node in RenderTree(root):
        print("%s%s" % (pre, node.name))


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



