from GoogleNews import GoogleNews
from datetime import datetime,timedelta

def get_news():
    dt_today=str(datetime.today().strftime('%m/%d/%Y'))
    dt_previous=datetime.today()-timedelta(days=5)
    dt_previous=str(dt_previous.strftime('%m/%d/%Y'))
    #print(dt_today)
    #print(dt_previous)

    googlenews=GoogleNews(start=dt_previous,end=dt_today)
    googlenews.search('Coronavirus')
    googlenews.getpage(1)
    result1=googlenews.result()
    googlenews.getpage(2)
    result2=googlenews.result()
    result=result1+result2
    news_list=list()
    for i in result:
        if i['desc']!='':
            dic=dict()
            dic['title']=i['title']
            dic['source']=i['media']
            dic['date&time']=i['date']
            dic['desc']=i['desc']
            dic['link']=i['link']
            news_list.append(dic)
    return news_list
