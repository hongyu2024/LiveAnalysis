import pandas as pd  # pip install pandas
import re
import jieba  # pip install jieba
import collections
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS  # pip install WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def do_analysis(txt_file,live_id):
    # 读取数据
    path = r"doc\2024-01-25-14-46-42.txt"
    path = txt_file
    with open(path, encoding='utf-8') as f:
        data = f.read()
        # 文本预处理
    pattern = re.compile(u'[\t|\n?*]')
    data = re.sub(pattern, '', data)

    # 精准模式对文本进行分词
    # 去除常见的停用词和单个词
    seg_list_exact = jieba.cut(data, cut_all=False)
    # 自定义去除词库
    remove_words = [u'关注', u'，', u'送出',  u'。', u' ', u'、', u'主播', u'直播', u'Ta', '点点', '赞赞', '直播间', '用户']
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
    word_counts_top100 = word_counts.most_common(15)
    key_word = []
    key_val = []
    for key, val in word_counts_top100:
        key_word.append(key)
        key_val.append(val)

    # print(word_counts_top100)
    #print(key_word)
    #print(key_val)
    with open('key_word.txt', 'w') as file:
        for item in key_word:
            file.write(str(item) + '\n')
        file.close()
    with open('key_val.txt', 'w') as file:
        for item in key_val:
            file.write(str(item) + '\n')
        file.close()

    #img_mask = plt.imread('live.png') * 255
    img_mask = np.array(Image.open("live.png"))  #将图片转为数组。
    my_wordcloud = WordCloud(
        background_color='white',  # 设置背景颜色
        mask=img_mask,  # 背景图片
        max_words=200,  # 设置最大显示的词数
        stopwords=STOPWORDS,  # 设置停用词
        # 设置字体格式，字体格式 .ttf文件需自己网上下载，最好将名字改为英文，中文名路径加载可能会出现问题。
        font_path='simhei.ttf',
        max_font_size=50,  # 设置字体最大值
        random_state=50,  # 设置随机生成状态，即多少种配色方案
        ##提高清晰度
        width=1000, height=600,
        min_font_size=5,
    ).generate_from_frequencies(word_counts)
    plt.imshow(my_wordcloud)
    plt.axis('off')
    #plt.show()
    plt.savefig('img\\'+live_id+'.png')


#do_analysis('doc\\2024-01-25-14-46-42.txt')
