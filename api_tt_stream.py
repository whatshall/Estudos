import json
import tweepy
from json.tool import main
from threading import main_thread
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler, Stream
from datetime import datetime

# AS CHAVES DE ACESSO
consumer_key = "jB7J58ABmLTtgJz4zSRihXdRp" # api key
consumer_secret = "W8fNTcDDNyo47ttcr1yPJBZzzJv8m5VQH424bacv4iPvc34FHR" # api secret key"

acess_token = "1369270012792410112-mJloNVTxXBd4Th0C3XyMyKUrk5BZLo" # Access Token
acess_token_secret = "bGlQkfOdRrkPTYBZNLs59TN0KuMcnt3SSvyFA7nEDiBDe" # Access Token Secret

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
