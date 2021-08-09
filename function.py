from settings import *

def preprocess_text(document, stop_words):
    stemmer = WordNetLemmatizer()
    # Удаление специальных символов
    document = re.sub(r'\W', ' ', str(document))
    # Удаление всех одиночных символов
    document = re.sub(r'\s+[a-zA-Z]\s+', ' ', document)
    # Удаление символов в начале слова
    document = re.sub(r'\^[a-zA-Z]\s+', ' ', document)
    # Замена нескольких пробелов одинарным пробелом
    document = re.sub(r'\s+', ' ', document, flags=re.I)
    # Удаление бинарного символа 'b'
    document = re.sub(r'^b\s+', '', document)
    # приобразование в нижний регистр
    document = document.lower()

    # Лематизация
    tokens = document.split()
    tokens = [stemmer.lemmatize(word) for word in tokens]
    tokens = [word for word in tokens if word not in stop_words]
    tokens = [word for word in tokens if len(word) > 3]

    return tokens

def syntax_parsing(text, nlp):
    comb_token = []
    for sent in text:
        doc = nlp(sent)
        temp_list = []
        for token in doc:
            chunk = ''
            if token.pos_ == 'NOUN':
                for w in token.children:
                    if w.pos_ == 'ADP' or w.pos_ == 'ADJ':
                        chunk = chunk + w.text + ' '
                chunk = chunk + token.text

            if chunk != '':
                temp_list.append(chunk)

        comb_token.append(temp_list)

    return comb_token

# w.pos_ == 'ADJ' or w.pos_ == 'DET' or w.pos_ == 'ADP'


def counterConcept(concepts, lib):
    couent_concepts = {}

    for k, v in lib.items():
        count = 0
        for el2 in concepts:
            if v == int(el2[0]):
                count += 1

        couent_concepts[k] = count
        count = 0

    return couent_concepts


def print_border(info):
    print(' ' * 250)
    print('*' * 250)
    print('-' * ((250 - len(info))//2) + info + '-' * ((250 - len(info))//2 + 1))
    print('*' * 250)
    print(' ' * 250)



