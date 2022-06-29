import re

def get_clean_text(df):
    text = []
    
    for i in range(0, len(df)):
        temp = df[i]
        temp = re.sub('[-=+,#/\:$.@*\"※&%ㆍ』\\‘|\(\)\[\]\<\>`\'…《\》]', '', temp) # 특수문자
        temp = re.sub('([ㄱ-ㅎㅏ-ㅣ]+)', '', temp) # 한글 자음, 한글 모음
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
print(get_clean_text('과학자가 존경받는나라!👍👍👍'))