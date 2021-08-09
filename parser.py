from settings import *
from function import *

pd.set_option('display.max_columns', None)

nlp = spacy.load("ru_core_news_lg")

# stop_words = nltk.corpus.stopwords.words('russian')

file_name="data/НСИ - закупки.xlsx"
rb = xlrd.open_workbook(file_name)
sheet = rb.sheet_by_index(1)

#получаем список значений из всех записей
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

#
#
# print('test_text  -', test_text)
# print('type(test_text) -', type(test_text))


print_border('КОНЕЦ СИНТАКТИЧЕСКОГО РАЗБОРА SPACY')
#
# tmp_text = 'Анестезиологические и респираторные медицинские изделия. Ортопедические медицинские изделия. ' \
#            'Стерилизаторы и сопутствующие изделия. Офтальмологические медицинские изделия. Офтальмологические лазерные системы. ' \
#            'Ламинарные системы. Сетки хирургические и сопутствующие изделия. Матрасы медицинские и сопутствующие изделия. ' \
#            'Радиологические медицинские изделия. Медицинские изделия для анализа гемодинамики. ' \
#            'Медицинские изделия для сердечно-сосудистой хирургии. Экспресс-тесты. Мониторы/мониторные системы гастроэнтерологические. ' \
#            'Системы электростимуляции центральной нервной системы'

# print(tmp_text)
# print(type(tmp_text))

#Анализ частоты слова
# tmp = tmp_text.replace('.', '').lower().split()
tmp = test_text.replace('.', '').lower().split()
# print(tmp)
# print(type(tmp))
count_word = Counter(tmp)
# print(count_word)

t_count = max(count_word, key=count_word.get)
# print(len(t_count))

t_unic = {el for el in tmp if len(el) > 3}
# print(t_unic)
# print(len(t_unic))


def parsSent(sent):
    if sent[-2].dep_ == 'ROOT' and sent[-2].pos_ == 'NOUN':
        return sent[-2].test



dataSet = pd.DataFrame(0, index=t_unic, columns=t_unic)
# print(dataSet)
# print('3 - ', symb)
dict_word = {}
for el in test_text.split('.'):
    for symb in el.lower().split(' '):
        if symb not in dict_word.keys():
            if len(symb) > 3:
                dict_word[symb] = [el + '.']
        else:
            dict_word[symb].append(el + '.')


# print(dict_word)
# sort_list = []
for k, v in dict(sorted(dict_word.items(), key=lambda x: len(x[1]), reverse=False)).items():
    # if len(v) > 1:
    #     if dict_word[k][0] in dict_word[root_count]:

    print(k, ' - ', len(v), v)

# print(dict_word['стерилизаторы'][0] in dict_word['изделия'])
print_border('КОНЕЦ СИНТАКТИЧЕСКОГО РАЗБОРА SPACY')

# root_count = max(dict_word, key=dict_word.get)
root_count = max(dict_word.items(), key = lambda x: x[1])[0]
print(root_count)

tree = Tree()
tree.create_node(max(dict_word, key=dict_word.get).upper(), max(dict_word, key=dict_word.get))  # root node

for k, v in dict_word.items():
    if k != root_count:
        if dict_word[k][0] in dict_word[root_count]:
            if len(v) > 1:
                tree.create_node(k.upper(), k, parent=root_count)
                for el in v:
                    tree.create_node(el, parent=k)

tree.show()


##############################################################################
#                                  ВАРИАНТ 4                                 #
##############################################################################
#

# #Формирование таблицы смещения
# t = max(count_word, key=count_word.get)
#
# S = set()   # Уникадбные символы в образцу
# M = len(t)  # Число символов в образце
# d ={}       # Словарь смещений
#
# for i in range(M - 2, -1, -1):  # Итерации с предпоследнего символа
#     if t[i] not in S:           # если символ еще не добавлен в таблицу
#         d[t[i]] = M - i - 1
#         S.add(t[i])
#
# if t[M - 1] not in S:          # Отдельно формируем последний символ
#     d[t[M-1]] = M
#
# d['*'] = M                     # смещение для прочих символов
#
# print(d)
#
#
# #Поиск образца в строке
#
# a = tmp_text
# N = len(a)
#
# if N >= M:
#     i = M - 1
#     while i < N:
#         k = 0
#         for j in range(M - 1, -1, -1):
#             if a[i-k] != t[j]:
#                 if j == M - 1:
#                     off = d[a[i]] if d.get(a[i], False) else d['*']
#                 else:
#                     off = d[t[j]]
#                 i += off
#                 break
#             k += 1
#         if j == 0:
#             print(f"Образец найден по индексу {i - k + 1}")
#             break
#
# else:
#     print("Образец не найден.")



