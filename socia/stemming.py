# 词干提取
from nltk.stem.porter import PorterStemmer

porter_stemmer = PorterStemmer()
print(porter_stemmer.stem('maximum'))
print(porter_stemmer.stem('presumably'))
print(porter_stemmer.stem('multiply'))
print(porter_stemmer.stem('provision'))
