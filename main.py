import synthesize_text
import transcribe_streaming_mic
import asyncio
import time
import pyttsx3
import random

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 150)
engine.setProperty('voice', voices[11].id)

def opening_sequence_audio():
    time.sleep(1)
    engine.say('Welcome to Facebook.')
    engine.runAndWait()
    engine.say('Please dial one to see your messages, dial two to write a wall post, dial three to read the news feed.')
    engine.runAndWait()
    engine.say('dial nine to listen again')
    engine.runAndWait()
    opening_sequence_options()
    
def read_post():
    #Filler for when we pull data from facebook
    engine.say('Joe Bloggs posted: I love it, it is good, weed is amazing man oh man oh man')
    engine.runAndWait()
    
def read_post_sequence_audio(typeofmessage):
    read_post()
    time.sleep(1)
    engine.say('Please dial one to read the next ' + typeofmessage + '. two to read the ' + typeofmessage + ' again. three to add a reaction. four to comment. five to share this ' + typeofmessage)
    engine.runAndWait()
    engine.say('dial nine to listen again')
    engine.runAndWait()
    engine.say('dial zero to go back')
    engine.runAndWait()
    
def read_post_options(typeofmessage):
    answer = input("answer?")
    
    #read the next post.
    if (int(answer)==1):
        read_post_sequence_audio(typeofmessage)
        
    #read the same post again
    elif (int(answer)==2):
        read_post_sequence_audio(typeofmessage)
        
    #add a reaction to the post
    elif (int(answer)==3):
        reaction_list_audio()
        
    #comment on the post
    elif (int(answer)==4):
        reaction = 'wow'
        
    #share the post
    elif (int(answer)==5):
        reaction = 'sad'


def news_feed_sequence_audio(typeofmessage):
    ## this needs to be changed to read the first/next news post#
    read_post()
    engine.say('Please dial one to add a reaction. two to add a comment. three to share this post. four to listen to the next post')
    engine.runAndWait()
    engine.say('dial nine to listen again')
    engine.runAndWait()
    engine.say('dial zero to go back')
    engine.runAndWait()
    news_feed_options(typeofmessage)
    
def news_feed_options(typeofmessage):
    answer = input("answer?")
    if (int(answer)==1):
        reaction_list_audio(typeofmessage)
    elif (int(answer)==2):
        comment_list_audio(typeofmessage)
    elif (int(answer)==3):
        share_list_audio(typeofmessage)    
    elif (int(answer)==4):
        reaction = 'wow'
    elif (int(answer)==5):
        reaction = 'sad'
    elif (int(answer)==6):
        reaction = 'angry'
    
    
def comment_list_audio(typeofmessage):
    time.sleep(1)
    engine.say('You have chosen to comment on the ' + typeofmessage + '. Please dial one to make a new comment. two to read other comments.')
    engine.runAndWait()
    engine.say('dial nine to listen again')
    engine.runAndWait()
    engine.say('dial zero to go back')
    engine.runAndWait()
    comment_list_options(typeofmessage)  
    
def comment_list_options(typeofmessage):
    answer = input("answer?")
    if (int(answer)==1):
        write_post(typeofmessage)
    elif (int(answer)==2):
        read_post_sequence_audio(typeofmessage)
    elif (int(answer)==9):
        comment_list_audio(typeofmessage)
    elif (int(answer)==0):
        read_post_sequence_audio(typeofmessage)

def check_for_comments(typeofmessage):
    if (bool(random.getrandbits(1))):
        read_post_sequence_audio(typeofmessage) #grab the comment and read it out.
    else:
        engine.say('There are no comments on this post')
        read_post_sequence_audio(typeofmessage) #read the post
    
def reaction_list_audio(typeofmessage):
    engine.say('You have chosen to react. Please dial one to read the '+ typeofmessage + ' again. dial two to like this ' + typeofmessage + '. three to love this ' + typeofmessage + '. four to ha ha this ' + typeofmessage + '. five to wow this ' + typeofmessage + '. six to sad this ' + typeofmessage + '. seven to angry this ' + typeofmessage + '.')
    engine.runAndWait()
    engine.say('dial nine to listen again')
    engine.runAndWait()
    engine.say('dial zero to go back')
    engine.runAndWait()
    reaction_list_options(typeofmessage)
    
    
def reaction_list_options(typeofmessage):
    reaction=''
    answer = input("answer?")
    if (int(answer)==1):
        read_post()
    elif (int(answer)==2):
        reaction = 'like'
    elif (int(answer)==3):
        reaction = 'love'
    elif (int(answer)==4):
        reaction = 'haha'
    elif (int(answer)==5):
        reaction = 'wow'
    elif (int(answer)==6):
        reaction = 'sad'
    elif (int(answer)==7):
        reaction = 'angry'
    if (int(answer) > 1 < 8):
        engine.say('                   You have reacted to      ' + reaction + ' this ' + typeofmessage)
        engine.runAndWait()
    #need code here to add reaction to the post being looked at
    if (typeofmessage == "news post"):
        news_feed_sequence_audio(typeofmessage)
    
    
        
    
def write_post(typeofmessage):
    engine.say('Please record your '+ typeofmessage + ' after the beep. Please dial one to end the recording. dial zero to go back. dial nine to listen again.')
    engine.runAndWait()
    answer = input("answer?")
    if (int(answer)==0):
        if (typeofmessage=='comment'):
            read_post('comment')
            comment_list_audio(typeofmessage)
        if (typeofmessage=='shared post'):
            read_post('shared post')
            read_post_sequence_audio(typeofmessage)
    elif (int(answer)==9):
        write_post(typeofmessage) 
    
    time.sleep(1)
    engine.say('Beep beep')
    engine.runAndWait()
    listen_to(typeofmessage)
    
def listen_to(typeofmessage):
    text = transcribe_streaming_mic.main(0)
    
    time.sleep(1)
    engine.say('You said ' + text +'. please dial 1 to post. dial 0 to record again.')
    engine.runAndWait()
    post_message(typeofmessage)
    
def post_message(typeofmessage):
    answer = input("answer?")
    if (int(answer)==0):
        write_post(typeofmessage)
    elif (int(answer)==1):
        engine.say('Your ' + typeofmessage +' has been posted.')
        engine.runAndWait() 
        news_feed_sequence_audio(typeofmessage)

def share_list_audio(typeofmessage):
    time.sleep(1)
    engine.say('You have chosen to share the ' + typeofmessage + '. Please dial one to add a comment to the share. dial two to share without commenting.')
    engine.runAndWait()
    engine.say('dial nine to listen again')
    engine.runAndWait()
    engine.say('dial zero to go back')
    engine.runAndWait()
    share_list_options(typeofmessage)  
    
def share_list_options(typeofmessage):
    answer = input("answer?")
    if (int(answer)==1):
        write_post(typeofmessage)
    elif (int(answer)==2):
        engine.say('The ' + typeofmessage + ' has been shared. ')
        read_post_sequence_audio(typeofmessage)
    elif (int(answer)==9):
        share_list_audio(typeofmessage)
    elif (int(answer)==0):
        read_post_sequence_audio(typeofmessage)

def opening_sequence_options():
    answer = input("answer?")
    if (int(answer)==1):
        write_post()
    elif (int(answer)==2):
        read_post()
        newsfeed_sequence_audio()
    elif (int(answer)==3):
        news_feed_sequence_audio('news post')
    elif (int(answer)==9):
        opening_sequence_audio()


def main():
    opening_sequence_audio()
    #opening_sequence_audio()
    #opening_sequence_options()

if __name__ == "__main__":
    main()
