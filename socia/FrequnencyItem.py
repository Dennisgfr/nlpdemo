# TF Term Frequency,衡量一个term在文档出现有多频繁
# TF(t) = (t出现在文档中的次数)/(文档中的term总数)
# IDF inversedocumentfrequency 衡量一个term 有多重要
# IDF(t) = log_e(文档总数/ 含有t的文档总数)
# TF_IDF = TF * IDF
import nltk
from nltk.text import TextCollection

# TextCollection 会自动帮你断句，做统计， 做计算
corpus = TextCollection({
    'this is sentence one',
    'this is sentence two',
    'this is sentence three'
})
# 直接就能算出tfidf
# {term： 一句话中的某个term， text：这句话}
print(corpus.tf_idf('this', 'this is sentence four'))

new_sentence = 'this is sentence five'
token = nltk.word_tokenize(new_sentence)
print(token)
for word in token:
    print(corpus.tf_idf(word, new_sentence))
