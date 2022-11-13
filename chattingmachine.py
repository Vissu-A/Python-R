# Some logical adapters
# logic_adapters=['chatterbot.logic.BestMatch'],
# Some filters
# filters=['chatterbot.filters.RepetitiveResponseFilter']



from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Creating bot

chatbot = ChatBot('mybot',
                          storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
                          input_adapter='chatterbot.input.TerminalAdapter',
                          output_adapter='chatterbot.output.TerminalAdapter',
                          database_uri='mongodb://localhost:27017/chatterbot-database',)

    
# Setting trainer to train the bot
chatbot.set_trainer(ChatterBotCorpusTrainer)

# Starting the training
chatbot.train('chatterbot.corpus.english')

while 1:
	question = input("user:")
	answer = chatbot.get_response(question)
	print("bot:",answer)





