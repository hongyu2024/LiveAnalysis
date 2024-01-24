import pandas as pd  # pip install pandas
import re
import jieba  # pip install jieba
import collections
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS  # pip install WordCloud
import matplotlib.pyplot as plt
from PIL import Image

# 读取数据
path = r"doc\2024-01-23-21-09-17.txt"
with open(path, encoding='utf-8') as f:
    data = f.read()
    # 文本预处理
pattern = re.compile(u'[\t|\n?*]')
data = re.sub(pattern, '', data)

# 精准模式对文本进行分词
# 去除常见的停用词和单个词
seg_list_exact = jieba.cut(data, cut_all=False)
# 自定义去除词库
remove_words = [u'爆', u'，', u'和', u'是', u'随着', u'对于', u'对', u'等', u'能', u'都', u'。', u' ', u'、', u'中', u'在',
                u'了', u'通常', u'如果', u'我们', u'主播']
# 去除自定义词
object_list = []
for word in seg_list_exact:
    if word not in remove_words:
        object_list.append(word)
# 去除单个词
for i in range(len(object_list) - 1, -1, -1):
    if len(object_list[i]) < 2:
        object_list.pop(i)
# 分词词频统计
word_counts = collections.Counter(object_list)

# 获取前100个高频词
word_counts_top100 = word_counts.most_common(10)
key_word = []
key_val = []
for key, val in word_counts_top100:
    key_word.append(key)
    key_val.append(val)

print(word_counts_top100)
print(key_word)
print(key_val)

img_mask = plt.imread('bg.png') * 255
my_wordcloud = WordCloud(
    background_color='white',  # 设置背景颜色
    mask=img_mask,  # 背景图片
    max_words=200,  # 设置最大显示的词数
    stopwords=STOPWORDS,  # 设置停用词
    # 设置字体格式，字体格式 .ttf文件需自己网上下载，最好将名字改为英文，中文名路径加载可能会出现问题。
    font_path='simhei.ttf',
    max_font_size=100,  # 设置字体最大值
    random_state=50,  # 设置随机生成状态，即多少种配色方案
    ##提高清晰度
    width=1000, height=600,
    min_font_size=20,
).generate_from_frequencies(word_counts)
plt.imshow(my_wordcloud)
plt.axis('off')
plt.show()