# doc = nlp(test_text)

# print(doc)
# print(type(doc))

# doc = nlp(test_text)


# spans = list(doc.sents)
# print(spans)

# for el in doc:
#     print(el)

# spans = doc.sents
# print(spans)

# options = {'compact': True, 'font': "Tahoma"}
# displacy.serve(spans, style='dep', options=options, host='localhost')

##############################################################################
#                                  ВАРИАНТ 3                                 #
##############################################################################
#

# for sent1 in spans[:-1]:
#     temp = []
#     print('sent1 - ', sent1)
#     for sent2 in spans[spans.index(sent1) + 1:]:
#         print('\t\t\tsent2 - ', sent2)

# temp_dict = {}
# for sent in spans:
#     print(sent[-2])
#     root_phrase = ''
#     amod_phrase = ''
#     if sent[-2].dep_ == 'ROOT' and sent[-2].pos_ == 'NOUN':
#         if sent[-2].text not in temp_dict:
#             temp_dict[sent[-2].text] = [sent.text]
#         else:
#             temp_dict[sent[-2].text].append(sent.text)
#
# for k, v in temp_dict.items():
#     print(k, v)



# def parseSent(sent):
#
#     root_phrase = ''
#     amod_phrase = ''
#     nmod_phrase = ''
#     nmod_phrase_all = ''
#     list_root_word = []
#
#     if sent[-2].dep_ == 'ROOT' and sent[-2].pos_ == 'NOUN':
#         root_phrase = root_phrase + ' ' + sent[-2].text
#         if sent[-3].dep_ == 'amod' and sent[-3].pos_ == 'ADJ':
#             amod_phrase_all = ''
#             for word in sent[-2].lefts:
#                 if word.dep_ == 'amod' and word.pos_ == 'ADJ':
#                     amod_phrase_all = amod_phrase_all.rstrip() + ' ' + word.text
#
#             list_root_word.append((amod_phrase_all + root_phrase, amod_phrase_all.split(' ')[-1] + root_phrase ))
#
#     return list_root_word
#
# list_root_fierst = []
# list_root_second = []
# temp_list = {}
# big_temp_list = []
# for sent1 in spans[:-1]:
#     temp = []
#     if len(sent1.text.split()) > 1:
#         list_root_fierst = parseSent(sent1)
#         if len(list_root_fierst) > 0:
#             for sent2 in spans[spans.index(sent1) + 1:]:
#                 if len(sent2.text.split()) > 1:
#                     list_root_second = parseSent(sent1)
#                     if len(list_root_second) > 0:
#                         if float(sent1.similarity(sent2)) > 0.8:
#                             if list_root_fierst[0][1] not in temp_list.keys():
#                                 print('list_root_second_1 - ', list_root_fierst[0][1])
#                                 temp_list[list_root_fierst[0][1]] = [sent1.text]
#                             else:
#                                 temp_list[list_root_fierst[0][1]].append(sent1.text)
#
#
#                             if list_root_second[0][1] not in temp_list.keys():
#                                 print('list_root_second_2 - ', list_root_second[0][1])
#                                 temp_list[list_root_second[0][1]] = [sent2.text]
#                             else:
#                                 temp_list[list_root_second[0][1]].append(sent2.text)
#
#
#
#
#
#
#
# for k, v in temp_list.items():
#     print(k, v)


#
# tree = Tree()
# tree.create_node("Harry", "harry")  # root node
# tree.create_node("Jane", "jane", parent="harry")
# tree.create_node("Bill", "bill", parent="harry")
# tree.create_node("Diane", "diane", parent="jane")
# tree.create_node("Mary", "mary", parent="diane")
# tree.create_node("Mark", "mark", parent="jane")
# tree.show()






