import os


url_dic={"런닝맨":["https://www.youtube.com/watch?v=BhBHZq8AWMI&t=1114s", "https://www.youtube.com/watch?v=8SDktVaHHYs","https://www.youtube.com/watch?v=wWjkiG_aTrY&t=822s"]}

for key in url_dic.keys():
    for i in range(len(url_dic[key])):
        os.system("youtube-comment-downloader --url https://www.youtube.com/watch?v=ScMzIvxBSi4 --output ScMzIvxBSi4.json")
