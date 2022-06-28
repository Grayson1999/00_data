from utils.processing_json import Processing_json
from utils.predict import Predict 



if __name__ == '__main__':
    processing = Processing_json('sample_data/news_나로호_naver_20220618_20220628__202206.json')
    processed_dic = processing.dateNList()

    def dic_to_result(processed_dic):   
        predict = Predict()

        result_dic = {}
        for key in processed_dic.keys():
            missing_value = False
            positive = 0
            negative = 0
            if len(processed_dic[key]) == 0:
                missing_value = True
            for comment in processed_dic[key]:
                if predict.predict(comment):
                    positive +=1
                else:
                    negative +=1
            if missing_value:
                result_dic[key] = -1
            else:
                result_dic[key] = positive/(positive+negative)*100
            positive = 0
            negative = 0
        return result_dic   #ex) {'20220623':70, '20220624':-1(결측값)}
    
    result = dic_to_result(processed_dic)
    print(result)