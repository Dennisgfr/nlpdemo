##社交网络语言tokenize
# 正则表达式过滤法

import re

emoticons_str = r"""
    (?:
        [:=;]             # 眼睛
        [oO\-]?           # 鼻子
        [D\)\]\{\]/\\OpP] # 嘴
    )"""
regex_str = [
    emoticons_str,
    r'<[^>]+>',  # HTML Tags
    r'(?:@[\w_]+)',  # @某人
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)",  # 话题标签
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+'  # urls
    r'(?:(?:\d+,?)+(?:\.?\d+)?)',  # 数字
    r"(?:[a-z][a-z'\-_]+[a-z])",  # 含有 - 和 ‘ 的单词
    r'(?:[\w_]+)',  # 其他
    r'(?:\S)'  # 其他
]
tokens_re = re.compile(r'(' + '|'.join(regex_str) + ')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^' + emoticons_str + '$', re.VERBOSE | re.IGNORECASE)


# RAW_TEXT 源文本 满足token_re 的字符都找出来
def tokenize(s):
    return tokens_re.findall(s)


def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens


tweet = 'RT @angelababy: love you baby! :D http://ah.love #168cm'
print(preprocess(tweet))