# doc1 = 'Анестезиологические и респираторные медицинские изделия.'
# doc2 = 'Ортопедические медицинские изделия.'
# doc3 = 'Офтальмологические медицинские изделия.'
# doc4 = 'Медицинские изделия для анализа гемодинамики'
# doc5 = 'Медицинские изделия для кардиореанимации'
#
# doc1 = nlp(doc1)
# doc2 = nlp(doc2)
# doc3 = nlp(doc3)
# doc4 = nlp(doc4)
# doc5 = nlp(doc5)
# print('1 - 2', doc1.similarity(doc2))
# print('1 - 3', doc1.similarity(doc3))
# print('1 - 4', doc1.similarity(doc4))
# print('2 - 3', doc2.similarity(doc3))
# print('2 - 4', doc2.similarity(doc4))
# print('3 - 4', doc3.similarity(doc4))
# print('4 - 5', doc4.similarity(doc5))
# print('1 - 5', doc1.similarity(doc5))



# comb_word = ''
# comb_word_all = ''
# list_root_word1 = []
# list_root_word2 = []
# for i, sents in enumerate(doc.sents):
#     for
#     # print(sents.text.split())
#     # print(len(sents.text.split()))
#     # print(sents[-2])
#     if len(sents.text.split()) > 1:
#         root_phrase = ''
#         amod_phrase = ''
#         nmod_phrase = ''
#
#         nmod_phrase_all = ''
#
#         if sents[-2].dep_ == 'ROOT' and sents[-2].pos_ == 'NOUN':
#             # print(sents)
#             # print(sents[-2])
#             # print([w for w in sents[-2].lefts])
#             # print(len([w for w in sents[-2].lefts]))
#             root_phrase = root_phrase + ' ' + sents[-2].text
#             # temp_word = root_phrase
#             # print(phrase.strip())
#             if sents[-3].dep_ == 'amod' and sents[-3].pos_ == 'ADJ':
#                 # print([w for w in sents[-2].lefts])
#                 amod_phrase_all = ''
#                 for word in sents[-2].lefts:
#                     # print(word)
#                     if word.dep_ == 'amod' and word.pos_ == 'ADJ':
#                         # print(word.text)
#                         amod_phrase_all = amod_phrase_all + ' ' + word.text
#
#                 list_root_word1.append(amod_phrase_all + root_phrase)
#
# for el in list_root_word1:
#     print(el)






#
# temp_list = []
# for sent1 in spans[:-1]:
#     temp = []
#     for sent2 in spans[spans.index(sent1) + 1:]:
#         print(float(sent1.similarity(sent1)) - float(sent1.similarity(sent2)))
#         if float(sent1.similarity(sent2)) > 0.8:
#             if sent1 not in temp_list:
#                 temp_list.append(sent1)
#
#             if sent2 not in temp_list:
#                 temp.append(sent2)
#
#
#     if len(temp) != 0:
#         temp_list.extend(temp)
#
#
# for el in temp_list:
#     print(el)
#
#






# options = {'compact': True, 'font': "Tahoma"}
# displacy.serve(spans, style='dep', options=options, host='localhost')
#

##############################################################################
#                                  ВАРИАНТ 2                                 #
##############################################################################

# comb_word = ''
# comb_word_all = ''
# list_root_word1 = []
# list_root_word2 = []
# for i, sents in enumerate(doc.sents):
#     # print(sents.text.split())
#     # print(len(sents.text.split()))
#     # print(sents[-2])
#     if len(sents.text.split()) > 1:
#         root_phrase = ''
#         amod_phrase = ''
#         nmod_phrase = ''
#
#         nmod_phrase_all = ''
#
#         if sents[-2].dep_ == 'ROOT' and sents[-2].pos_ == 'NOUN':
#             # print(sents)
#             # print(sents[-2])
#             # print([w for w in sents[-2].lefts])
#             # print(len([w for w in sents[-2].lefts]))
#             root_phrase = root_phrase + ' ' + sents[-2].text
#             # temp_word = root_phrase
#             # print(phrase.strip())
#             if sents[-3].dep_ == 'amod' and sents[-3].pos_ == 'ADJ':
#                 # print([w for w in sents[-2].lefts])
#                 amod_phrase_all = ''
#                 for word in sents[-2].lefts:
#                     # print(word)
#                     if word.dep_ == 'amod' and word.pos_ == 'ADJ':
#                         # print(word.text)
#                         amod_phrase_all = amod_phrase_all + ' ' + word.text
#
#                 list_root_word1.append(amod_phrase_all + root_phrase)
#
# for el in list_root_word1:
#     print(el)

        # if amod_phrase_all != '':
        #     comb_word_all = amod_phrase_all + ' ' + root_phrase
        #     print(comb_word_all)
        # else:
        #     comb_word_all = root_phrase + ' ' + nmod_phrase_all
        #     print(comb_word_all)

        # comb_word = amod_phrase + ' ' + root_phrase
        # comb_word_all = amod_phrase_all + ' ' + root_phrase


        # print(comb_word)
        # print(comb_word_all)
