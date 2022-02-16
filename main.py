import time

import matplotlib.pyplot as plt
from scrapy.cmdline import execute
import numpy as np
import csv
import os
import sys
from scrapy.crawler import CrawlerProcess
from statsmodels.genmod.families import family

from scrapy_bili.spiders.lyc import LycSpider

if __name__ == '__main__':
    # 启动爬虫
    process = CrawlerProcess()
    process.crawl(LycSpider)
    process.start()
    time.sleep(1)
    print("爬取完毕...")
    print("生成图像中...")
    # 读取数据
    with open('a.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        data = [row for row in reader]
    # 将数据转换为数组
    data = np.array(data)
    # 将上映日期列转化为年份
    data[:, 3] = [int(i[:4]) for i in data[:, 3]]
    # 播放量都转化为数字
    data[:, 4] = [float(i) for i in data[:, 4]]
    # 根据上映日期列进行排序
    data = data[data[:, 3].argsort()]
    # 转换为二维列表
    data = data.tolist()
    # 统计每年的播放量
    play_count = {}
    for i in data:
        if i[3] in play_count:
            play_count[i[3]] += float(i[4])
        else:
            play_count[i[3]] = float(i[4])
    # 绘制播放量柱状图
    # 截图字典后面20个数据
    play_count = dict(list(play_count.items())[-20:])
    plt.figure(figsize=(14, 8))
    # print(play_count.keys(), play_count.values())
    # 打印字典
    # for item in play_count.items():
    #     print(item)
    # 设置大标题
    
    
    # 绘制柱状图
    font_family = ["PingFang SC", "Hiragino Sans GB", "Heiti SC", "Microsoft YaHei", "WenQuanYi Micro Hei"]
    font = {'family': font_family, 'weight': 'bold', 'size': 12}
    plt.rc('font', **font)
    # 显示数据大小
    plt.bar(play_count.keys(), play_count.values(), width=0.5, 
        color='#777bce', edgecolor='#0b2d64', linewidth=2, alpha=0.8)
    plt.title('bilibili Top100 电影播放量统计')
    # 同一子图上绘制折线图
    # ax = plt.subplot(212)
    # 绘制折线图
    plt.plot(play_count.keys(), play_count.values(), color='#f52443', linewidth=2,
        linestyle='-', marker='o', markerfacecolor='#f52443', markersize=5)
    for i, j in zip(play_count.keys(), play_count.values()):
        plt.text(i, j, "%.2f"%j, ha='center', va='bottom', fontsize=10)
    # 设置x轴的刻度
    # plt.xticks(play_count.keys(), rotation=45)
    plt.xlabel('上映年份(年)')
    plt.ylabel('播放量(万)')
    # # 绘制散点图
    # ax = plt.subplot(212)
    # font = {'family': 'SimHei', 'weight': 'bold', 'size': 15}
    # plt.rc('font', **font)
    # plt.scatter(play_count.keys(), play_count.values(), s=50,
    #     color='#123456', marker='o', edgecolors='#234567')
    # plt.xlabel('年份')
    # plt.ylabel('播放量')
    plt.show()
    # print(data)
    # 创建一个matplotlib图形
    # fig = plt.figure(figsize=(12, 10), dpi=80)
    # # 创建一个散点图，设置颜色为红色
    # plt.scatter(data[:, 3], data[:, 4], c='g', marker='o')
    # # 设置x轴标签
    # plt.xlabel('上映年份(年)')
    # # 设置y轴标签
    # plt.ylabel('播放量(万)')
    # # 设置标题
    # plt.title('各个年度电影播放量')
    # plt.show()