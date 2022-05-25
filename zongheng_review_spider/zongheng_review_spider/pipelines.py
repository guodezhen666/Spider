# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
# import pandas as pd

class ZonghengReviewSpiderPipeline:
    def process_item(self, item, spider):
        bkname = item['bkname']
        print(item['user_name'],item['review_content'],item['origin_content'],
                             item['time'],item["chapter"],item['up'],item['comment'])
        with open(f'{bkname}.txt','a',encoding='utf-8') as f:
            f.writelines(str(item['user_name'])+','+str(item['review_content']) + ',' +
                         str(item['origin_content']) +',' + str(item['time']) + ',' +str(item["chapter"])
                             + ',' + str(item['up']) + ',' +str(item['comment'])+'\n')
        return item

'''
class Csdn02Pipeline(object):
    def __init__(self):
        # 生成title.txt用于存储除内容外所有内容,分行存储
        self.cfile=open('F://demo/title.txt','a',encoding='utf8')
    def process_item(self, item, spider):
        curl=item['curl']
        title = item['title']
        updatetime = item['updatetime']
        readcount = item['readcount']
        author = item['author']
        ranking = item['ranking']
        context = item['context']
        self.cfile.write(f'标题:{title}\t发表时间:{updatetime}\t阅读数:{readcount}\t作者:{author}\t博客排名:{ranking}\t链接地址:{curl}\n')
        # 以writelines将列表形式的内容写入.html文件
        with open(f'F://demo/{title}.html', 'a', encoding='utf-8') as wl:
            wl.writelines(context)
        return item
    def file_close(self):
        # 关闭文件
        self.cfile.close()
        
'''