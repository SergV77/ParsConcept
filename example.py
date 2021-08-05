


def text_to_graph(text):
    import networkx as nx
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.neighbors import kneighbors_graph

    # use tfidf to transform texts into feature vectors
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(text)

    # build the graph which is full-connected
    N = vectors.shape[0]
    mat = kneighbors_graph(vectors, N, metric='cosine', mode='distance', include_self=True)
    mat.data = 1 - mat.data  # to similarity

    g = nx.from_scipy_sparse_matrix(mat, create_using=nx.Graph())

    return g

def load(self):
    categories = ['comp.sys.ibm.pc.hardware', 'comp.sys.mac.hardware']
    newsgroups_train = fetch_20newsgroups(
        subset='train', remove=('headers', 'footers', 'quotes'), categories=categories)
    newsgroups_test = fetch_20newsgroups(
        subset='test', remove=('headers', 'footers', 'quotes'), categories=categories)
    vectorizer = TfidfVectorizer(stop_words='english', min_df=0.001, max_df=0.20)
    vectors = vectorizer.fit_transform(newsgroups_train.data)
    vectors_test = vectorizer.transform(newsgroups_test.data)
    x1 = vectors
    y1 = newsgroups_train.target
    x2 = vectors_test
    y2 = newsgroups_test.target
    x = np.array(np.r_[x1.todense(), x2.todense()])
    y = np.r_[y1, y2]
    return x, y



