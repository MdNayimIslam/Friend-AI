form chatterbot import chatbot
form chatterbot.trainers import ChatterbotCorpusTrainer
Chatbot = Chatbot('bot')
trainer = ChatterbotCorpusTrainer(Chatbot)
trainer.train('chatterbot')
def main():
    while True:
        query = str(imput(">>"))
        print(Chatbot.get_response(query))
        if "exit" in query:
            break