# replies=['hello, how are you','nice to meet you']

import json
import random
# with open('chatbot.json','w') as f:
#     json.dump(replies,f)
with open('chatbot.json','r')as f:
    jsonResult=(json.load(f))

while True:
    userMessage=input('User: ')
    if str(userMessage.lower()) == "bye" : 
        print('Machine: Good Bye!')
        break

    print('Machine: '+random.choice(jsonResult))
