import json
class Processing_json():
    def __init__(self, file_path):
        # file_path = './result/naver_news/news_한동훈_naver_20220620_20220623__202206.json'
        json_file = open(file_path, encoding = 'utf-8')
        
        self.j_dic = json.load(json_file)
        self.result_dic = dict()


    def dateNList(self):
        for date in self.j_dic.keys():
            temp = []
            for url in self.j_dic[date].keys():
                for comment in self.j_dic[date][url]["comments"]:
                    temp.append(comment)
            self.result_dic[date] = temp
            temp = []
        return self.result_dic