# print('list_root_word1 - ', list_root_word1)
# print('list_root_word2 - ', list_root_word2)
#
# temp_text = reduce(lambda x, y: x + ', ' + y, list_root_word1)
# print(temp_text)

# count = Counter(list_root_word1)
# print(count)
# temp_text.split()
# options = {'compact': True, 'font': "Tahoma"}
# displacy.serve(spans, style='dep', options=options, host='localhost')
#


##############################################################################
#                                  ВАРИАНТ 1                                 #
##############################################################################
# comb_word = ''
# comb_word_all = ''
# list_root_word1 = []
# list_root_word2 = []
# for token in doc:
#     root_phrase = ''
#     amod_phrase = ''
#     nmod_phrase = ''
#     amod_phrase_all = ''
#     nmod_phrase_all = ''
#     # if token.pos_ == 'NOUN':
#     #     phrase = phrase + ' ' +token.text
#     if token.dep_ == 'ROOT' and token.pos_ == 'NOUN':
#         root_phrase = root_phrase + ' ' + token.text
#         temp_word = root_phrase
#         # print(phrase.strip())
#         for word in token.children:
#             # print(word)
#             if word.dep_ == 'amod' and word.pos_ == 'ADJ':
#                 amod_phrase = word.text
#                 amod_phrase_all = amod_phrase_all + ' ' + word.text
#
#             list_root_word1.append(amod_phrase + ' ' + temp_word)
#
#             if word.dep_ == 'nmod' and word.pos_ == 'NOUN':
#                 nmod_phrase = word.text
#                 nmod_phrase_all = nmod_phrase_all + ' ' + word.text
#
#             list_root_word2.append(temp_word + ' ' + nmod_phrase)
#
#         if amod_phrase_all != '':
#             comb_word_all = amod_phrase_all + ' ' + root_phrase
#             print(comb_word_all)
#         else:
#             comb_word_all = root_phrase + ' ' + nmod_phrase_all
#             print(comb_word_all)



##############################################################################
#                                  ВАРИАНТ 2                                 #
##############################################################################















# comb_token = syntax_parsing(text, nlp)
#
#
# for el in comb_token:
#     print(el)
















# #Очистка и токенизация текста
# allwords = [el[1].replace('\n', '').split(" ") for el in vals[1:]]
# print('allwords -', allwords)
# print('1.1 -', len(allwords))
#
# #Очистка и токенизация текста с учетом стоп-слов
# processed_data = []
# processed_data_all = []
# for doc in vals[1:]:
#     tokens = preprocess_text(doc, stop_words)
#     processed_data.append(tokens)
#     processed_data_all += tokens
#
# print('processed_data -', processed_data)
# print('2.1 -', len(processed_data))

# for el in processed_data:
#     print(el)


#
# temp_res = [' '.join(el) for el in processed_data]
#
# tfidf_vectorizer = TfidfVectorizer(max_df=1.0,
#                                    max_features=2500,
#                                    min_df=0.0,
#                                    use_idf=True,
#                                    ngram_range=(1, 3))
#
# tfidf_matrix = tfidf_vectorizer.fit_transform(temp_res)
#
#
# features = tfidf_vectorizer.get_feature_names()
# indices = zip(*tfidf_matrix.nonzero())
# print(features)
# # data_list = {}
# # for row, column in indices:
# #     if row not in data_list.keys():
# #         data_list[row] = [(features[column], tfidf_matrix[row, column], row)]
# #     else:
# #         data_list[row].append((features[column], tfidf_matrix[row, column], row))
#
#
# dense = tfidf_matrix.todense()
# print(dense.shape)
# vectorizer = TfidfVectorizer()
# X = vectorizer.fit_transform(temp_res)
#
# dataSet = pd.DataFrame(data=X.todense(), columns=vectorizer.get_feature_names())
# dataSet["Class"] = [el for el in range(1, (len(dataSet.index)) + 1)]
# # print(dataSet)
# # print(dataSet.shape)
#
# X = dataSet.drop('Class', axis=1)
# y = dataSet['Class']
#
#
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
#
# classifier = DecisionTreeClassifier()
# classifier.fit(X_train, y_train)
#
# y_pred = classifier.predict(X_test)
#



