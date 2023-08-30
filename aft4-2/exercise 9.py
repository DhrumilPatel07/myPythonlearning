import requests
import json


def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    speak("news for today")
    url = "https://newsapi.org/v2/everything?q=tesla&from=2022-01-11&sortBy=publishedAt&apiKey=dc82913f2932448c829126e71b50f963"
    news = requests.get(url).text
    news_dict = json.loads(news)
    print(news_dict["articles"])
    arts = news_dict['articles']
    for article in arts:
        speak(article['title'])
        speak("moving on to the next news...listen carefully")
    speak("thanks for listening")