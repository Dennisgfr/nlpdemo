# 词形归一
import nltk
from nltk.stem import WordNetLemmatizer

wordnet_lemmatizer = WordNetLemmatizer()
print(wordnet_lemmatizer.lemmatize('dogs'))
print(wordnet_lemmatizer.lemmatize('churches'))
print(wordnet_lemmatizer.lemmatize('aardwolves'))
print(wordnet_lemmatizer.lemmatize('abaci'))
print(wordnet_lemmatizer.lemmatize('hardrock'))

# 词性标记 POS Tag
print(wordnet_lemmatizer.lemmatize('are'))
print(wordnet_lemmatizer.lemmatize('is'))

# 手动标注 标记为动词
print(wordnet_lemmatizer.lemmatize('are', pos='v'))
print(wordnet_lemmatizer.lemmatize('is', pos='v'))

text = nltk.word_tokenize('what does the for say')  # 分词 返回列表 ['what', 'does', 'the', 'for', 'say']
print(text)
print(nltk.pos_tag(text))  # 分词 并放回词性 [('what', 'WDT'), ('does', 'VBZ'), ('the', 'DT'), ('for', 'IN'), ('say', 'NN')]
