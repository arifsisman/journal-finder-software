from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def get_cosine_sim(*strs):
    vectors = [t for t in get_vectors(*strs)]
    return cosine_similarity(vectors)


def get_vectors(*strs):
    text = [t for t in strs]
    vectorizer = CountVectorizer(text)
    vectorizer.fit(text)
    return vectorizer.transform(text).toarray()


# Cosine helper needs data and print option
def cosine_helper(abstract, datas):
    arr_len = len(datas)
    result = [[0] * 3 for element in range(arr_len)]

    for i in range(0, arr_len):
        sim = cosine_similarity(get_vectors(abstract, datas[i][1]))
        result.append((datas[i][0], datas[i][1], sim[1][0]))
    return result