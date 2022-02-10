import json
import tweepy
from json.tool import main
from threading import main_thread
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler, Stream
from datetime import datetime

# AS CHAVES DE ACESSO
consumer_key = "" # api key
consumer_secret = "" # api secret key"

acess_token = "-mJloNVTxXBd4Th0C3XyMyKUrk5BZLo" # Access Token
acess_token_secret = "" # Access Token Secret

# Definir arquivo de saída p/ armazenar os tweets coletados
data_hoje = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
out = open(f"tweets_coletados_{data_hoje}.txt", "w")

# Classe p/ conexão com o tt

class MyStreamListener(tweepy.StreamListener):

    def on_data(self, data):
        itemString = json.dumps(data)
        out.write(itemString + "\n")
        return True

    def on_error(sef,status):
        print(status)

# Função MAIN
if __name__ == "__main__":
    l = MyStreamListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(acess_token, acess_token_secret)

    stream = Stream(auth, l)
    stream.filter(track = ["Biden"]) #lista de palavras chaves pra trackeamento
