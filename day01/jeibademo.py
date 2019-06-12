import jieba

seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
print("Full Mode:" + "/".join(seg_list))  # cut_all = True 全模式

seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
print("Default Mode:" + "/".join(seg_list))  # cut_all = False 精确模式

neg_list = jieba.cut("他来到了杭州网易杭研大厦")  # 默认是精确模式
print("新词识别:" + ".".join(neg_list))

seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")
# 搜索引擎模式
print("搜索引擎模式" + ".".join(seg_list))
