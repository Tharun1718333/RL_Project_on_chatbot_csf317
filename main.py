from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import time
time.clock = time.time
bot1 = ChatBot('Buddy1')
trainer1 = ChatterBotCorpusTrainer(bot1)
trainer1.train("chatterbot.corpus.english.ai","chatterbot.corpus.english.emotion","chatterbot.corpus.english.literature","chatterbot.corpus.english.food","chatterbot.corpus.english.botprofile","chatterbot.corpus.english.history","chatterbot.corpus.english.sports","chatterbot.corpus.english.psychology","chatterbot.corpus.english.money")
bot2 = ChatBot('Buddy2')
trainer2 = ChatterBotCorpusTrainer(bot2)
trainer2.train("chatterbot.corpus.english.computers","chatterbot.corpus.english.gossip","chatterbot.corpus.english.conversations","chatterbot.corpus.english.health","chatterbot.corpus.english.greetings","chatterbot.corpus.english.politics","chatterbot.corpus.english.movies","chatterbot.corpus.english.trivia","chatterbot.corpus.english.science")
file = open("top_10k_words.txt")
combined_top_10_k = file.read()
top_10_k = combined_top_10_k.split()
file1 = open("text_loop_stopper.txt")
combined_text_loop_stopper = file1.read()
text_loop_stopper = combined_text_loop_stopper.splitlines()
bot1list = ['hello peter']
bot2list = ['hello doctor']
bannedlist = []
def no_of_words(a):
    res = len(a.split())
    return len
def word_value(a):
    if(a in top_10_k):
        return  1
    return 0
def append_bot1(a):
    if(a in bot1list):
        return False
    bot1list.append(a)
    return True
def append_bot2(a):
    if(a in bot2list):
        return False
    bot2list.append(a)
    return True
def word_score(a):
    res = a.split()
    l1 = len(res)
    switcher = {
        1:-3,
        2:-2,
        3:-1,
        4:0,
        5:1,
        6:2,
        7:3,
        8:2,
        9:1,
        10:0,
    }
    return  switcher.get(l1,0)/5
def is_banned(a):
    if(a in bannedlist):
        return True
    return False
def sentence_word_score(a):
    res = a.split()
    score = 0
    for i in res:
        score = score + word_value(i)
    return score/10
def current_streak(a):
    return a/500
request = input("YOU:")
response = bot1.get_response(request)
request = str(response)
r1 = 0.9  #initial policy value for word length score
r2 = 0.6 #initial policy value for streak score
r3 = -0.5  #initial policy value for word score
streak = 0
reward = 0
loop_text_counter = 0
count = 0
while 1:
    if request not in bot1list:
        bot1list.append(request)
    else:
        reward = (r1*word_score(request)) + (r2*sentence_word_score(request)) - (r3*current_streak(streak))
        if reward > 0.5:
            r1 = r1 + ((r1*(0 - reward)*r1*word_score(request))/reward)
            r2 = r2 + ((r2*(0 - reward)*r2*sentence_word_score(request))/reward)
            r3 = r3 + ((r3 * (0 - reward) *r3*current_streak(streak)) / reward)
            print("r1",r1,"r2",r2,"r3",r3)
        loop_text_counter = loop_text_counter +1
        loop_text_counter = (loop_text_counter % 78)
        k = loop_text_counter
        print("r1", r1, "r2", r2, "r3", r3)
        # print("r1",r1 * word_score(request), "r2",r2 * sentence_word_score(request),"r3", (r3 * current_streak(streak)))
        streak = 0
        print(reward)
        print("new value_____________________________________________________________")
        response = text_loop_stopper[k]
    print("Bot1 response:",response)
    response = bot2.get_response(response)
    request = str(response)
    if request not in bot2list:
        bot2list.append(request)
    else:
        reward = (r1 * word_score(request)) + (r2 * sentence_word_score(request)) - (r3 * current_streak(streak))
        if reward > 0.8:
            r1 = ((r1 * (reward - 0.8) * r1 * word_score(request)) / reward)
            r2 = ((r2 * (reward - 0.8) * r2 * sentence_word_score(request)) / reward)
            r3 = ((r3 * (reward - 0.8) * r3 * current_streak(streak)) / reward)
            print("r1", r1, "r2", r2, "r3", r3)
        loop_text_counter = loop_text_counter + 1
        loop_text_counter = loop_text_counter % 78
        k = loop_text_counter
        print("r1", r1, "r2", r2, "r3", r3)
        # print("r1",r1 * word_score(request), "r2",r2 * sentence_word_score(request),"r3", (r3 * current_streak(streak)))
        streak = 0
        print(reward)
        print("new value_____________________________________________________________")
        response = text_loop_stopper[k]
    print("Bot2 response:-",response)
    response = bot1.get_response(response)
    request = str(response)
    streak = streak + 2
    count = count + 2
    print(count)



