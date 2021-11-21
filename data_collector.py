import pandas as pd
from tqdm import tqdm

from jvc import *


class TopicCollector():
    def __init__(self):
        self.new_data = []

    def register_page(self,n):
        url = "https://www.jeuxvideo.com/forums/0-51-0-1-0-{}-0-blabla-18-25-ans.htm".format(1+25*n)
        topics = getTopics(url)
        for topic in filter(lambda x: x!={}, topics):
            try:
                message = getPosts(topic['topic_url'])[0]['post_message']
                id = topic['topic_id']
                title = topic['topic_title']
                author = topic['topic_author']
                self.new_data.append([id,title,message,author])
            except IndexError:
                continue

    def save(self,path):
        df = pd.DataFrame(self.new_data, columns =['id','title','content','author'])
        df.drop_duplicates(subset=['id'],inplace=True)
        df.to_csv(path,index=False)

    def run(self,n,path='ds.csv'):
        for k in tqdm(range(n+1)):
            self.register_page(k)
            if not(k%100):
                self.save(path)
                print("saved")
        df = pd.DataFrame(self.new_data, columns =['id','title','content','author'])
        df.drop_duplicates(subset=['id'],inplace=True)
        df.to_csv(path,index=False)

if __name__ == "__main__":
    t = TopicCollector()
    t.run(1000,path="data/ds.csv")
