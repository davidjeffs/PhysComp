import synthesize_text
import transcribe_streaming_mic
import asyncio
import time
import pyttsx3
import random
import threading
from  AppKit import NSSpeechSynthesizer

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 150)
engine.setProperty('voice', voices[10].id)

nssp = NSSpeechSynthesizer

ve = nssp.alloc().init()

def speak_text(text):
    ve.startSpeakingString_(text)
    while not ve.isSpeaking():
        time.sleep(0.1)

    while ve.isSpeaking():
        time.sleep(0.1)  

def read_post():
    #Filler for when we pull data from facebook
    speak_text('Joe Bloggs posted: I love it, it is good, weed is amazing man oh man oh man')
    
    
def read_post_sequence():
    audio = threading.Thread(target=read_post_sequence_audio)
    options = threading.Thread(target=read_post_options)
    audio.start()
    options.start()

def read_post_sequence_audio(typeofmessage):
    NSSpeechImmediateBoundary = 0
    read_post()
    time.sleep(1)
    speak_text('Please dial one to read the next ' + typeofmessage + '. two to read the ' + typeofmessage + ' again. three to add a reaction. four to comment. five to share this ' + typeofmessage + ',dial nine to listen again, dial zero to go back')
    
def read_post_options(typeofmessage):
    try:
        answer = input_with_timeout("answer:", 15)
    except TimeoutExpired:
        while not ve.isSpeaking():
            read_post_sequence_audio(typeofmessage)
    else:    
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

            
def news_feed_sequence(typeofmessage):
    audio = threading.Thread(target=news_feed_sequence_audio, args=(typeofmessage,))
    options = threading.Thread(target=news_feed_options, args=(typeofmessage,))
    audio.start()
    options.start()

def news_feed_sequence_audio(typeofmessage):
    NSSpeechImmediateBoundary = 0
    ## this needs to be changed to read the first/next news post#
    read_post()
    speak_text('Please dial one to add a reaction. two to add a comment. three to share this post. four to listen to the next post, dial nine to listen again, dial zero to go back')
    
def news_feed_options(typeofmessage):
    try:
        answer = input_with_timeout("answer:", 15)
    except TimeoutExpired:
        while not ve.isSpeaking():
            news_feed_sequence_audio(typeofmessage)
    else:
        if (int(answer)==1):

            reaction_list_sequence(typeofmessage)
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
            
def comments_list():
    audio = threading.Thread(target=comment_list_audio)
    options = threading.Thread(target=comment_list_options)
    audio.start()
    options.start() 
    
def comment_list_audio(typeofmessage):
    NSSpeechImmediateBoundary = 0
    time.sleep(1)
    speak_text('You have chosen to comment on the ' + typeofmessage + '. Please dial one to make a new comment. two to read other comments, dial nine to listen again, dial zero to go back.')
        
def comment_list_options(typeofmessage):
    try:
        answer = input_with_timeout("answer:", 15)
    except TimeoutExpired:
        comment_list_audio(typeofmessage)
    else:
        if (int(answer)==1):

            write_post(typeofmessage)
        elif (int(answer)==2):

            read_post_sequence_audio(typeofmessage)
        elif (int(answer)==9):

            comment_list_audio(typeofmessage)
        elif (int(answer)==0):

            read_post_sequence_audio(typeofmessage)

def check_for_comments(typeofmessage):
    NSSpeechImmediateBoundary = 0
    if (bool(random.getrandbits(1))):
        read_post_sequence_audio(typeofmessage) #grab the comment and read it out.
    else:
        speak_text('There are no comments on this post')
        read_post_sequence_audio(typeofmessage) #read the post
        
def reaction_list_sequence(typeofmessage):
    audio = threading.Thread(target=reaction_list_audio, args=(typeofmessage,))
    options = threading.Thread(target=reaction_list_options, args=(typeofmessage,))
    audio.start()
    options.start()          

def reaction_list_audio(typeofmessage):
    NSSpeechImmediateBoundary = 0
    speak_text('You have chosen to react. Please dial one to read the '+ typeofmessage + ' again. dial two to like this ' + typeofmessage + '. three to love this ' + typeofmessage + '. four to ha ha this ' + typeofmessage + '. five to wow this ' + typeofmessage + '. six to sad this ' + typeofmessage + '. seven to angry this ' + typeofmessage + ', dial nine to listen again, dial zero to go back.')    
    
def reaction_list_options(typeofmessage):
    reaction=''
    try:
        answer = input_with_timeout("answer:", 15)
    except TimeoutExpired:
        reaction_list_sequence(typeofmessage)
    else:
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
            NSSpeechImmediateBoundary = 0
            speak_text('You have reacted to      ' + reaction + ' this ' + typeofmessage)
            
        #need code here to add reaction to the post being looked at
        if (typeofmessage == "news post"):
            news_feed_sequence(typeofmessage)

def write_post_sequence(typeofmessage):
    audio = threading.Thread(target=write_post_audio, args=(typeofmessage,))
    options = threading.Thread(target=write_post_options, args=(typeofmessage,))
    audio.start()
    options.start()    
        
    
def write_post_audio(typeofmessage):
    NSSpeechImmediateBoundary = 0
    speak_text('Please record your '+ typeofmessage + ' after the beep. Please dial one to end the recording. dial zero to go back. dial nine to listen again.')

