from comment import arrangement

company = "naver"
search = "한동훈"
start_date = "20220620"
end_date = "20220623"
date = "20220620"

arrangement.Comment(f'./result/{company}_news/news_{search}_{company}_{start_date}_{end_date}__{date[:6]}.json')