# clf = tree.DecisionTreeClassifier()
# clf = clf.fit(X, y)



#
# all_concept = []
# for k, v in data_list.items():
#     # print(k, ' - ', sorted(v, key=lambda x: x[1], reverse=True))
#     all_concept.extend(v)
#
#
# # print(all_concept)
#
# # print(len(all_concept))
#
# voc = [ el[0] for el in sorted(all_concept, reverse=False) ]
# voc2 = sorted(list(set(voc)), reverse=False)
# voc_lib = {}
# for i, el in enumerate(voc2, start=1):
#     voc_lib[el] = i

# for k, v in voc_lib.items():
#     print(k, ' - ', v)


# new_all_concept = []
# for el in all_concept:
#     new_all_concept.append((voc_lib[el[0]], *el))
#
# new_all_concept_sort = sorted(new_all_concept, key=lambda x: x[0], reverse=False)

# for el in new_all_concept_sort:
#     print(el)

#
# print_border('СИНТАКТИЧЕСКИЙ РАЗБОР SPACY')
#
# # doc = nlp('Анестезиологические и респираторные медицинские изделия. Ортопедические медицинские изделия. '
# #           'Офтальмологические медицинские изделия. '
# #           'Радиологические медицинские изделия')
# # spans = list(doc.sents)
# # displacy.serve(spans, style='dep', host='localhost')
#
# # comb_token = syntax_parsing(text, nlp)
# #
# #
# # for el in comb_token:
# #     print(el)



#
# temp_list = []
# for sent1 in spans[:-1]:
#     temp = []
#     for sent2 in spans[spans.index(sent1) + 1:]:
#         print(sent1)
#         print(sent2)
#         print(sent1.similarity(sent2))
#         print(type(float(sent1.similarity(sent2))))
#         print('-' * 50)
#         print(float(sent1.similarity(sent1)) - float(sent1.similarity(sent2)))
#         if float(sent1.similarity(sent2)) > 0.8:
#             if sent1 not in temp_list:
#                 temp_list.append(sent1)
#
#             if sent2 not in temp_list:
#                 temp.append(sent2)
#
#
#     if len(temp) != 0:
#         temp_list.extend(temp)
#
#
# for el in temp_list:
#     print(el)
















# count_lib = counterConcept(new_all_concept_sort, voc_lib)
#
# for k, v in sorted(count_lib.items(), key=lambda x: x[1], reverse=True):
#     print(k, ' - ', v)

# for el in sorted(all_concept, key=lambda x: x[0], reverse=False):
#     print(el)

# #
# #
# def compute_tfidf(corpus):
#     def compute_tf(text):
#         tf_text = Counter(text)
#         for i in tf_text:
#             tf_text[i] = tf_text[i] / float(len(text))
#
#         return tf_text
#
#     def compute_idf(word, corpus):
#         return math.log10(len(corpus) / sum([1.0 for i in corpus if word in i]))
#
#     documents_list = []
#     for text in corpus:
#         tf_idf_dictionary = {}
#         computed_tf = compute_tf(text)
#         for word in computed_tf:
#             tf_idf_dictionary[word] = computed_tf[word] * compute_idf(word, corpus)
#             documents_list.append(tf_idf_dictionary)
#
#     return documents_list
#
#
#
# result = compute_tfidf(processed_data)
# result2 = {}
# for el in result:
#     for k, v in el.items():
#         if k not in result2.keys():
#             result2[k] = v
#
#
# print(result2)
# res = [(k, result2[k]) for k in sorted(result2, key=result2.get, reverse=True)]
# for k, v in res:
#     print(k, v)
#
# print(len(result))
# print(len(result2))



# print(list([[].append(x) for x, y in zip(result[:-1], result[1:]) if x == y]))

