import json
import re

class Processing_json():
    def __init__(self, file_path):
        # file_path = './result/naver_news/news_한동훈_naver_20220620_20220623__202206.json'
        json_file = open(file_path, encoding = 'utf-8')

        
        self.j_dic = json.load(json_file)
        self.result_dic = dict()


    #이모티콘 제거
    def remove_emoji(self, comment):
        emoji_pattern = re.compile("["
                                u"\U0001F600-\U0001F64F"
                                u"\U0001F300-\U0001F5FF"
                                u"\U0001F680-\U0001F6FF"
                                u"\U0001F1E0-\U0001F1FF"
                                "]+", flags=re.UNICODE)
        return emoji_pattern.sub(r'', comment)


    def dateNList(self):
        for date in self.j_dic.keys():
            temp = []
            for url in self.j_dic[date].keys():
                for comment in self.j_dic[date][url]["comments"]:
                    self.remove_emoji(comment)
                    temp.append(comment)
            self.result_dic[date] = temp
            temp = []
        return self.result_dic



