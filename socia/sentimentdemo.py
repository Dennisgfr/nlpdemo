# ML+ 情感分析

from nltk.classify import NaiveBayesClassifier

# 随手造点训练集
s1 = 'this is a good book'
s2 = 'this is a awesome book'
s3 = 'this is a bad book'
s4 = 'this is a terrible book'


def preprocess(s):
    print(s.lower().split())
    # Func: 句子处理
    # 这里简单的用了split()， 把句子中每个单词分开
    # 显然 还有更多的processing method可以用
    return {word: True for word in s.lower().split()}
    # return长这样
    # {}
    # 其中，前一个叫 fname，对应每个出现的文本单词
    # 后一个叫fval， 指的是每个文本单词中对应的值
    # 这里我们用最简单的True，来表示，这个词【出现在当前句子中】的意义


# print(preprocess(s1))
# print(preprocess(s2))
# print(preprocess(s3))
# print(preprocess(s4))

# 把训练集做成标准形式
training_data = [
    [preprocess(s1), 'pos'],
    [preprocess(s2), 'pos'],
    [preprocess(s3), 'neg'],
    [preprocess(s4), 'neg'],
]

# 喂给model吃
model = NaiveBayesClassifier.train(training_data)

# 输出结果
print(model.classify(preprocess('this terrible  good book')))