#
# fierst_dict = {}
# second_dict = {}
#
# for i, el in enumerate(processed_data):
#     # print('3.0 -', el)
#     if el[0] not in fierst_dict.keys():
#         fierst_dict[el[0]] = [" ".join(allwords[i])]
#         second_dict[el[0]] = [el[1:]]
#     else:
#         fierst_dict[el[0]].append(" ".join(allwords[i]))
#         second_dict[el[0]].append(el[1:])
#
# print('3.1 -', fierst_dict)
# print('3.2 -', second_dict)
#
#
# big_dict = {}
# big_dict2 = {}
# for key, value in second_dict.items():
#     temp_dict = dublicated(value)
#     print('4.0 -', temp_dict)






# def dublicated(allwords):
#     temp_dict = {}
#     for i, el in enumerate(allwords):
#         if len(el) > 1:
#             if len(el[1]) > 1:
#                 if
#                 if el[1] not in temp_dict.keys():
#                     temp_dict[el[1]] = [" ".join(el)]
#                 else:
#                     temp_dict[el[1]].append(" ".join(el))
#         else:
#             return el
#     return temp_dict



# def dublicated(allwords):
#     temp_list = [set(el) for el in allwords]
#     res = list([x & y for x, y in zip(temp_list[:-1], temp_list[1:])])
#
#     print(res)





# b = list(itertools.combinations(allwords, 2))
# res = [x for x in b if x[0] in x[1]]
# def dublicated(allwords):
#     new_list = []
#     for el1 in allwords[:len(allwords)-1]:
#         if len(el1) > 1:
#             temp_list = []
#             temp_dict = {}
#             for el2 in allwords[1:len(allwords)]:
#                 if len(el2[1]) > 3:
#                     if el1[1] == el2[1]:
#                         if el1[1] not in temp_dict.keys():
#                             temp_dict[el1[1]] = [el1]
#                         else:
#                             temp_dict[el[1]].append(el1)
#                     else:
#                         temp_list.append(el2)
#                 else:
#                     temp_list.append(el2)
#
#                 temp_list.append(el1)
#
#             if len(temp_dict) > 0:
#                 new_list.append(temp_dict)
#
#             new_list.append(temp_list)
#
#         else:
#             new_list = allwords
#     return new_list




# def dublicated(allwords):
#     new_list = []
#     for el1 in allwords[:len(allwords)]:
#         if len(el1) > 1:
#             temp_dict = {}
#             temp_list = []
#             for el2 in allwords[1:len(allwords)]:
#                 if len(el2[1]) > 3:
#                     if el1[1] == el2[1]:
#                         if el1[1] not in temp_dict.keys():
#                             temp_dict[el1[1]] = [el1]
#                         else:
#                             temp_dict[el[1]].append(el1)
#                     else:
#                         temp_list.append(el2)
#                 else:
#                     temp_list.append(el2)
#             if len(temp_dict) > 0:
#                 new_list.append(temp_dict)
#
#             new_list.append(temp_list)
#
#         else:
#             new_list = allwords
#     return new_list


# fierst_dict = {}
# second_dict = {}
#
# for i, el in enumerate(processed_data):
#     # print('3.0 -', el)
#     if el[0] not in fierst_dict.keys():
#         fierst_dict[el[0]] = [" ".join(allwords[i])]
#         second_dict[el[0]] = [el[1:]]
#     else:
#         fierst_dict[el[0]].append(" ".join(allwords[i]))
#         second_dict[el[0]].append(el[1:])
#
# print('3.1 -', fierst_dict)
# print('3.2 -', second_dict)
#
#
# big_dict = {}
# big_dict2 = {}
# for key, value in second_dict.items():
#     temp_dict = dublicated(value)
#     print('4.0 -', temp_dict)


    # for i, el1 in enumerate(value):
    #     for j, el2 in enumerate(value, i+1):
    #         print('4.0.1 -', el1)
    #         print('4.0.2 -', el2)
    #         if el1[0] == el2[0]:
    #             if len(el2) > 1:
    #                 if el1[1] == el2[1]:
    #                     if el2[1] not in temp_dict.keys():
    #                         temp_dict[el2[1]] = [" ".join(allwords[j])]
    #                         temp_dict2[el2[1]] = [el2]
    #                     else:
    #                         temp_dict[el2[1]].append(" ".join(allwords[j]))
    #                         temp_dict2[el2[1]].append(el2)
    #                 else:
    #                     if el2[1] not in temp_dict.keys():
    #                         temp_dict[el2[1]] = [" ".join(allwords[j])]
    #                         temp_dict2[el2[1]] = [el2]
    #                     else:
    #                         temp_dict[el2[1]].append(" ".join(allwords[j]))
    #                         temp_dict2[el2[1]].append(el2)
    #
    #
    # if key not in big_dict.keys():
    #     big_dict[key] = [temp_dict]
    #     big_dict2[key] = [temp_dict2]
    # else:
    #     big_dict[key].append(temp_dict)
    #     big_dict2[key].append(temp_dict2)

