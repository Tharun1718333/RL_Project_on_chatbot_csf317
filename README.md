# RL_Project_on_chatbot_csf317

Hi Folks!!

This project deals with implementation of conversational chatbots using Reinforcement
learning taking into account a different policy rather than the one implied
There are a lot of available chatbots in the current market which can generate pretty good
responses for any sentence but most of these bots fail to make a conversation. They only
factor in the short term reward(greedy approach) instead of considering the impact it has
on the next conversations.
So here we decided to implement an off-policy method in which the behavioral policy is
a greedy approach and the target policy is an exploration-based approach and try to see
the results we took the same approach as the research paper but we changed the factors
considered (the factors we considered are 1, number of words in the commonly used
words list 2, number of words in the sentence 3, the current streak).
We implement the algorithm using chatterbot by training two chatbots and making them
have a conversation.
Action,States,Policy and Reward
Action:-
An action a is the dialogue utterance to generate. The action space is infinite since
arbitrary-length sequences can be generated.
State:-
The has the current streak of the conversation (the number of exchanges that happened
between the bots after a duplicate was detected and replaced)
Policy:-
We follow the behavioral policy for this and from the response generated from the
LTSM(seq2seq) and maximum likelihood function we take the result and check if the
same statement is repeated or not by the bot. If yes, we check the reward score if the
target policy predicts correctly that the statement should be replaced then we leave the
target policy unchanged but if the target policy predicts incorrectly we change the
coefficients of the reward coefficients(target policy) as per the error obtained in the
prediction after every such repetition, we replace the current response with a random
statement from a separate data set and update the streak to 0.
Reward:-
The rewards are as mentioned above the implementation is as follows:
1. Streak reward :- the current streak is divided by 500
2. Word score individual :- this is given based on the no of words in the current
response that are present in the most commonly used english words
3. Word length score :- these are given as per the bell curve obtained form data and
will output a rounded integer based on the given length
6
Data sets used:-
Coronell movie corpus data set(220,579 conversational exchanges between 10,292 pairs
of movie characters)
Reddit comments for random sentences(comments from a video from r/wholesome)
Top ten thousand words from github repository


The whole code is in a single file



feel free to use it in any of your work