def write_post_options(typeofmessage):
    NSSpeechImmediateBoundary = 0
    try:
        answer = input_with_timeout("answer:", 15)
    except TimeoutExpired:
        write_post_audio(typeofmessage)
    else:
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
    speak_text('Beep beep')
    
    listen_and(typeofmessage)
    

def listen_and(typeofmessage):
    audio = threading.Thread(target=listen_to, args=(typeofmessage,))
    audio.start()

def and_post(typeofmessage, post):
    audio = threading.Thread(target=post_message, args=(typeofmessage,post))
    audio.start()

def listen_to(typeofmessage):
    NSSpeechImmediateBoundary = 0
    text = transcribe_streaming_mic.main(0)
    time.sleep(1)
    speak_text('You said ' + text +'. please dial 1 to post. dial 0 to record again.')
    and_post(typeofmessage, text)
    
def post_message(typeofmessage, post):
    NSSpeechImmediateBoundary = 0
    try:
        answer = input_with_timeout("answer:", 4)
    except TimeoutExpired:
        listen_and_post(typeofmessage)
    else:
        if (int(answer)==0):
            write_post(typeofmessage)
        elif (int(answer)==1):

            speak_text('Your ' + typeofmessage +' has been posted.')
             
            news_feed_sequence_audio(typeofmessage)
            
def share_sequence():
    audio = threading.Thread(target=messages_sequence_audio)
    options = threading.Thread(target=messages_options)
    audio.start()
    options.start()
            
    
def share_list_audio(typeofmessage):
    NSSpeechImmediateBoundary = 0
    time.sleep(1)
    speak_text('You have chosen to share the ' + typeofmessage + '. Please dial one to add a comment to the share. dial two to share without commenting, dial nine to listen again, dial zero to go back')

    
def share_list_options(typeofmessage):
    NSSpeechImmediateBoundary = 0
    try:
        answer = input_with_timeout("answer:", 15)
    except TimeoutExpired:
        while not ve.isSpeaking():
            share_sequence()
    else:
        if (int(answer)==1):

            write_post(typeofmessage)
        elif (int(answer)==2):

            ve.startSpeakingString_('The ' + typeofmessage + ' has been shared. ')
            while not ve.isSpeaking():
                time.sleep(0.1)

            while ve.isSpeaking():
                time.sleep(0.1)
            read_post_sequence_audio(typeofmessage)
        elif (int(answer)==9):

            share_list_audio(typeofmessage)
        elif (int(answer)==0):

            read_post_sequence_audio(typeofmessage)

            
def messaging_sequence():
    audio = threading.Thread(target=messages_sequence_audio)
    options = threading.Thread(target=messages_options)
    audio.start()
    options.start()
        
def messages_sequence_audio():
    NSSpeechImmediateBoundary = 0
    time.sleep(1)
    speak_text('To access messages please select a person. Please dial one for David Jeffs, dial two for William Hayward, dial three for Julien Tran, dial four for Yaxin Cui, dial 8 for someone else, dial nine to listen again. dial zero to go back.')

def messages_options(): 
    NSSpeechImmediateBoundary = 0
    try:
        answer = input_with_timeout("answer:", 15)
    except TimeoutExpired:
        while not ve.isSpeaking():
            messaging_sequence()
    else:
        if (int(answer)==1):

            messaging('David Jeffs')
        elif (int(answer)==2):

            messaging('William Hayward')
        elif (int(answer)==3):

            messaging('Julien Tran')
        elif (int(answer)==4):
            messaging('Yaxin Cui')
        elif (int(answer)==5):
            messaging('blah')
        elif (int(answer)==8):
            messaging_search()
        elif (int(answer)==9):
            messages_sequence_audio()
        elif (int(answer)==0):
            opening_sequence_audio()

def opening_sequence():
    audio = threading.Thread(target=opening_sequence_audio)
    options = threading.Thread(target=opening_sequence_options)
    audio.start()
    options.start()
            
def opening_sequence_audio():
    NSSpeechImmediateBoundary = 0
    try:
        speak_text('Welcome to Facebook. Please dial one to see your messages, dial two to write a wall post, dial three to read the news feed. dial nine to listen again')

    except AttributeError:
        pass
    
    
def opening_sequence_options():
    try:
        answer = input_with_timeout("answer:", 15)
    except TimeoutExpired:
        while not ve.isSpeaking():
            opening_sequence()
    else:
        if (int(answer)==1):

            messaging_sequence()
        elif (int(answer)==2):

            write_post_sequence("wall post")
        elif (int(answer)==3):

            news_feed_sequence("news post")
        elif (int(answer)==9):
            opening_sequence()




def main():
    opening_sequence()
    #opening_sequence_audio()
    #opening_sequence_options()






class TimeoutExpired(Exception):
    pass

import select
import sys

def input_with_timeout(prompt, timeout):
    sys.stdout.write(prompt)
    sys.stdout.flush()
    ready, _, _ = select.select([sys.stdin], [],[], timeout)
    if ready:
        return sys.stdin.readline().rstrip('\n') # expect stdin to be line-buffered
    raise TimeoutExpired
    
    

if __name__ == "__main__":
    main()