# print('4.1 -', big_dict)
# print('4.2 -', big_dict2)
#






# big_dict = {}
# big_dict2 = {}
# for key, value in second_dict.items():
#     temp_dict = {}
#     temp_dict2 = {}
#     for i, el1 in enumerate(value):
#         for j, el2 in enumerate(value, i + 1):
#             print('4.0.1 -', el1)
#             print('4.0.2 -', el2)
#             if el1[0] == el2[0]:
#                 if len(el2) > 1:
#                     if el1[1] == el2[1]:
#                         if el2[1] not in temp_dict.keys():
#                             temp_dict[el2[1]] = [" ".join(allwords[j])]
#                             temp_dict2[el2[1]] = [el2]
#                         else:
#                             temp_dict[el2[1]].append(" ".join(allwords[j]))
#                             temp_dict2[el2[1]].append(el2)
#                     else:
#                         if el2[1] not in temp_dict.keys():
#                             temp_dict[el2[1]] = [" ".join(allwords[j])]
#                             temp_dict2[el2[1]] = [el2]
#                         else:
#                             temp_dict[el2[1]].append(" ".join(allwords[j]))
#                             temp_dict2[el2[1]].append(el2)
#
#     if key not in big_dict.keys():
#         big_dict[key] = [temp_dict]
#         big_dict2[key] = [temp_dict2]
#     else:
#         big_dict[key].append(temp_dict)
#         big_dict2[key].append(temp_dict2)
#
# print('4.1 -', big_dict)
# print('4.2 -', big_dict2)

# fierst_dict = {}
# fierst_list = []
# for i, el1 in enumerate(processed_data):
#     for j, el2 in enumerate(processed_data, start=i+1):
#         if el1[i][0] == el2[j][0]:
#             fierst_list







#
# fierst_dict = dublicated(allwords, 0)
# # print(fierst_dict)
#
# new_dict = {}
# for key, value in fierst_dict.items():
#     print('0 - ', value)
#     if len(value) > 1:
#         word_list = [el[0].split(' ') for el in [el.split(",") for el in value]]
#         print('1 - ', word_list)
#         temp_dict = dublicated(word_list, 1)
#         print('3 - ', temp_dict)
    #         for k, v in temp_dict.items():
    #             if k not in new_dict.keys():
    #                 new_dict[k] = [value]
    #             else:
    #                 new_dict[k].append(value)
    #             print(v)
    # else:
    #     if key not in new_dict.keys():
    #         new_dict[key] = [value]
    #     else:
    #         new_dict[key].append(value)

# temp_dict = {}
# for i, el1 in enumerate(allwords):
#     print('1- ', el1)
#     small_dict = {}
#     for j, el2 in enumerate(allwords, start=i+1):
#         print('2- ', el2)
#         if len(el2) > 1:
#             if el1[0] == el2[0]:
#                 if el2[1] not in small_dict.keys():
#                     small_dict[el2[1]] = [" ".join(el2)]
#                 else:
#                     small_dict[el2[1]].append(" ".join(el2))
#
#             temp_dict[el1[0]] = [temp_dict]
#         else:
#             if el1[0] not in temp_dict.keys():
#                 temp_dict[el1[0]] = [" ".join(el1)]
#             else:
#                 temp_dict[el1[0]].append(" ".join(el1))
#
# print(temp_dict)

# for k, v in temp_dict.items():
#     for el in v:
#         print(k, '\t'*5, el)

#
# print('ID' + '\t'*10 + 'NAMES')
# print('+'*100)
#
# for k, v in temp_dict.items():
#     for el in v:
#         print(k, '\t'*5, el)



# with open('data/fierst.csv', mode='w', encoding='utf-8', newline='') as file:
#     file_writer = csv.writer(file, delimiter=',', lineterminator='\n')
#     file_writer.writerow(['id', 'names'])
#     for k, v in temp_dict.items():
#         for el in v:
#             file_writer.writerow((k, el))
#


