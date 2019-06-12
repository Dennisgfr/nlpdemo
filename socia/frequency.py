# 用出现频率表示文本特征

# Frequency频率统计

import nltk
from nltk import FreqDist

# 做个词库先
corpus = 'this is my sentence this is my life this is the day'

# 进行Tokenize processing预处理（stopwords， lemma， stemming， etc）

tokens = nltk.word_tokenize(corpus)
print(tokens)

# 用FreDist 统计一下文字出现的频率
fdist = FreqDist(tokens)

# 它就类似与一个dict
# 带上某个单词，可以看到他在整个文章中出现的次数
print(fdist)

standard_freq_vector = fdist.most_common(50)
size = len(standard_freq_vector)
print(standard_freq_vector)


def position_lookup(v):
    res = {}
    counter = 0
    for word in v:  # word 是一个元组（'this', 3） 单词，单词出现频次
        print(word)
        res[word[0]] = counter
        counter += 1
    return res


standard_position_dict = position_lookup(standard_freq_vector)
print(standard_position_dict)  # 得到一个位置对应表 （单词， 单词出现的位置）

# 测试
sentence = 'this is cool'

# 新建一个跟我们的标准vector 同样大小的向量
print(size)
freq_vector = [0] * size

# 简单的preprocessing
token = nltk.word_tokenize(sentence)
for word in token:
    try:
        # 如果在我们的词库里出现过那么就在标准位置上+1
        freq_vector[standard_position_dict[word]] += 1
    except KeyError:
        # 如果是新词就pass掉
        continue

print(token)
print(freq_vector)
