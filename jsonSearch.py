import json
class jsonSearch:
    i = 0
    search_dic = dict()
    search_list = []
    file_path = 'search.json'

    def __init__(self, search):
        self.search = search
        self.search_save(self.search)
    
    def search_save(self, search):
        self.search_list.append(search)

    def dic_save(self):
        for j in range(len(self.search_list)):
            self.search_dic[j] = self.search_list[j]
        print(self.search_dic)
        with open(self.file_path, 'a', encoding='utf-8') as f:
            f.write(json.dumps(self.search_dic, ensure_ascii=False, indent='\t'))

abc = jsonSearch("로꼬")
abc.dic_save()