#
# for k, v in temp_dict:
#     for el in v:
#         print(k, ' - ', el)
#



# temp_dict = {}
# for i, el1 in enumerate(allwords):
#     print(el1)
#     for j, el2 in enumerate(allwords, start=i+1):
#         print(el2)
#         temp_dict[el1[0]] = [el2]



#allwords = reduce(lambda x,y: x + y , [el[1].split(" ") for el in vals])
# my_array = pyexcel.get_array(file_name=file_name)

# my_dict = pyexcel.get_dict(file_name=file_name, name_columns_by_row=0)
# book_dict = pyexcel.get_book_dict(file_name=file_name)
# print(book_dict[0:10])
# # for el in book_dict:
# #     print(book_dict['1'])
#
# for cellObj in sheet['A1':'C3']:
#       for cell in cellObj:
#               print(cells.coordinate, cells.value)
#       print('--- END ---')


#
# new_dict = {}
# for key, value in fierst_dict.items():
#     print('0 - ', value)
#     if len(value) > 1:
#         word_list = [el.split(",") for el in value]
#         print('1 - ', word_list)
#         if len(value[1]) > 1:
#             print('2 - ', [el[0].split(' ') for el in word_list])
#             # temp_dict = dublicated([el[1].split(" ") for el in word_list])
            # print('3 - ', temp_dict)
    #         for k, v in temp_dict.items():
    #             if k not in new_dict.keys():
    #                 new_dict[k] = [value]
    #             else:
    #                 new_dict[k].append(value)
    #             print(v)







#
# outfile = open('data.csv', 'w')
# writer = csv.writer(outfile, delimiter=';', quotechar='"')
# writer.writerows(data)
# outfile.close()


# df = pd.read_excel('data/НСИ - закупки.xlsx')
# print(df)
# file = 'data/НСИ - закупки.xlsx'
# x1 = pd.ExcelFile(file)
#
# print(x1.sheet_names)
# df1 = x1.parse('1')
# print(df1)

# wb = load_workbook('data/НСИ - закупки.xlsx')
# print(wb.sheetnames)
# sheet = wb['Оглавление']
# sheet.title


# def tree(self):
#     db_tree = [
#         {"id": 2, "parent_id": 1, "level": 1, "name": "parent 1"},
#         {"id": 5, "parent_id": 2, "level": 2, "name": "child 1 - 1"},
#         {"id": 6, "parent_id": 2, "level": 2, "name": "child 1 - 2"},
#         {"id": 9, "parent_id": 2, "level": 2, "name": "child 1- 3"},
#         {"id": 7, "parent_id": 5, "level": 3, "name": "child 1 - 1 - 1"},
#         {"id": 11, "parent_id": 6, "level": 3, "name": "children 2- 1"},
#         {"id": 10, "parent_id": 7, "level": 4, "name": "child 4 levl parent 1"},
#         {"id": 3, "parent_id": 1, "level": 1, "name": "parent 2"},
#         {"id": 13, "parent_id": 3, "level": 2, "name": "parent 2- 1 - chil"},
#         {"id": 4, "parent_id": 1, "level": 1, "name": "parent 3"},
#         {"id": 8, "parent_id": 1, "level": 1, "name": "parent 4"}
#     ]
#     db_tree = self.buildTree(db_tree)
#     return db_tree
#
#
# # Строит узел дерева
# def buildTree(self, db_tree):
#     tree = {}
#     index = {row["id"]: row for row in db_tree}
#     for row in db_tree:
#         self.processRowTree(row, index, tree)
#     return tree
#
#
# # Строит строку узла дерева
# def processRowTree(self, row, index, tree):
#     if row is None:
#         return tree
#     parent = index.get(row["parent_id"], None)
#     subtree = self.processRowTree(parent, index, tree)
#     if row["name"] not in subtree:
#         subtree[row["name"]] = {}
#
#     return subtree[row["name"]]


# N = np.zeros([len(count_word),len(count_word)])
# print(N)



# dict_word = {}
# for el in tmp_text.split('.'):
#     for symb in el.lower().split(' '):
#         if symb not in dict_word.keys():
#             if len(symb) > 3:
#                 dict_word[symb] = el + '.'
#         else:
#             dict_word[symb] += el + '.'
#
