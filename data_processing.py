import pandas as pd
import re

def remove_urls(text):
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    return url_pattern.sub(r'', text)

def remove_emoji(string):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)

class DataProcessor():
    def __init__(self,path='ds.csv'):
        self.path = path
        self.df = pd.read_csv(path)
        self.df["content"] = self.df["content"].astype(str)
    
    def process(self):
        self.df["content"] = self.df["content"].apply(lambda text: remove_emoji(text))
        self.df["content"] = self.df["content"].apply(lambda text: remove_urls(text))
        self.df["title"] = self.df["title"].apply(lambda text: remove_emoji(text))
        self.df["title"] = self.df["title"].apply(lambda text: remove_urls(text))
        self.df["data"] = self.df["title"] + "\n" + self.df["content"]
        self.df.to_csv("processed_"+self.path,index=False)
        
if __name__ == "__main__":
    dp = DataProcessor()
    dp.process()