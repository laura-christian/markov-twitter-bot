import os
import twitter
from markov import *

api = twitter.Api(
    consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
    consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
    access_token_key=os.environ['TWITTER_ACCESS_TOKEN_KEY'],
    access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET'])

print api.VerifyCredentials()

filenames = ['leavesofgrass.txt', 'wasteland.txt']
text = open_and_read_file(filenames)
chains = make_chains(text)


def everything(chains):
    random_text = make_text(chains)
    return tweet(random_text)


poem = everything(chains)

def user_options():
    command = raw_input('Enter to tweet again [q to quit] > ')
    if command == 'q':
        return False


while True:
    poem = everything(chains)
    status = api.PostUpdate(poem)
    print status.text
    if not user_options():
        break

# If you updated secrets.sh, you can go to your Twitter 
# timeline to see it.