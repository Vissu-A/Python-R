from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer,ListTrainer
import os

def setup():
    chatbot = ChatBot('Bot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer')
    # for file in os.listdir('../data/'):
    #     convData = open(r'../data/' + file,encoding='latin-1').readlines()
    #     chatbot.set_trainer(ListTrainer)
    #     chatbot.train(convData)
        #print("Training completed")
    # chatbot.train('C:/Users/vadapala/Desktop/my_export.json')

    # order = ['how to cancel my order?','sure, follow the below steps to cancel order','how to place order?','That\'s good, here are the steps to place order','how can i track my order?','here steps to track your order']
    chatbot.set_trainer(ListTrainer)
    # chatbot.train(order)
    
    # booking = ['book flight ticket?','<a href="https://www.redbus.in">Click to Book</a>','show some animal inages?','<a href="https://www.pexels.com/search/animals/">Animal images</a>']
    # images = ['show me some animal images?','']
    data = open(r'C:/Users/vadapala/Desktop/flowerimages.txt').readlines()
    print(type(data))    # List
    chatbot.train(data)
    chatbot.trainer.export_for_training('C:/Users/vadapala/Desktop/export.yml')   # Exporting chatbot knowledgebase to an external file

setup()
