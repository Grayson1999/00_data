import re

def get_clean_text(df):
    text = []
    
    for i in range(0, len(df)):
        temp = df[i]
        temp = re.sub('[-=+,#/\:$.@*\"※&%ㆍ』\\‘|\(\)\[\]\<\>`\'…《\》]', '', temp) # 특수문자
        # temp = re.sub('([ㄱ-ㅎㅏ-ㅣ]+)', '', temp) # 한글 자음, 한글 모음
        temp = re.sub('([♡❤✌❣♥ᆢ✊❤️✨⤵️☺️;”“]+)', '', temp) # 이모티콘 
        only_BMP_pattern = re.compile("["
                                u"\U00010000-\U0010FFFF"  #BMP characters 이외
                               "]+", flags=re.UNICODE)
        temp = only_BMP_pattern.sub(r'', temp)# BMP characters만
        emoji_pattern = re.compile("["
                                    u"\U0001F600-\U0001F64F"  # emoticons
                                    u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                    u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                    u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                                       "]+", flags=re.UNICODE)
        temp=  emoji_pattern.sub(r'', temp) # 유니코드로 이모티콘 지우기
        text.append(temp)
            
        text1 = "".join(text)
            
    return text1
print(get_clean_text("이렇게 가슴 벅차오를 날이 오다니ㅠㅠㅠ 우리나라 국뽕차게 하는데 최고 아니냐고요....연구원분들 그 동안 얼마나 고생 많으셨을지 가늠도 안되지만 너어어어무 고생많으셨어요!!!! 진짜 다들 멋있고 존경하고 또 열심히 날아가 준 누리야 고생했다!!!!!!!!!행복해라!!!!!!!!"))