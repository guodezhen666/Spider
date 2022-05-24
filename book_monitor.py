# -*- coding: utf-8 -*-
"""
Created on Sat May 14 19:58:35 2022

@author: guodezhen
"""

import os
import pandas as pd
import requests
from lxml import etree
import time



def parse_information(url):
    book_info_list = []
    r = requests.get(url)
    html = etree.HTML(r.text)
    book_name = "".join(html.xpath('//div[contains(@class,"book-name")]/text()')).strip()
    book_info_list.append(book_name)
    book_img = "".join(html.xpath('//div[contains(@class,"book-img fl")]/img/@src'))
    book_info_list.append(book_img)
    
    book_sign = len(html.xpath('//div[contains(@class,"book-name")]/em[contains(@class,"sign")]'))
    book_info_list.append(book_sign)
    book_vip = len(html.xpath('//div[contains(@class,"book-name")]/em[contains(@class,"vip")]'))
    book_info_list.append(book_vip)
    book_label_1 = html.xpath('//div[contains(@class,"book-label")]/a/text()')
    book_info_list.append(book_label_1)
    book_label_2 = html.xpath('//div[contains(@class,"book-label")]/span/a/text()')
    book_info_list.append(book_label_2)
    
    book_num_words = "".join(html.xpath('//div[contains(@class,"nums")]/span[1]/i/text()'))
    book_info_list.append(book_num_words)
    book_recommand = "".join(html.xpath('//div[contains(@class,"nums")]/span[2]/i/text()'))
    book_info_list.append(book_recommand)
    book_click = "".join(html.xpath('//div[contains(@class,"nums")]/span[3]/i/text()'))
    book_info_list.append(book_click)
    book_week_recommand = "".join(html.xpath('//div[contains(@class,"nums")]/span[4]/i/text()'))
    book_info_list.append(book_week_recommand)
    book_abstract = "".join(html.xpath('//div[contains(@class,"book-dec Jbook-dec hide")]/p/text()'))
    book_info_list.append(book_abstract)
    book_author_link = "".join(html.xpath('//div[contains(@class,"au-head")]/a/@href'))
    book_info_list.append(book_author_link)
    book_author_name = "".join(html.xpath('//div[contains(@class,"au-head")]/a/img/@alt'))
    book_info_list.append(book_author_name)
    book_author_sign = "".join(html.xpath('//div[contains(@class,"au-head")]/em/text()'))
    book_info_list.append(book_author_sign)
    
    # 作品数
    book_author_works = "".join(html.xpath('//div[contains(@class,"au-words")]/span[1]/i/text()'))
    book_info_list.append(book_author_works)
    #累计字数
    book_author_words = "".join(html.xpath('//div[contains(@class,"au-words")]/span[2]/i/text()'))
    book_info_list.append(book_author_words)
    # 本月更新次数
    book_author_update_days = "".join(html.xpath('//div[contains(@class,"au-words")]/span[3]/i/text()'))
    book_info_list.append(book_author_update_days)
    
    # new chapter
    book_update_title = "".join(html.xpath('//div[contains(@class,"tit")]/a/text()'))
    book_info_list.append(book_update_title)
    book_update_chapter_url = "".join(html.xpath('//div[contains(@class,"tit")]/a/@href'))
    book_info_list.append(book_update_chapter_url)
    book_update_chapter_abstract = "".join(html.xpath('//div[contains(@class,"con")]/text()'))
    book_info_list.append(book_update_chapter_abstract)
    try:
        book_update_chapter_time = html.xpath('//div[contains(@class,"time")]/text()')[0].strip()
        book_update_chapter_day = "".join(html.xpath('//div[contains(@class,"time")]/text()')[1]).strip()
    except:
        book_update_chapter_time = ''
        book_update_chapter_day = ''
        
    book_info_list.append(book_update_chapter_day)
    book_info_list.append(book_update_chapter_time)
    cata_log_url = "".join(html.xpath('//div[contains(@class,"fr link-group")]/a[1]/@href'))
    book_info_list.append(cata_log_url)
    
    book_info_list.append(time.localtime().tm_hour)
    book_info_list.append(time.localtime().tm_min)
    return(book_info_list)


os.chdir("/ZonghengNewbook/book_update_one_month/")
file_list = os.listdir()
i = 1
for file in file_list:
    data = pd.read_excel(file)
    url_list = data["book_url"].to_list()
    book_info_file = []
    for url in url_list:
        book_info_file.append(parse_information(url))
        time.sleep(0.2)
        print("book {} done.".format(i))
        i += 1
    col = ["book_name","book_img","book_sign","book_vip","book_label_1","book_label_2","book_num_words",
           "book_recommand","book_click","book_week_recommand","book_abstract","book_author_link","book_author_name",
           "book_author_sign","book_author_works","book_author_words","book_author_update_days","book_update_title",
           "book_update_chapter_url","book_update_chapter_abstract","book_update_chapter_time","book_update_chapter_day",
           "cata_log_url","hour","minutes"]
    df = pd.DataFrame(book_info_file,columns = col)
    os.chdir("/ZonghengNewbook/book_update_info/")
    df.to_excel(file[:-5] + "_" + str(time.localtime().tm_mon)+"_"+str(time.localtime().tm_mday)+".xlsx")
    os.chdir("/ZonghengNewbook/book_update_one_month/")


