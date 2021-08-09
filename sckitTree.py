from settings import *
from function import *

nlp = spacy.load("ru_core_news_lg")
pd.set_option('display.max_columns', None)
# nlp = spacy.load("ru_core_news_lg")
stop_words = nltk.corpus.stopwords.words('russian')

file_name="data/НСИ - закупки.xlsx"

rb = xlrd.open_workbook(file_name)
sheet = rb.sheet_by_index(1)

#Получаем список значений из всех записей
vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]

text = []
for el in vals[1:]:
    text.append(el[1].replace('\n', ''))

#Очистка и токенизация текста
processed_data = []
processed_data_all = []
for doc in vals[1:]:
    tokens = preprocess_text(doc, stop_words)
    processed_data.append(tokens)
    processed_data_all += tokens

temp_res = [' '.join(el) for el in processed_data]

#Векторизация и создания датасета
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(temp_res)
features = vectorizer.get_feature_names()

dataSet = pd.DataFrame(data=X.todense(), columns=vectorizer.get_feature_names())
dataSet["Class"] = [el for el in range(1, (len(dataSet.index)) + 1)]
# print(dataSet)
# print(dataSet.shape)

X = dataSet.drop('Class', axis=1)
y = dataSet['Class']

#Создание обучающей и тренировочной выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

#Классификация
#Обучение модели
classifier = DecisionTreeClassifier()
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

#Оценка алгоритма
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))


r = export_text(classifier, feature_names=features)
# print(r)

#Дерево решений для регрессии
regressor = DecisionTreeRegressor()
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)

df=pd.DataFrame({'Actual':y_test, 'Predicted':y_pred})
print(df)

print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))


r = export_text(regressor, feature_names=features)
print(r)

tree.plot_tree(regressor)
dot_data = tree.export_graphviz(regressor, out_file=None)
graph = graphviz.Source(dot_data)
graph.render("medical")

dot_data = tree.export_graphviz(regressor, out_file=None,
feature_names=features,
class_names=y,
filled=True, rounded=True,
special_characters=True)
graph = graphviz.Source(dot_data)



tfidf_vectorizer = TfidfVectorizer(max_df=1.0,
                                   max_features=2500,
                                   min_df=0.0,
                                   use_idf=True,
                                   ngram_range=(1, 3))

tfidf_matrix = tfidf_vectorizer.fit_transform(temp_res)


features = tfidf_vectorizer.get_feature_names()
indices = zip(*tfidf_matrix.nonzero())
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










#
# plt.figure(figsize=(10,6))
# plt.scatter(X, y, s=6, c='black')
# plt.xlabel()
# plt.ylabel()
# graph.plot_model()
# plt.show()
#
# def plot_mesh(model, y, X, title):
#
#     n_classes = 3
#     plot_colors = "ryb"
#     plot_step = 0.02
#
#     x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
#     y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
#     xx, yy = np.meshgrid(np.arange(x_min, x_max, plot_step),
#                          np.arange(y_min, y_max, plot_step))
#     plt.tight_layout(h_pad=0.5, w_pad=0.5, pad=2.5)
#
#     Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
#     Z = Z.reshape(xx.shape)
#     cs = plt.contourf(xx, yy, Z, cmap=plt.cm.RdYlBu)
#
#     plt.xlabel('features 0'); plt.ylabel('features 1')
#
#     # Plot the training points
#     for i, color in zip(range(n_classes), plot_colors):
#         idx = np.where(y == i)
#         plt.scatter(X[idx, 0], X[idx, 1], c=color,
#                     cmap=plt.cm.RdYlBu, edgecolor='black', s=15)
#     plt.title(title)
#
# plt.figure(figsize=(8,6))
#
# plot_mesh(regressor, y, X, title="depth 6")


# import nltk
# import pandas as pd
#
# from sklearn.feature_extraction.text import TfidfVectorizer
#
# nltk.download('punkt')
#
# STEMMER = nltk.stem.porter.PorterStemmer()
#
#
# def stem_tokens(tokens, stemmer=STEMMER):
#     return [stemmer.stem(item) for item in tokens]
#
#
# def tokenizer(text):
#     tokens = nltk.word_tokenize(text)
#     return stem_tokens(tokens)
#
#
# tfidf = TfidfVectorizer(tokenizer=tokenizer, stop_words='english')
#
# # assuming our text elements exist in a pandas dataframe `df` with
# # a column / feature name of `document`
# tfs = tfidf.fit_transform(df.document.values)
#
# # you can calculate cosine similarity easily given this
# cossim = tfs @ tfs.T

#
# from sklearn.feature_extraction.text import TfidfVectorizer
# import pandas as pd
#
#
# corpus = [
#     'hi, my name is Bob.',
#     'hi, my name is Sara.'
# ]
#
# vectorizer = TfidfVectorizer(max_features=2)
# X = vectorizer.fit_transform(corpus).todense()
#
#
# df = pd.DataFrame(X, columns=vectorizer.get_feature_names())
# vectorizer = TfidfVectorizer(max_features=10)
# X = vectorizer.fit_transform(corpus).todense()
# df = pd.DataFrame(X, columns=vectorizer.get_feature_names())
# print(df)


#
# def _recurse_tree(parent, depth, source):
#     last_line = source.readline().rstrip()
#     while last_line:
#         tabs = last_line.count('\t')
#         if tabs < depth:
#             break
#         node = last_line.strip()
#         if tabs >= depth:
#             if parent is not None:
#                 print "%s: %s" %(parent, node)
#             last_line = _recurse_tree(node, tabs+1, source)
#     return last_line
#
# inFile = open("test.txt")
# _recurse_tree(None, 0, inFile)

