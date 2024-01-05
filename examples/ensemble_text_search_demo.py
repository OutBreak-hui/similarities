# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import sys

sys.path.append('..')

from similarities import (
    BertSimilarity,
    TfidfSimilarity,
    EnsembleSimilarity,
)

if __name__ == '__main__':
    text1 = [
        '如何更换花呗绑定银行卡',
        '花呗更改绑定银行卡'
    ]
    text2 = [
        '花呗更改绑定银行卡',
        '我什么时候开通了花呗',
    ]
    corpus = [
        '花呗更改绑定银行卡',
        '我什么时候开通了花呗',
        '俄罗斯警告乌克兰反对欧盟协议',
        '暴风雨掩埋了东北部；新泽西16英寸的降雪',
        '中央情报局局长访问以色列叙利亚会谈',
        '人在巴基斯坦基地的炸弹袭击中丧生',
    ]

    queries = [
        '我的花呗开通了？',
        '乌克兰被俄罗斯警告',
        '更改绑定银行卡',
    ]
    print('text1: ', text1)
    print('text2: ', text2)
    print('query: ', queries)
    m1 = BertSimilarity()
    m2 = TfidfSimilarity()
    m = EnsembleSimilarity(similarities=[m1, m2], weights=[0.5, 0.5])
    print(m)
    sim_scores = m.similarity(text1, text2)
    print('sim scores: ', sim_scores)
    for (idx, i), j in zip(enumerate(text1), text2):
        s = sim_scores[idx] if isinstance(sim_scores, list) else sim_scores[idx][idx]
        print(f"{i} vs {j}, score: {s:.4f}")
    m.add_corpus(corpus)
    res = m.most_similar(queries, topn=3)
    print('sim search: ', res)
    for q_id, c in res.items():
        print('query:', queries[q_id])
        print("search top 3:")
        for corpus_id, s in c.items():
            print(f'\t{m.corpus[corpus_id]}: {s:.4f}')
    print('-' * 50 + '\n')
