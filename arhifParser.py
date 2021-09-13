# from settings import *
# from function import *
#
# pd.set_option('display.max_columns', None)
#
# nlp = spacy.load("ru_core_news_lg")
#
# # stop_words = nltk.corpus.stopwords.words('russian')
#
# file_name="data/НСИ - закупки.xlsx"
# rb = xlrd.open_workbook(file_name)
# sheet = rb.sheet_by_index(1)
#
# #получаем список значений из всех записей
# vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
#
# print_border('СИНТАКТИЧЕСКИЙ РАЗБОР SPACY')
# text = []
# for el in vals[1:]:
#     el[1].replace('-', '')
#     text.append(el[1].replace('\n', '').replace('-', '_'))
# # print('text  -', text)
# # print('len(text) -', len(text))
# print_border('СОСТАВЛЕНИЕ ПРЕДЛОЖЕНИЙ')
# test_text = reduce(lambda x, y: x + '. ' + y, text)
#
# #
# #
# # print('test_text  -', test_text)
# # print('type(test_text) -', type(test_text))
#
#
# print_border('КОНЕЦ СИНТАКТИЧЕСКОГО РАЗБОРА SPACY')
# #
# # tmp_text = 'Анестезиологические и респираторные медицинские изделия. Ортопедические медицинские изделия. ' \
# #            'Стерилизаторы и сопутствующие изделия. Офтальмологические медицинские изделия. Офтальмологические лазерные системы. ' \
# #            'Ламинарные системы. Сетки хирургические и сопутствующие изделия. Матрасы медицинские и сопутствующие изделия. ' \
# #            'Радиологические медицинские изделия. Медицинские изделия для анализа гемодинамики. ' \
# #            'Медицинские изделия для сердечно-сосудистой хирургии. Экспресс-тесты. Мониторы/мониторные системы гастроэнтерологические. ' \
# #            'Системы электростимуляции центральной нервной системы'
#
# # print(tmp_text)
# # print(type(tmp_text))
#
# #Анализ частоты слова
# # tmp = tmp_text.replace('.', '').lower().split()
# tmp = test_text.replace('.', '').lower().split()
# # print(tmp)
# # print(type(tmp))
# count_word = Counter(tmp)
# # print(count_word)
#
# t_count = max(count_word, key=count_word.get)
# # print(len(t_count))
#
# t_unic = {el for el in tmp if len(el) > 3}
# # print(t_unic)
# # print(len(t_unic))
#
#
# def parsSent(sent):
#     if sent[-2].dep_ == 'ROOT' and sent[-2].pos_ == 'NOUN':
#         return sent[-2].test
#
#
#
# dataSet = pd.DataFrame(0, index=t_unic, columns=t_unic)
# # print(dataSet)
# # print('3 - ', symb)
# dict_word = {}
# for el in test_text.split('.'):
#     for symb in el.lower().split(' '):
#         if symb not in dict_word.keys():
#             if len(symb) > 3:
#                 dict_word[symb] = [el + '.']
#         else:
#             dict_word[symb].append(el + '.')
#
#
# # print(dict_word)
# # sort_list = []
# for k, v in dict(sorted(dict_word.items(), key=lambda x: len(x[1]), reverse=False)).items():
#     # if len(v) > 1:
#     #     if dict_word[k][0] in dict_word[root_count]:
#
#     print(k, ' - ', len(v), v)
#
# # print(dict_word['стерилизаторы'][0] in dict_word['изделия'])
# print_border('КОНЕЦ СИНТАКТИЧЕСКОГО РАЗБОРА SPACY')
#
#
#
# for k, v in {k: v for k, v in dict_word.items() if len(v) == max([len(v) for _, v in dict_word.items()])}.items():
#     root_count = k
# print(root_count)
#
# print(dict_word)
#
#
#
#
#
# # tree = Tree()
# # tree.create_node(max(dict_word, key=dict_word.get).title(), max(dict_word, key=dict_word.get))  # root node
# #
# # for k, v in dict_word.items():
# #     if k != root_count:
# #         if dict_word[k][0] in dict_word[root_count]:
# #             if len(v) > 1:
# #                 tree.create_node(k.title(), k, parent=root_count)
# #                 for el in v:
# #                     tree.create_node(el, parent=k)
# #
# # tree.show()
#
# ##############################################################################
# #                                  ВАРИАНТ 5                                 #
# ##############################################################################
# #
#
# # tree = Tree()
# # tree.create_node("Harry", "harry")  # root node
# # tree.create_node("Jane", "jane", parent="harry")
# # tree.create_node("Bill", "bill", parent="harry")
# # tree.create_node("Diane", "diane", parent="jane")
# # tree.create_node("Mary", "mary", parent="diane")
# # tree.create_node("Mark", "mark", parent="jane")
# # tree.show()
# #
# #
# # new_tree = Tree()
# # new_tree.create_node("n1", 1)  # root node
# # new_tree.create_node("n2", 2, parent=1)
# # new_tree.create_node("n3", 3, parent=1)
# # tree.paste('bill', new_tree)
# # tree.show()
#
#
#
#
#
#
#
#
# # root_count = max(dict_word, key=dict_word.get)
# # root_count = max(dict_word.items(), key = lambda x: x[1])[0]
# # print(root_count)
# # tree = Tree()
# # tree.create_node(max(dict_word, key=dict_word.get).title(), max(dict_word, key=dict_word.get))  # root node
# #
# # for k, v in dict_word.items():
# #     if k != root_count:
# #         if dict_word[k][0] in dict_word[root_count]:
# #             if len(v) > 1:
# #                 tree.create_node(k.title(), k, parent=root_count)
# #                 for el in v:
# #                     tree.create_node(el, parent=k)
# #
# # tree.show()
#
#
#
#
# ##############################################################################
# #                                  ВАРИАНТ 4                                 #
# ##############################################################################
# #
#
# # #Формирование таблицы смещения
# # t = max(count_word, key=count_word.get)
# #
# # S = set()   # Уникадбные символы в образцу
# # M = len(t)  # Число символов в образце
# # d ={}       # Словарь смещений
# #
# # for i in range(M - 2, -1, -1):  # Итерации с предпоследнего символа
# #     if t[i] not in S:           # если символ еще не добавлен в таблицу
# #         d[t[i]] = M - i - 1
# #         S.add(t[i])
# #
# # if t[M - 1] not in S:          # Отдельно формируем последний символ
# #     d[t[M-1]] = M
# #
# # d['*'] = M                     # смещение для прочих символов
# #
# # print(d)
# #
# #
# # #Поиск образца в строке
# #
# # a = tmp_text
# # N = len(a)
# #
# # if N >= M:
# #     i = M - 1
# #     while i < N:
# #         k = 0
# #         for j in range(M - 1, -1, -1):
# #             if a[i-k] != t[j]:
# #                 if j == M - 1:
# #                     off = d[a[i]] if d.get(a[i], False) else d['*']
# #                 else:
# #                     off = d[t[j]]
# #                 i += off
# #                 break
# #             k += 1
# #         if j == 0:
# #             print(f"Образец найден по индексу {i - k + 1}")
# #             break
# #
# # else:
# #     print("Образец не найден.")
#
#
#
# # doc = nlp(test_text)
#
# # print(doc)
# # print(type(doc))
#
# # doc = nlp(test_text)
#
#
# # spans = list(doc.sents)
# # print(spans)
#
# # for el in doc:
# #     print(el)
#
# # spans = doc.sents
# # print(spans)
#
# # doc.user_data["title"] = "Это заголовок"
# # options = {'compact': True, 'font': "Tahoma"}
# # displacy.serve(spans, style='dep', options=options, host='localhost')
#
# ##############################################################################
# #                                  ВАРИАНТ 3                                 #
# ##############################################################################
# #
#
# # for sent1 in spans[:-1]:
# #     temp = []
# #     print('sent1 - ', sent1)
# #     for sent2 in spans[spans.index(sent1) + 1:]:
# #         print('\t\t\tsent2 - ', sent2)
#
# # temp_dict = {}
# # for sent in spans:
# #     print(sent[-2])
# #     root_phrase = ''
# #     amod_phrase = ''
# #     if sent[-2].dep_ == 'ROOT' and sent[-2].pos_ == 'NOUN':
# #         if sent[-2].text not in temp_dict:
# #             temp_dict[sent[-2].text] = [sent.text]
# #         else:
# #             temp_dict[sent[-2].text].append(sent.text)
# #
# # for k, v in temp_dict.items():
# #     print(k, v)
#
#
#
# # def parseSent(sent):
# #
# #     root_phrase = ''
# #     amod_phrase = ''
# #     nmod_phrase = ''
# #     nmod_phrase_all = ''
# #     list_root_word = []
# #
# #     if sent[-2].dep_ == 'ROOT' and sent[-2].pos_ == 'NOUN':
# #         root_phrase = root_phrase + ' ' + sent[-2].text
# #         if sent[-3].dep_ == 'amod' and sent[-3].pos_ == 'ADJ':
# #             amod_phrase_all = ''
# #             for word in sent[-2].lefts:
# #                 if word.dep_ == 'amod' and word.pos_ == 'ADJ':
# #                     amod_phrase_all = amod_phrase_all.rstrip() + ' ' + word.text
# #
# #             list_root_word.append((amod_phrase_all + root_phrase, amod_phrase_all.split(' ')[-1] + root_phrase ))
# #
# #     return list_root_word
# #
# # list_root_fierst = []
# # list_root_second = []
# # temp_list = {}
# # big_temp_list = []
# # for sent1 in spans[:-1]:
# #     temp = []
# #     if len(sent1.text.split()) > 1:
# #         list_root_fierst = parseSent(sent1)
# #         if len(list_root_fierst) > 0:
# #             for sent2 in spans[spans.index(sent1) + 1:]:
# #                 if len(sent2.text.split()) > 1:
# #                     list_root_second = parseSent(sent1)
# #                     if len(list_root_second) > 0:
# #                         if float(sent1.similarity(sent2)) > 0.8:
# #                             if list_root_fierst[0][1] not in temp_list.keys():
# #                                 print('list_root_second_1 - ', list_root_fierst[0][1])
# #                                 temp_list[list_root_fierst[0][1]] = [sent1.text]
# #                             else:
# #                                 temp_list[list_root_fierst[0][1]].append(sent1.text)
# #
# #
# #                             if list_root_second[0][1] not in temp_list.keys():
# #                                 print('list_root_second_2 - ', list_root_second[0][1])
# #                                 temp_list[list_root_second[0][1]] = [sent2.text]
# #                             else:
# #                                 temp_list[list_root_second[0][1]].append(sent2.text)
# #
# #
# #
# #
# #
# #
# #
# # for k, v in temp_list.items():
# #     print(k, v)
#
#
# #
# # tree = Tree()
# # tree.create_node("Harry", "harry")  # root node
# # tree.create_node("Jane", "jane", parent="harry")
# # tree.create_node("Bill", "bill", parent="harry")
# # tree.create_node("Diane", "diane", parent="jane")
# # tree.create_node("Mary", "mary", parent="diane")
# # tree.create_node("Mark", "mark", parent="jane")
# # tree.show()
#
#
#
#
#
#
# # doc1 = 'Анестезиологические и респираторные медицинские изделия.'
# # doc2 = 'Ортопедические медицинские изделия.'
# # doc3 = 'Офтальмологические медицинские изделия.'
# # doc4 = 'Медицинские изделия для анализа гемодинамики'
# # doc5 = 'Медицинские изделия для кардиореанимации'
# #
# # doc1 = nlp(doc1)
# # doc2 = nlp(doc2)
# # doc3 = nlp(doc3)
# # doc4 = nlp(doc4)
# # doc5 = nlp(doc5)
# # print('1 - 2', doc1.similarity(doc2))
# # print('1 - 3', doc1.similarity(doc3))
# # print('1 - 4', doc1.similarity(doc4))
# # print('2 - 3', doc2.similarity(doc3))
# # print('2 - 4', doc2.similarity(doc4))
# # print('3 - 4', doc3.similarity(doc4))
# # print('4 - 5', doc4.similarity(doc5))
# # print('1 - 5', doc1.similarity(doc5))
#
#
#
# # comb_word = ''
# # comb_word_all = ''
# # list_root_word1 = []
# # list_root_word2 = []
# # for i, sents in enumerate(doc.sents):
# #     for
# #     # print(sents.text.split())
# #     # print(len(sents.text.split()))
# #     # print(sents[-2])
# #     if len(sents.text.split()) > 1:
# #         root_phrase = ''
# #         amod_phrase = ''
# #         nmod_phrase = ''
# #
# #         nmod_phrase_all = ''
# #
# #         if sents[-2].dep_ == 'ROOT' and sents[-2].pos_ == 'NOUN':
# #             # print(sents)
# #             # print(sents[-2])
# #             # print([w for w in sents[-2].lefts])
# #             # print(len([w for w in sents[-2].lefts]))
# #             root_phrase = root_phrase + ' ' + sents[-2].text
# #             # temp_word = root_phrase
# #             # print(phrase.strip())
# #             if sents[-3].dep_ == 'amod' and sents[-3].pos_ == 'ADJ':
# #                 # print([w for w in sents[-2].lefts])
# #                 amod_phrase_all = ''
# #                 for word in sents[-2].lefts:
# #                     # print(word)
# #                     if word.dep_ == 'amod' and word.pos_ == 'ADJ':
# #                         # print(word.text)
# #                         amod_phrase_all = amod_phrase_all + ' ' + word.text
# #
# #                 list_root_word1.append(amod_phrase_all + root_phrase)
# #
# # for el in list_root_word1:
# #     print(el)
#
#
#
#
#
#
# #
# # temp_list = []
# # for sent1 in spans[:-1]:
# #     temp = []
# #     for sent2 in spans[spans.index(sent1) + 1:]:
# #         print(float(sent1.similarity(sent1)) - float(sent1.similarity(sent2)))
# #         if float(sent1.similarity(sent2)) > 0.8:
# #             if sent1 not in temp_list:
# #                 temp_list.append(sent1)
# #
# #             if sent2 not in temp_list:
# #                 temp.append(sent2)
# #
# #
# #     if len(temp) != 0:
# #         temp_list.extend(temp)
# #
# #
# # for el in temp_list:
# #     print(el)
# #
# #
#
#
#
#
#
#
# # options = {'compact': True, 'font': "Tahoma"}
# # displacy.serve(spans, style='dep', options=options, host='localhost')
# #
#
# ##############################################################################
# #                                  ВАРИАНТ 2                                 #
# ##############################################################################
#
# # comb_word = ''
# # comb_word_all = ''
# # list_root_word1 = []
# # list_root_word2 = []
# # for i, sents in enumerate(doc.sents):
# #     # print(sents.text.split())
# #     # print(len(sents.text.split()))
# #     # print(sents[-2])
# #     if len(sents.text.split()) > 1:
# #         root_phrase = ''
# #         amod_phrase = ''
# #         nmod_phrase = ''
# #
# #         nmod_phrase_all = ''
# #
# #         if sents[-2].dep_ == 'ROOT' and sents[-2].pos_ == 'NOUN':
# #             # print(sents)
# #             # print(sents[-2])
# #             # print([w for w in sents[-2].lefts])
# #             # print(len([w for w in sents[-2].lefts]))
# #             root_phrase = root_phrase + ' ' + sents[-2].text
# #             # temp_word = root_phrase
# #             # print(phrase.strip())
# #             if sents[-3].dep_ == 'amod' and sents[-3].pos_ == 'ADJ':
# #                 # print([w for w in sents[-2].lefts])
# #                 amod_phrase_all = ''
# #                 for word in sents[-2].lefts:
# #                     # print(word)
# #                     if word.dep_ == 'amod' and word.pos_ == 'ADJ':
# #                         # print(word.text)
# #                         amod_phrase_all = amod_phrase_all + ' ' + word.text
# #
# #                 list_root_word1.append(amod_phrase_all + root_phrase)
# #
# # for el in list_root_word1:
# #     print(el)
#
#         # if amod_phrase_all != '':
#         #     comb_word_all = amod_phrase_all + ' ' + root_phrase
#         #     print(comb_word_all)
#         # else:
#         #     comb_word_all = root_phrase + ' ' + nmod_phrase_all
#         #     print(comb_word_all)
#
#         # comb_word = amod_phrase + ' ' + root_phrase
#         # comb_word_all = amod_phrase_all + ' ' + root_phrase
#
#
#         # print(comb_word)
#         # print(comb_word_all)
# # print('list_root_word1 - ', list_root_word1)
# # print('list_root_word2 - ', list_root_word2)
# #
# # temp_text = reduce(lambda x, y: x + ', ' + y, list_root_word1)
# # print(temp_text)
#
# # count = Counter(list_root_word1)
# # print(count)
# # temp_text.split()
# # options = {'compact': True, 'font': "Tahoma"}
# # displacy.serve(spans, style='dep', options=options, host='localhost')
# #
#
#
# ##############################################################################
# #                                  ВАРИАНТ 1                                 #
# ##############################################################################
# # comb_word = ''
# # comb_word_all = ''
# # list_root_word1 = []
# # list_root_word2 = []
# # for token in doc:
# #     root_phrase = ''
# #     amod_phrase = ''
# #     nmod_phrase = ''
# #     amod_phrase_all = ''
# #     nmod_phrase_all = ''
# #     # if token.pos_ == 'NOUN':
# #     #     phrase = phrase + ' ' +token.text
# #     if token.dep_ == 'ROOT' and token.pos_ == 'NOUN':
# #         root_phrase = root_phrase + ' ' + token.text
# #         temp_word = root_phrase
# #         # print(phrase.strip())
# #         for word in token.children:
# #             # print(word)
# #             if word.dep_ == 'amod' and word.pos_ == 'ADJ':
# #                 amod_phrase = word.text
# #                 amod_phrase_all = amod_phrase_all + ' ' + word.text
# #
# #             list_root_word1.append(amod_phrase + ' ' + temp_word)
# #
# #             if word.dep_ == 'nmod' and word.pos_ == 'NOUN':
# #                 nmod_phrase = word.text
# #                 nmod_phrase_all = nmod_phrase_all + ' ' + word.text
# #
# #             list_root_word2.append(temp_word + ' ' + nmod_phrase)
# #
# #         if amod_phrase_all != '':
# #             comb_word_all = amod_phrase_all + ' ' + root_phrase
# #             print(comb_word_all)
# #         else:
# #             comb_word_all = root_phrase + ' ' + nmod_phrase_all
# #             print(comb_word_all)
#
#
#
# ##############################################################################
# #                                  ВАРИАНТ 2                                 #
# ##############################################################################
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # comb_token = syntax_parsing(text, nlp)
# #
# #
# # for el in comb_token:
# #     print(el)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # #Очистка и токенизация текста
# # allwords = [el[1].replace('\n', '').split(" ") for el in vals[1:]]
# # print('allwords -', allwords)
# # print('1.1 -', len(allwords))
# #
# # #Очистка и токенизация текста с учетом стоп-слов
# # processed_data = []
# # processed_data_all = []
# # for doc in vals[1:]:
# #     tokens = preprocess_text(doc, stop_words)
# #     processed_data.append(tokens)
# #     processed_data_all += tokens
# #
# # print('processed_data -', processed_data)
# # print('2.1 -', len(processed_data))
#
# # for el in processed_data:
# #     print(el)
#
#
# #
# # temp_res = [' '.join(el) for el in processed_data]
# #
# # tfidf_vectorizer = TfidfVectorizer(max_df=1.0,
# #                                    max_features=2500,
# #                                    min_df=0.0,
# #                                    use_idf=True,
# #                                    ngram_range=(1, 3))
# #
# # tfidf_matrix = tfidf_vectorizer.fit_transform(temp_res)
# #
# #
# # features = tfidf_vectorizer.get_feature_names()
# # indices = zip(*tfidf_matrix.nonzero())
# # print(features)
# # # data_list = {}
# # # for row, column in indices:
# # #     if row not in data_list.keys():
# # #         data_list[row] = [(features[column], tfidf_matrix[row, column], row)]
# # #     else:
# # #         data_list[row].append((features[column], tfidf_matrix[row, column], row))
# #
# #
# # dense = tfidf_matrix.todense()
# # print(dense.shape)
# # vectorizer = TfidfVectorizer()
# # X = vectorizer.fit_transform(temp_res)
# #
# # dataSet = pd.DataFrame(data=X.todense(), columns=vectorizer.get_feature_names())
# # dataSet["Class"] = [el for el in range(1, (len(dataSet.index)) + 1)]
# # # print(dataSet)
# # # print(dataSet.shape)
# #
# # X = dataSet.drop('Class', axis=1)
# # y = dataSet['Class']
# #
# #
# # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
# #
# # classifier = DecisionTreeClassifier()
# # classifier.fit(X_train, y_train)
# #
# # y_pred = classifier.predict(X_test)
# #
#
#
#
# # clf = tree.DecisionTreeClassifier()
# # clf = clf.fit(X, y)
#
#
#
# #
# # all_concept = []
# # for k, v in data_list.items():
# #     # print(k, ' - ', sorted(v, key=lambda x: x[1], reverse=True))
# #     all_concept.extend(v)
# #
# #
# # # print(all_concept)
# #
# # # print(len(all_concept))
# #
# # voc = [ el[0] for el in sorted(all_concept, reverse=False) ]
# # voc2 = sorted(list(set(voc)), reverse=False)
# # voc_lib = {}
# # for i, el in enumerate(voc2, start=1):
# #     voc_lib[el] = i
#
# # for k, v in voc_lib.items():
# #     print(k, ' - ', v)
#
#
# # new_all_concept = []
# # for el in all_concept:
# #     new_all_concept.append((voc_lib[el[0]], *el))
# #
# # new_all_concept_sort = sorted(new_all_concept, key=lambda x: x[0], reverse=False)
#
# # for el in new_all_concept_sort:
# #     print(el)
#
# #
# # print_border('СИНТАКТИЧЕСКИЙ РАЗБОР SPACY')
# #
# # # doc = nlp('Анестезиологические и респираторные медицинские изделия. Ортопедические медицинские изделия. '
# # #           'Офтальмологические медицинские изделия. '
# # #           'Радиологические медицинские изделия')
# # # spans = list(doc.sents)
# # # displacy.serve(spans, style='dep', host='localhost')
# #
# # # comb_token = syntax_parsing(text, nlp)
# # #
# # #
# # # for el in comb_token:
# # #     print(el)
#
#
#
# #
# # temp_list = []
# # for sent1 in spans[:-1]:
# #     temp = []
# #     for sent2 in spans[spans.index(sent1) + 1:]:
# #         print(sent1)
# #         print(sent2)
# #         print(sent1.similarity(sent2))
# #         print(type(float(sent1.similarity(sent2))))
# #         print('-' * 50)
# #         print(float(sent1.similarity(sent1)) - float(sent1.similarity(sent2)))
# #         if float(sent1.similarity(sent2)) > 0.8:
# #             if sent1 not in temp_list:
# #                 temp_list.append(sent1)
# #
# #             if sent2 not in temp_list:
# #                 temp.append(sent2)
# #
# #
# #     if len(temp) != 0:
# #         temp_list.extend(temp)
# #
# #
# # for el in temp_list:
# #     print(el)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # count_lib = counterConcept(new_all_concept_sort, voc_lib)
# #
# # for k, v in sorted(count_lib.items(), key=lambda x: x[1], reverse=True):
# #     print(k, ' - ', v)
#
# # for el in sorted(all_concept, key=lambda x: x[0], reverse=False):
# #     print(el)
#
# # #
# # #
# # def compute_tfidf(corpus):
# #     def compute_tf(text):
# #         tf_text = Counter(text)
# #         for i in tf_text:
# #             tf_text[i] = tf_text[i] / float(len(text))
# #
# #         return tf_text
# #
# #     def compute_idf(word, corpus):
# #         return math.log10(len(corpus) / sum([1.0 for i in corpus if word in i]))
# #
# #     documents_list = []
# #     for text in corpus:
# #         tf_idf_dictionary = {}
# #         computed_tf = compute_tf(text)
# #         for word in computed_tf:
# #             tf_idf_dictionary[word] = computed_tf[word] * compute_idf(word, corpus)
# #             documents_list.append(tf_idf_dictionary)
# #
# #     return documents_list
# #
# #
# #
# # result = compute_tfidf(processed_data)
# # result2 = {}
# # for el in result:
# #     for k, v in el.items():
# #         if k not in result2.keys():
# #             result2[k] = v
# #
# #
# # print(result2)
# # res = [(k, result2[k]) for k in sorted(result2, key=result2.get, reverse=True)]
# # for k, v in res:
# #     print(k, v)
# #
# # print(len(result))
# # print(len(result2))
#
#
#
# # print(list([[].append(x) for x, y in zip(result[:-1], result[1:]) if x == y]))
#
# #
# # fierst_dict = {}
# # second_dict = {}
# #
# # for i, el in enumerate(processed_data):
# #     # print('3.0 -', el)
# #     if el[0] not in fierst_dict.keys():
# #         fierst_dict[el[0]] = [" ".join(allwords[i])]
# #         second_dict[el[0]] = [el[1:]]
# #     else:
# #         fierst_dict[el[0]].append(" ".join(allwords[i]))
# #         second_dict[el[0]].append(el[1:])
# #
# # print('3.1 -', fierst_dict)
# # print('3.2 -', second_dict)
# #
# #
# # big_dict = {}
# # big_dict2 = {}
# # for key, value in second_dict.items():
# #     temp_dict = dublicated(value)
# #     print('4.0 -', temp_dict)
#
#
#
#
#
#
# # def dublicated(allwords):
# #     temp_dict = {}
# #     for i, el in enumerate(allwords):
# #         if len(el) > 1:
# #             if len(el[1]) > 1:
# #                 if
# #                 if el[1] not in temp_dict.keys():
# #                     temp_dict[el[1]] = [" ".join(el)]
# #                 else:
# #                     temp_dict[el[1]].append(" ".join(el))
# #         else:
# #             return el
# #     return temp_dict
#
#
#
# # def dublicated(allwords):
# #     temp_list = [set(el) for el in allwords]
# #     res = list([x & y for x, y in zip(temp_list[:-1], temp_list[1:])])
# #
# #     print(res)
#
#
#
#
#
# # b = list(itertools.combinations(allwords, 2))
# # res = [x for x in b if x[0] in x[1]]
# # def dublicated(allwords):
# #     new_list = []
# #     for el1 in allwords[:len(allwords)-1]:
# #         if len(el1) > 1:
# #             temp_list = []
# #             temp_dict = {}
# #             for el2 in allwords[1:len(allwords)]:
# #                 if len(el2[1]) > 3:
# #                     if el1[1] == el2[1]:
# #                         if el1[1] not in temp_dict.keys():
# #                             temp_dict[el1[1]] = [el1]
# #                         else:
# #                             temp_dict[el[1]].append(el1)
# #                     else:
# #                         temp_list.append(el2)
# #                 else:
# #                     temp_list.append(el2)
# #
# #                 temp_list.append(el1)
# #
# #             if len(temp_dict) > 0:
# #                 new_list.append(temp_dict)
# #
# #             new_list.append(temp_list)
# #
# #         else:
# #             new_list = allwords
# #     return new_list
#
#
#
#
# # def dublicated(allwords):
# #     new_list = []
# #     for el1 in allwords[:len(allwords)]:
# #         if len(el1) > 1:
# #             temp_dict = {}
# #             temp_list = []
# #             for el2 in allwords[1:len(allwords)]:
# #                 if len(el2[1]) > 3:
# #                     if el1[1] == el2[1]:
# #                         if el1[1] not in temp_dict.keys():
# #                             temp_dict[el1[1]] = [el1]
# #                         else:
# #                             temp_dict[el[1]].append(el1)
# #                     else:
# #                         temp_list.append(el2)
# #                 else:
# #                     temp_list.append(el2)
# #             if len(temp_dict) > 0:
# #                 new_list.append(temp_dict)
# #
# #             new_list.append(temp_list)
# #
# #         else:
# #             new_list = allwords
# #     return new_list
#
#
# # fierst_dict = {}
# # second_dict = {}
# #
# # for i, el in enumerate(processed_data):
# #     # print('3.0 -', el)
# #     if el[0] not in fierst_dict.keys():
# #         fierst_dict[el[0]] = [" ".join(allwords[i])]
# #         second_dict[el[0]] = [el[1:]]
# #     else:
# #         fierst_dict[el[0]].append(" ".join(allwords[i]))
# #         second_dict[el[0]].append(el[1:])
# #
# # print('3.1 -', fierst_dict)
# # print('3.2 -', second_dict)
# #
# #
# # big_dict = {}
# # big_dict2 = {}
# # for key, value in second_dict.items():
# #     temp_dict = dublicated(value)
# #     print('4.0 -', temp_dict)
#
#
#     # for i, el1 in enumerate(value):
#     #     for j, el2 in enumerate(value, i+1):
#     #         print('4.0.1 -', el1)
#     #         print('4.0.2 -', el2)
#     #         if el1[0] == el2[0]:
#     #             if len(el2) > 1:
#     #                 if el1[1] == el2[1]:
#     #                     if el2[1] not in temp_dict.keys():
#     #                         temp_dict[el2[1]] = [" ".join(allwords[j])]
#     #                         temp_dict2[el2[1]] = [el2]
#     #                     else:
#     #                         temp_dict[el2[1]].append(" ".join(allwords[j]))
#     #                         temp_dict2[el2[1]].append(el2)
#     #                 else:
#     #                     if el2[1] not in temp_dict.keys():
#     #                         temp_dict[el2[1]] = [" ".join(allwords[j])]
#     #                         temp_dict2[el2[1]] = [el2]
#     #                     else:
#     #                         temp_dict[el2[1]].append(" ".join(allwords[j]))
#     #                         temp_dict2[el2[1]].append(el2)
#     #
#     #
#     # if key not in big_dict.keys():
#     #     big_dict[key] = [temp_dict]
#     #     big_dict2[key] = [temp_dict2]
#     # else:
#     #     big_dict[key].append(temp_dict)
#     #     big_dict2[key].append(temp_dict2)
#
# # print('4.1 -', big_dict)
# # print('4.2 -', big_dict2)
# #
#
#
#
#
#
#
# # big_dict = {}
# # big_dict2 = {}
# # for key, value in second_dict.items():
# #     temp_dict = {}
# #     temp_dict2 = {}
# #     for i, el1 in enumerate(value):
# #         for j, el2 in enumerate(value, i + 1):
# #             print('4.0.1 -', el1)
# #             print('4.0.2 -', el2)
# #             if el1[0] == el2[0]:
# #                 if len(el2) > 1:
# #                     if el1[1] == el2[1]:
# #                         if el2[1] not in temp_dict.keys():
# #                             temp_dict[el2[1]] = [" ".join(allwords[j])]
# #                             temp_dict2[el2[1]] = [el2]
# #                         else:
# #                             temp_dict[el2[1]].append(" ".join(allwords[j]))
# #                             temp_dict2[el2[1]].append(el2)
# #                     else:
# #                         if el2[1] not in temp_dict.keys():
# #                             temp_dict[el2[1]] = [" ".join(allwords[j])]
# #                             temp_dict2[el2[1]] = [el2]
# #                         else:
# #                             temp_dict[el2[1]].append(" ".join(allwords[j]))
# #                             temp_dict2[el2[1]].append(el2)
# #
# #     if key not in big_dict.keys():
# #         big_dict[key] = [temp_dict]
# #         big_dict2[key] = [temp_dict2]
# #     else:
# #         big_dict[key].append(temp_dict)
# #         big_dict2[key].append(temp_dict2)
# #
# # print('4.1 -', big_dict)
# # print('4.2 -', big_dict2)
#
# # fierst_dict = {}
# # fierst_list = []
# # for i, el1 in enumerate(processed_data):
# #     for j, el2 in enumerate(processed_data, start=i+1):
# #         if el1[i][0] == el2[j][0]:
# #             fierst_list
#
#
#
#
#
#
#
# #
# # fierst_dict = dublicated(allwords, 0)
# # # print(fierst_dict)
# #
# # new_dict = {}
# # for key, value in fierst_dict.items():
# #     print('0 - ', value)
# #     if len(value) > 1:
# #         word_list = [el[0].split(' ') for el in [el.split(",") for el in value]]
# #         print('1 - ', word_list)
# #         temp_dict = dublicated(word_list, 1)
# #         print('3 - ', temp_dict)
#     #         for k, v in temp_dict.items():
#     #             if k not in new_dict.keys():
#     #                 new_dict[k] = [value]
#     #             else:
#     #                 new_dict[k].append(value)
#     #             print(v)
#     # else:
#     #     if key not in new_dict.keys():
#     #         new_dict[key] = [value]
#     #     else:
#     #         new_dict[key].append(value)
#
# # temp_dict = {}
# # for i, el1 in enumerate(allwords):
# #     print('1- ', el1)
# #     small_dict = {}
# #     for j, el2 in enumerate(allwords, start=i+1):
# #         print('2- ', el2)
# #         if len(el2) > 1:
# #             if el1[0] == el2[0]:
# #                 if el2[1] not in small_dict.keys():
# #                     small_dict[el2[1]] = [" ".join(el2)]
# #                 else:
# #                     small_dict[el2[1]].append(" ".join(el2))
# #
# #             temp_dict[el1[0]] = [temp_dict]
# #         else:
# #             if el1[0] not in temp_dict.keys():
# #                 temp_dict[el1[0]] = [" ".join(el1)]
# #             else:
# #                 temp_dict[el1[0]].append(" ".join(el1))
# #
# # print(temp_dict)
#
# # for k, v in temp_dict.items():
# #     for el in v:
# #         print(k, '\t'*5, el)
#
# #
# # print('ID' + '\t'*10 + 'NAMES')
# # print('+'*100)
# #
# # for k, v in temp_dict.items():
# #     for el in v:
# #         print(k, '\t'*5, el)
#
#
#
# # with open('data/fierst.csv', mode='w', encoding='utf-8', newline='') as file:
# #     file_writer = csv.writer(file, delimiter=',', lineterminator='\n')
# #     file_writer.writerow(['id', 'names'])
# #     for k, v in temp_dict.items():
# #         for el in v:
# #             file_writer.writerow((k, el))
# #
#
#
# #
# # for k, v in temp_dict:
# #     for el in v:
# #         print(k, ' - ', el)
# #
#
#
#
# # temp_dict = {}
# # for i, el1 in enumerate(allwords):
# #     print(el1)
# #     for j, el2 in enumerate(allwords, start=i+1):
# #         print(el2)
# #         temp_dict[el1[0]] = [el2]
#
#
#
# #allwords = reduce(lambda x,y: x + y , [el[1].split(" ") for el in vals])
# # my_array = pyexcel.get_array(file_name=file_name)
#
# # my_dict = pyexcel.get_dict(file_name=file_name, name_columns_by_row=0)
# # book_dict = pyexcel.get_book_dict(file_name=file_name)
# # print(book_dict[0:10])
# # # for el in book_dict:
# # #     print(book_dict['1'])
# #
# # for cellObj in sheet['A1':'C3']:
# #       for cell in cellObj:
# #               print(cells.coordinate, cells.value)
# #       print('--- END ---')
#
#
# #
# # new_dict = {}
# # for key, value in fierst_dict.items():
# #     print('0 - ', value)
# #     if len(value) > 1:
# #         word_list = [el.split(",") for el in value]
# #         print('1 - ', word_list)
# #         if len(value[1]) > 1:
# #             print('2 - ', [el[0].split(' ') for el in word_list])
# #             # temp_dict = dublicated([el[1].split(" ") for el in word_list])
#             # print('3 - ', temp_dict)
#     #         for k, v in temp_dict.items():
#     #             if k not in new_dict.keys():
#     #                 new_dict[k] = [value]
#     #             else:
#     #                 new_dict[k].append(value)
#     #             print(v)
#
#
#
#
#
#
#
# #
# # outfile = open('data.csv', 'w')
# # writer = csv.writer(outfile, delimiter=';', quotechar='"')
# # writer.writerows(data)
# # outfile.close()
#
#
# # df = pd.read_excel('data/НСИ - закупки.xlsx')
# # print(df)
# # file = 'data/НСИ - закупки.xlsx'
# # x1 = pd.ExcelFile(file)
# #
# # print(x1.sheet_names)
# # df1 = x1.parse('1')
# # print(df1)
#
# # wb = load_workbook('data/НСИ - закупки.xlsx')
# # print(wb.sheetnames)
# # sheet = wb['Оглавление']
# # sheet.title
#
#
# # def tree(self):
# #     db_tree = [
# #         {"id": 2, "parent_id": 1, "level": 1, "name": "parent 1"},
# #         {"id": 5, "parent_id": 2, "level": 2, "name": "child 1 - 1"},
# #         {"id": 6, "parent_id": 2, "level": 2, "name": "child 1 - 2"},
# #         {"id": 9, "parent_id": 2, "level": 2, "name": "child 1- 3"},
# #         {"id": 7, "parent_id": 5, "level": 3, "name": "child 1 - 1 - 1"},
# #         {"id": 11, "parent_id": 6, "level": 3, "name": "children 2- 1"},
# #         {"id": 10, "parent_id": 7, "level": 4, "name": "child 4 levl parent 1"},
# #         {"id": 3, "parent_id": 1, "level": 1, "name": "parent 2"},
# #         {"id": 13, "parent_id": 3, "level": 2, "name": "parent 2- 1 - chil"},
# #         {"id": 4, "parent_id": 1, "level": 1, "name": "parent 3"},
# #         {"id": 8, "parent_id": 1, "level": 1, "name": "parent 4"}
# #     ]
# #     db_tree = self.buildTree(db_tree)
# #     return db_tree
# #
# #
# # # Строит узел дерева
# # def buildTree(self, db_tree):
# #     tree = {}
# #     index = {row["id"]: row for row in db_tree}
# #     for row in db_tree:
# #         self.processRowTree(row, index, tree)
# #     return tree
# #
# #
# # # Строит строку узла дерева
# # def processRowTree(self, row, index, tree):
# #     if row is None:
# #         return tree
# #     parent = index.get(row["parent_id"], None)
# #     subtree = self.processRowTree(parent, index, tree)
# #     if row["name"] not in subtree:
# #         subtree[row["name"]] = {}
# #
# #     return subtree[row["name"]]
#
#
# # N = np.zeros([len(count_word),len(count_word)])
# # print(N)
#
#
#
# # dict_word = {}
# # for el in tmp_text.split('.'):
# #     for symb in el.lower().split(' '):
# #         if symb not in dict_word.keys():
# #             if len(symb) > 3:
# #                 dict_word[symb] = el + '.'
# #         else:
# #             dict_word[symb] += el + '.'
# #
#
#
# # -*- coding: utf8 -*-
# from settings import *
# from function import *
# from itertools import *
# from anytree import Node, NodeMixin, RenderTree
#
#
# pd.set_option('display.max_columns', None)
#
# nlp = spacy.load("ru_core_news_lg")
#
# file_name="data/НСИ - закупки.xlsx"
# rb = xlrd.open_workbook(file_name)
# sheet = rb.sheet_by_index(1)
#
# #Получаем список значений из всех записей
# vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
# print(vals)
#
# ###########Создание файла исходнйо таблицы#######################
#
# print_border('Загрузка данных из таблицы EXCEL')
# tuple_text = []
# for el in vals[1:]:
#     tuple_text.append((el[0], el[1].replace('\n', '').replace('-', '_')))
#
# print('text  -', tuple_text)
#
#
# with open('data/table_one.csv', mode='w', encoding='utf-8', newline='') as file:
#     file_writer = csv.writer(file, delimiter=',', lineterminator='\n')
#     file_writer.writerow(['id', 'code', 'name'])
#     for i, el in enumerate(tuple_text):
#         file_writer.writerow([i+1, el[0], el[1]])
# print_border('Загрузка данных из таблицы EXCEL завершена')
#
# # tuple_data = []
# # with open('data/table_one.csv', encoding='utf-8', newline='') as csvfile:
# #     reader_data = csv.reader(csvfile, delimiter=',')
# #     for row in reader_data:
# #         print(row)
# #         tuple_data.append(row)
#
# dict_data = []
# with open('data/table_one.csv', encoding='utf-8', newline='') as csvfile:
#     reader_dict = csv.DictReader(csvfile, delimiter=',')
#     for row in reader_dict:
#         print(row)
#         dict_data.append(row)
#
# print(dict_data)
# list_text = [el['name'] for el in dict_data]
# print(list_text)
# # print('len(text) -', len(text))
# # print_border('СОСТАВЛЕНИЕ ПРЕДЛОЖЕНИЙ')
# all_text = reduce(lambda x, y: x + '. ' + y, list_text)
# #
# print(all_text)
#
# # print_border('СИНТАКТИЧЕСКИЙ РАЗБОР SPACY')
# # text = []
# # for el in vals[1:]:
# #     el[1].replace('-', '')
# #     text.append(el[1].replace('\n', '').replace('-', '_'))
# # # print('text  -', text)
# # # print('len(text) -', len(text))
# # print_border('СОСТАВЛЕНИЕ ПРЕДЛОЖЕНИЙ')
# # test_text = reduce(lambda x, y: x + '. ' + y, text)
# #
# # # print('test_text  -', test_text)
# # # print('type(test_text) -', type(test_text))
# #
# # print_border('КОНЕЦ СИНТАКТИЧЕСКОГО РАЗБОРА SPACY')
# #
# #
# #
# #
# #
# # def change_list(array):
# #     dict_word = {}
# #     for el in array:
# #         # count_word = Counter(tmp)
# #         # # print(count_word)
# #         for symb in el.lower().split(' '):
# #
# #             if symb.rstrip(".") not in dict_word.keys():
# #                 if len(symb) > 3:
# #                     dict_word[symb.rstrip(".")] = [el]
# #             else:
# #                 dict_word[symb.rstrip(".")].append(el)
# #     return dict_word
# #
# #
# # def change_list2(array):
# #
# #     dict_word = {}
# #     for el in array:
# #         # count_word = Counter(tmp)
# #         # # print(count_word)
# #         for symb in el.lower().split(' '):
# #
# #             if symb.rstrip(".") not in dict_word.keys():
# #                 if len(symb) > 3:
# #                     dict_word[symb.rstrip(".")] = [el]
# #             else:
# #                 dict_word[symb.rstrip(".")].append(el)
# #     return dict_word
# #
# # # test_text = 'Дезинфицирующие салфетки для гигиенической обработки рук. Диспенсерная система с сухими салфетками. Дозатор. Жидкое мыло. Жидкое мыло антибактериальное. Кожный антисептик для гигиенической обработки рук. Кожный антисептик для обработки рук хирургов. Кожный антисептик окрашенный для операционного и инъекционного поля. Кондиционер для белья. Контроль качества предстерилизационной очистки изделий медицинского назначения. Контроль концентрации рабочего раствора ДС. Крем для рук. Обеззараживание медицинских отходов (объектов одноразового использования и биологического материала). Отбеливатель. Салфетки для обработки инъекционного поля. Сменный блок салфеток. Средство дезинфекции поверхностей (текущей и генеральных уборок, в том числе санитарно-технического оборудования). Средство для быстрой дезинфекции небольших поверхностей. Средство для ДВУ эндоскопов. Средство для дезинфекции белья ручным способом. Средство для дезинфекции и мытья посуды. Средство для дезинфекции ИМН, совмещенной с ПСО, ручным или механизированным способом. Средство для дезинфекции на пищеблоке. Средство для дезинфекции пищевого яйца. Средство для дезинфекции при особоопасных инфекциях. Средство для очистки воды бассейна. Средство для очистки медицинских изделий и эндоскопов на основе ферментов. Средство для химической стерилизации. Средство моющее для мытья посуды. Средство моющее для полов. Средство моющее для стекол. Средство чистящее для прочистки труб и канализации. Стиральный порошок.'
# # # test_text = 'Мышечная защита, накопление экссудата и болевой синдром; функциональные расстройства работы органов пищеварения и мочевыведения; общие признаки, обусловленные интоксикацией. Острая боль в животе – наиболее типичный признак развивающегося воспаления брюшины. Особенно сильно она проявляется при перфоративных перитонитах. При воспалении, не связанном с нарушением целостности стенок внутренних органов, боли менее выражены, усиливаются постепенно. Разрыв (перфорация) стенки полого органа обычно отдаёт резкой, простреливающей болью, которая похожа на колющий удар или выстрел из пистолета. После такого больной стремится лечь и не двигаться, так как малейшее движение причиняет сильною боль. Болезненно также сотрясание брюшины, дыхание, прикосновения к передней стенке живота. Иногда боль резка и сильна настолько, что пострадавший теряет сознание, а его пульс становится нитевидным.'
# # doc = nlp(test_text)
# test_text = all_text
# #Находим корневые существительные
# def find_root_noun(text):
#     set_root = set()
#     doc = nlp(text)
#     for sent in doc.sents:
#         for token in sent:
#             if token.dep_ == 'ROOT' and token.pos_ == 'NOUN': #token.dep_ == 'ROOT' and token.pos_ == 'NOUN'
#                 # print(token.head.text, ' - ', token.dep_, ' - ', token.pos_, ' - ', token.text)
#                 set_root.add(token.text.lower())
#
#     return set_root
#
# #Находим корневыые прилагательные
# def find_root_adj(text):
#     set_root = set()
#     doc = nlp(text)
#     for sent in doc.sents:
#         for token in sent:
#             if token.dep_ == 'ROOT' and token.pos_ == 'ADJ': #token.dep_ == 'ROOT' and token.pos_ == 'NOUN'
#                 # print(token.head.text, ' - ', token.dep_, ' - ', token.pos_, ' - ', token.text)
#                 set_root.add(token.text.lower())
#
#     return set_root
#
# # #Находим связанные с корневем прилагательные
# # def find_noun_adj(text):
# #     set_root = set()
# #     doc = nlp(text)
# #     for token in doc:
# #         if token.dep_ == 'ROOT' and token.pos_ == 'NOUN': #token.dep_ == 'ROOT' and token.pos_ == 'NOUN'
# #             chunk = ''
# #             # print('token -', token)
# #             for w in token.children:
# #                 if w.dep_ == 'amod' or w.pos_ == 'ADJ':
# #                     chunk = chunk + w.text + ' '
# #             chunk = chunk + token.text
# #             set_root.add(chunk)
# #
# #     return set_root
#
# #Находим связанные с корневем прилагательные дубль
# def find_noun_adj(text):
#     set_root = set()
#     doc = nlp(text)
#     list_word_comb = []
#     for token in doc:
#         if token.dep_ == 'ROOT' or token.pos_ == 'NOUN': #token.dep_ == 'ROOT' and token.pos_ == 'NOUN'
#             # print('token -', token)
#             for w in token.children:
#                 if w.dep_ == 'amod' or w.pos_ == 'ADJ':
#                     chunk = ''
#                     chunk = chunk + w.text.lower() + ' ' + token.text.lower()
#                     list_word_comb.append(chunk)
#             # chunk = chunk + token.text
#             # set_root.add(chunk)
#
#     return list_word_comb
#
# def find_adj(text):
#     doc = nlp(text)
#     for token in doc:
#         if token.dep_ == 'ROOT' and token.pos_ == 'NOUN': #token.dep_ == 'ROOT' and token.pos_ == 'NOUN'
#             chunk = [w.text for w in token.children if w.dep_ == 'amod' and w.pos_ == 'ADJ']
#             if len(chunk) > 0:
#                 return chunk, token.text
#         elif token.dep_ == 'ROOT' and token.pos_ == 'ADJ':
#             chunk = [w.text for w in token.children if w.dep_ == 'amod' and w.pos_ == 'ADJ']
#             if len(chunk) > 0:
#                 return chunk, token.text
#
#         else:
#             continue
#
# #Создание словаря
# def make_dict(array):
#     dict_word = {}
#     for el in array.split('.'):
#         for symb in el.lower().split(' '):
#             if symb not in dict_word.keys():
#                 if len(symb) > 3:
#                     dict_word[symb] = [el + '.']
#             else:
#                 dict_word[symb].append(el + '.')
#     return dict_word
#
# def make_dict_sent(array, root):
#     dict_word = {}
#     for token in root:
#         for el in array.split('.'):
#             for symb in el.lower().split(' '):
#                 if token == symb:
#                     if token not in dict_word.keys():
#                         dict_word[token] = [el.lstrip() + '.']
#                     else:
#                         dict_word[token].append(el.lstrip() + '.')
#     return dict_word
#
# def take_dict(array):
#     tmp_dict = {}
#     for el in array:
#         tup_el = find_adj(el)
#         if tup_el:
#             list_adj, root = tup_el
#             if len(list_adj) > 1:
#                 for word in list_adj:
#                     if word.lower() + ' ' + root not in tmp_dict.keys():
#                         tmp_dict[word.lower() + ' ' + root] = [el]
#                     else:
#                         tmp_dict[word.lower() + ' ' + root].append(el)
#             elif len(list_adj) == 1:
#                 if list_adj[0].lower() + ' ' + root not in tmp_dict.keys():
#                     tmp_dict[list_adj[0].lower() + ' ' + root] = [el]
#                 else:
#                     tmp_dict[list_adj[0].lower() + ' ' + root].append(el)
#             else:
#                 continue
#
#     return tmp_dict
#
# #Формируем рекурсивно слвоарь словаре
# def make_recurs_dict(dict_item):
#     word_comb = {}
#     for key, value in dict_item.items():
#         if type(value) == dict:
#             make_recurs_dict(value)
#
#         elif type(value) == list:
#             if len(value) > 2:
#                 word_comb[key] = take_dict(value)
#             else:
#                 word_comb[key] = value
#         else:
#             continue
#
#     return word_comb
#
# def mix_noun_adj(text, list_adj):
#     dict_word = {}
#     for token in list_adj:
#         for el in text.split('.'):
#             for symb in el.lower().split(' '):
#                 if token == symb:
#                     if token not in dict_word.keys():
#                         dict_word[token] = [el.lstrip() + '.']
#                     else:
#                         dict_word[token].append(el.lstrip() + '.')
#     return dict_word
#
# #Находи корни существительные в предложении
# set_root_noun = find_root_noun(test_text)
# print(set_root_noun)
# print(len(set_root_noun))
#
# #Находи корни прилагательные в предложении
# set_root_adj = find_root_adj(test_text)
# # print(set_root_adj)
# # print(len(set_root_adj))
#
# list_noun_adj = find_noun_adj(test_text)
# print(len(list_noun_adj))
# set_noun_adj = set(list_noun_adj)
# print(len(set_noun_adj))
# for el in set_noun_adj:
#     print(el)
#
# # temp_mix_vord_comb = list(set_root_noun) + list(set_noun_adj)
# # for el in temp_mix_vord_comb:
# #     print('1 - ', el)
#
#
# # tmp_list = []
# # tmp_dict = {}
# # tmp_set = set()
#
#
# # for el in set_noun_adj:
# #     if len(el.split(" ")) > 1:
# #         if len(el.lower().split(" ")) > 2:
# #             tmp_list.extend(el.lower().split(" "))
# #         # com_set = itertools.combinations(el.lower().split(" "), 2)
# #         tmp_set = set(tmp_list)
# #         com_set = itertools.combinations(tmp_set, 2)
#         # print(el)
#         # print(tmp_set)
#         # print(tmp_list)
#         # print(list(com_set))
# # print(set_noun_adj)
# # print(len(set_noun_adj))
# # print(len(tmp_list))
# # print(len(tmp_set))
#
# #Создаем словарь существительных в предложении
# dict_noun = make_dict_sent(test_text, list(set_root_noun))
# # print(dict_noun)
# # print(len(dict_noun))
#
# #Создаем словарь прилагательных в предложении
# dict_adj = make_dict_sent(test_text, list(set_root_adj))
# # print(dict_adj)
# # print(len(dict_adj))
#
# # #Существительное + прилагательное
# noun_adj_dict = {}
# for key, value in dict(sorted(dict_noun.items(), key=lambda x: len(x[1]), reverse=False)).items():
#     if len(mix_noun_adj(" ".join(value), list(set_root_adj))) != 0:
#         noun_adj_dict[key] = mix_noun_adj(" ".join(value), list(set_root_adj))
#
# list_tupl_concepts = []
# for i, elem1 in enumerate(set(set_root_noun)):
#     for j, elem2 in enumerate(set(set_noun_adj)):
#         if elem1 in elem2.split():
#             list_tupl_concepts.append(((i+1)*10000+(j+1), elem2, (i+1)*100, elem1))
#         else:
#             list_tupl_concepts.append(((i+1)*100, elem1, 0, "Приборы и инструменты"))
#
# print(len(list_tupl_concepts))
# print(len(set(list_tupl_concepts)))
# print('2 - ', (set(list_tupl_concepts)))
#
#
# # set(list_tupl_concepts).sort(key = lambda x: x[1])
# for el in sorted(set(list_tupl_concepts), key=lambda x: x[0]):
#     print(el)
# #
# with open('data/table_two.csv', mode='w', encoding='utf-8', newline='') as file:
#     file_writer = csv.writer(file, delimiter=',', lineterminator='\n')
#     file_writer.writerow(['id', 'name', 'parant_id', 'parant_name'])
#     for el in sorted(set(list_tupl_concepts), key=lambda x: x[0]):
#         file_writer.writerow([el[0], el[1], el[2], el[3]])
# print_border('Загрузка данных из таблицы EXCEL завершена')
#
#
# # temp_data = []
# # for elem1 in set(set_root_noun):
# #     for elem2 in set(list_tupl_concepts):
# #         if elem1[3] in elem2['name'].lower() or ' '.join(reversed(elem1[3].split())) in elem2['name'].lower():
# #             temp_data.append((elem1[1], elem1[3], elem2['id'], elem2['name']))
#
#
#
# #
# # data_mix = []
# # for elem1 in set(list_tupl_concepts):
# #     for elem2 in dict_data:
# #         if elem1[3] in elem2['name'].lower() or ' '.join(reversed(elem1[3].split())) in elem2['name'].lower():
# #             data_mix.append((elem1[1], elem1[3], elem2['id'], elem2['name']))
# #
# #         for el in elem1[3].split():
# #             if el in elem2['name'].split():
# #                 data_mix.append((elem1[1], elem1[3], elem2['id'], elem2['name']))
# #
# # print(len(data_mix))
# # for el in data_mix:
# #     print(el)
# #
# #
# #
# #
# #
# # itog_dict = {}
# # for k, v in dict(sorted(noun_adj_dict.items(), key=lambda x: len(x[1]), reverse=False)).items():
# #     # print(k, ' - ', len(v), ' - ', v)
# #
# #     itog_dict[k] = make_recurs_dict(v)
#
# #*****************************************************************************************************
#
#
# from treelib import Node, Tree
#
# #
# # def rec_tree(array):
# #     tree = Tree()
# #     for key, value in array.items():
# #         tree.create_node(key, key)  # root node
# #         if isinstance(value, list):
# #             for el in value:
# #                 return tree.create_node(el, el, parent=key)
# #         else:
# #             new_tree = rec_tree(value)
# #             if isinstance(new_tree, Tree):
# #                 return tree.paste(key, new_tree)
# #             else:
# #                 continue
# #
# #
# # #
# # tree = Tree()
# # for key, value in itog_dict.items():
# #     print(key, ' - ', len(value), ' - ', value)
# #     tree.create_node(key, key)  # root node
# #     if isinstance(value, list):
# #         for el in value:
# #             tree.create_node(el, el, parent=key)
# #     else:
# #         new_tree = rec_tree(value)
# #         if isinstance(new_tree, Tree):
# #             tree.paste(key, new_tree)
# #         else:
# #             continue
# #
# #     tree.show()
#
#
# #
# # tree = Tree()
# # tree.create_node("Harry", "harry")  # root node
# # tree.create_node("Jane", "jane", parent="harry")
# # tree.create_node("Bill", "bill", parent="harry")
# # tree.create_node("Diane", "diane", parent="jane")
# # tree.create_node("Mary", "mary", parent="diane")
# # tree.create_node("Mark", "mark", parent="jane")
# # tree.show()
# #
# #
# # new_tree = Tree()
# # new_tree.create_node("n1", 1)  # root node
# # new_tree.create_node("n2", 2, parent=1)
# # new_tree.create_node("n3", 3, parent=1)
# # tree.paste('bill', new_tree)
# # tree.show()
#
# #####################################################
# #***************************************************
# #
# # for key, value in itog_dict.items():
# #     print(key, ' - ', len(value), ' - ', value)
# #     root = Node(key)
# #     if type(value) == dict:
# #         for k, v in value.items():
# #             k = Node(k, parent=root)
# #             if type(v) == dict and len(v) != 0:
# #                 for t, m in v.items():
# #                     t = Node(t, parent=k)
# #                     if type(m) == dict and len(m) != 0:
# #                         continue
# #                     elif type(m) == list:
# #                         for el in m:
# #                             el = Node(el, parent=t)
# #                     else:
# #                         continue
# #             elif type(v) == list:
# #                 for el in v:
# #                     el = Node(el, parent=k)
# #             else:
# #                 continue
# #     else:
# #         continue
# #
# #     for pre, fill, node in RenderTree(root):
# #         print("%s%s" % (pre, node.name))
# #*********************************************************************
#
# #
# # def iteritems_recursive(itog_dict):
# #   for k, v in itog_dict.items():
# #     if isinstance(v, dict):
# #       for k1, v1 in iteritems_recursive(v):
# #         yield (k,)+k1, v1
# #     else:
# #       yield (k,),v
# #
# #
# #
# # for p, v in iteritems_recursive(itog_dict):
# #     print(p, "->", v)
# #
#
#
#
# #
# # class Tree(object):
# #     "Generic tree node."
# #     def __init__(self, name='root', children=None):
# #         self.name = name
# #         self.children = []
# #         if children is not None:
# #             for child in children:
# #                 self.add_child(child)
# #     def __repr__(self):
# #         return self.name
# #     def add_child(self, node):
# #         assert isinstance(node, Tree)
# #         self.children.append(node)
# #
#
#
# # #
# # fieldnames = ['id', 'name', 'master_id', 'parent_id']
# # with open('datas/table.csv', mode='w', encoding='utf-8', newline='') as file:
# #     file_writer = csv.DictWriter(file, delimiter=',', fieldnames=fieldnames)
# #     file_writer.writeheader()
# #     for key, value in itog_dict.items():
# #         if isinstance(value, list):
# #             for i, el in enumerate(value):
# #                 file_writer.writerow([i, key, j, value])
# #
# #
# # with open('db/dataset_black/disease_symptoms_names2.csv', mode='w', encoding='utf-8', newline='') as file:
# #     file_writer = csv.writer(file, delimiter=',', lineterminator='\n')
# #     file_writer.writerow(['id_symptoms', 'name_symptoms'])
# #     for key, value in itog_dict.items():
# #         file_writer.writerow([key, value])
#
#
# # all_list = []
# # parent = []
# #
# # def inter_list(all_dict):
# #     all_list = []
# #     for key, value in all_dict.items():
# #         if isinstance(value, dict):
# #             all_list.append(key)
# #             all_list.extend(inter_list(value))
# #         else:
# #             all_list.append(key)
# #             all_list.extend(value)
# #
# #     return all_list
# #
# #
# # all_array = inter_list(itog_dict)
# # print(all_array)
# # print(len(all_array))
# #
# # set_array = set(all_array)
# # print(len(set_array))
#
# #
# # def iteritems_recursive(itog_dict):
# #   for k, v in itog_dict.items():
# #     if isinstance(v, dict):
# #       for k1, v1 in iteritems_recursive(v):
# #         yield (k,)+k1, v1
# #     else:
# #       yield (k,),v
# #
#
#
#
#
#
#
# # #Во-первых , найдите родителя по имени, используя anytrees find_by_attr
# # from anytree import Node, RenderTree, find_by_attr
# #
# # with open('input.txt', 'r') as f:
# #     lines = f.readlines()[1:]
# #     root = Node(lines[0].split(" ")[0])
# #
# #     for line in lines:
# #         line = line.split(" ")
# #         Node("".join(line[1:]).strip(), parent=find_by_attr(root, line[0]))
# #
# #     for pre, _, node in RenderTree(root):
# #         print("%s%s" % (pre, node.name))
#
# # #Во-вторых , просто кэшируйте их в диктанте, пока мы их создаем:
# # from anytree import Node, RenderTree, find_by_attr
# #
# # with open('input.txt', 'r') as f:
# #     lines = f.readlines()[1:]
# #     root = Node(lines[0].split(" ")[0])
# #     nodes = {}
# #     nodes[root.name] = root
# #
# #     for line in lines:
# #         line = line.split(" ")
# #         name = "".join(line[1:]).strip()
# #         nodes[name] = Node(name, parent=nodes[line[0]])
# #
# #     for pre, _, node in RenderTree(root):
# #         print("%s%s" % (pre, node.name))
#
#
#
#
#
#
#
#
#
# # root = Node("root", children=[
# # Node("sub0", children=[
# #     Node("sub0B", bar=109, foo=4),
# #     Node("sub0A", children=None),
# # ]),
# # Node("sub1", children=[
# #     Node("sub1A"),
# #     Node("sub1B", bar=8, children=[]),
# #     Node("sub1C", children=[
# #         Node("sub1Ca"),
# #     ]),
# # ]),
# # ])
#
#
#
# from anytree import NodeMixin, RenderTree
#
# class MyBaseClass(object):  # Just an example of a base class
#     foo = 4
#
# class MyClass(MyBaseClass, NodeMixin):  # Add Node feature
#     def __init__(self, name, length, width, parent=None, children=None):
#         super(MyClass, self).__init__()
#         self.name = name
#         self.length = length
#         self.width = width
#         self.parent = parent
#         if children:
#             self.children = children
#
#
#
#
#
# #
# # tree = Tree()
# # tree.create_node("Harry", "harry")  # root node
# # tree.create_node("Jane", "jane", parent="harry")
# # tree.create_node("Bill", "bill", parent="harry")
# # tree.create_node("Diane", "diane", parent="jane")
# # tree.create_node("Mary", "mary", parent="diane")
# # tree.create_node("Mark", "mark", parent="jane")
# #
# #
# #
# # new_tree = Tree()
# # new_tree.create_node("n1", 1)  # root node
# # new_tree.create_node("n2", 2, parent=1)
# # new_tree.create_node("n3", 3, parent=1)
# # tree.paste('bill', new_tree)
# # tree.show()
# #
# #
# #
# #
# # def creat_tree(dicts, parent):
# #     tree = Tree()
# #     for key, value in dicts.items():
# #         tree.create_node(key, parent)
# #         if type(value) == dict:
# #             tree.paste(key, creat_tree(value, key))
# #               # root node
# #         else:
# #             for token in value:
# #                 tree.create_node(token, parent=parent)
# #
# #     return tree
# #
#
#
# # new_tree = Tree()
# # new_tree.create_node("n1", 1)  # root node
# # new_tree.create_node("n2", 2, parent=1)
# # new_tree.create_node("n3", 3, parent=1)
# # tree.paste('bill', new_tree)
# # tree.show()
#
#
# # for key, value in itog_dict.items():
# #     # print(k, ' - ', len(v), ' - ', v)
# #     tree = Tree()
# #     tree.create_node(key.title(), key)  # root node
# #     for k, v in value.items():
# #         if type(v) == dict:
# #             tree = creat_tree(v, k)
# #         else:
# #             for token in v:
# #                 tree.create_node(token, parent=k)
# #     tree.paste(key, tree)
# #     tree.show()
#
# # from collections import defaultdict
# #
# # d = defaultdict(list)  # parent: List[children]
# # for k, v in itog_dict.items():
# #     d[v['parent']].append(k)
# # root = d[None][0]
# #
# # tree = Tree()
# # tree.create_node(root, root)
# #
# # agenda, seen = [root], set([root])
# # while agenda:
# #     nxt = agenda.pop()
# #     for child in d[nxt]:
# #         tree.create_node(child, child, parent=nxt)
# #         if child not in seen:
# #             agenda.append(child)
# #             seen.add(child)
#
#
#
# # from treelib import Node, Tree
# #
# # dict_ = itog_dict
# #
# # added = set()
# # tree = Tree()
# # while dict_:
# #     for key, value in dict_.items():
# #         if value['parent'] in added:
# #             tree.create_node(key, key, parent=value['parent'])
# #             added.add(key)
# #             dict_.pop(key)
# #             break
# #         elif value['parent'] is None:
# #             tree.create_node(key, key)
# #             added.add(key)
# #             dict_.pop(key)
# #             break
# #
# # tree.show()
#
#
# #
# # tree = Tree()
# # tree.create_node("Harry", "harry")  # root node
# # tree.create_node("Jane", "jane", parent="harry")
# # tree.create_node("Bill", "bill", parent="harry")
# # tree.create_node("Diane", "diane", parent="jane")
# # tree.create_node("Mary", "mary", parent="diane")
# # tree.create_node("Mark", "mark", parent="jane")
# # tree.show()
# #
# #
# # new_tree = Tree()
# # new_tree.create_node("n1", 1)  # root node
# # new_tree.create_node("n2", 2, parent=1)
# # new_tree.create_node("n3", 3, parent=1)
# # tree.paste('bill', new_tree)
# # tree.show()
#
#
#
# # for k, v in dict(sorted(noun_adj_dict.items(), key=lambda x: len(x[1]), reverse=False)).items():
# #     # print(k, ' - ', len(v), ' - ', v)
# #     for t, m in v.items():
# #         print(k, ' - ', len(v), ' - ', t, ' - ', len(m), ' - ', m)
# #         if len(m) == reduce(lambda a, b: a if (a > b) else b, m):
# #             pass
#
#
# # adj_noun_dict = {}
# # for k, v in dict(sorted(noun_adj_dict.items(), key=lambda x: len(x[1]), reverse=False)).items():
# #     # print(k, ' - ', len(v), ' - ', v)
# #     tree = Tree()
# #     tree.create_node(k.title(), k)  # root node
# #     for key, value in v.items():
# #         tree.create_node(k.title() + " " + key, key, parent=k)
# #         for token in value:
# #             tree.create_node(token, parent=key)
# #     tree.show()
#
#
# # # Прилагательное + Существительное
# # adj_noun_dict = {}
# # for key, value in dict(sorted(dict_adj.items(), key=lambda x: len(x[1]), reverse=False)).items():
# #     if len(mix_noun_adj(" ".join(value), list(set_root_noun))) != 0:
# #         adj_noun_dict[key] = mix_noun_adj(" ".join(value), list(set_root_noun))
# #
# #
# # for k, v in dict(sorted(adj_noun_dict.items(), key=lambda x: len(x[1]), reverse=False)).items():
# #     print(k, ' - ', len(v), ' - ', v)
# #
# #
# #
# # def make_tree(adj_noun_dict):
# #     for k, v in dict(sorted(adj_noun_dict.items(), key=lambda x: len(x[1]), reverse=False)).items():
# #         # print(k, ' - ', len(v), ' - ', v)
# #         tree = Tree()
# #         tree.create_node(k.title(), k)  # root node
# #         for key, value in v.items():
# #             tree.create_node(k.title() + " " + key, key, parent=k)
# #             for token in value:
# #                 tree.create_node(token, parent=key)
# #     return tree
# #
# # tree = make_tree(adj_noun_dict)
# # tree.show()
#
# #
# # for k, v in dict(sorted(adj_noun_dict.items(), key=lambda x: len(x[1]), reverse=False)).items():
# #     # print(k, ' - ', len(v), ' - ', v)
# #     tree = Tree()
# #     tree.create_node(k.title(), k)  # root node
# #     for key, value in v.items():
# #         tree.create_node(k.title() + " " + key, key, parent=k)
# #         for token in value:
# #             tree.create_node(token, parent=key)
# #     tree.show()
#
#
#
#
# #
# # from anytree import NodeMixin, RenderTree
# #
# #
# # class MyClass(NodeMixin):  # Add Node feature
# #     def __init__(self, name, parent=None):
# #         super(MyClass, self).__init__()
# #         self.name = name
# #         self.parent = parent
# #
# #
# #
# #
# # def print_anytree(startnode):
# #
# #     for pre, _, node in RenderTree(startnode):
# #         treestr = u"%s%s" % (pre, node.name)
# #         print(treestr.ljust(8))
# #
# # def rec_tree(dict_arr, MyClass):
# #     for k, v in value.items():
# #         if isinstance(v, list):
# #             for el in v:
# #                 return MyClass(el, parent=k)
# #         else:
# #             NodeMixin(rec_tree(v, MyClass), k)
# #
# #
# # if __name__ == '__main__':
# #     for key, value in itog_dict.items():
# #
# #         print(key, ' - ', len(value), ' - ', value)
# #         key = MyClass(key)
# #         if isinstance(value, list):
# #             for el in value:
# #                 el = MyClass(el, parent=key)
# #         else:
# #             NodeMixin(rec_tree(value, MyClass), key)
# #
# #     print_anytree(key)
# #
#
#
#
#
#
#
#
