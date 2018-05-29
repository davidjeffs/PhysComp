import synthesize_text
import transcribe_streaming_mic
import time
import random
import threading
from  AppKit import NSSpeechSynthesizer
from pysine import sine


nssp = NSSpeechSynthesizer

ve = nssp.alloc().init()

def speak_text(text):
    ve.startSpeakingString_(text)
    while not ve.isSpeaking():
        time.sleep(0.1)

    while ve.isSpeaking():
        time.sleep(0.1)  

##################### READ A POST AND SUGGEST OPTIONS TO INTERACT WITH IT ##################
def read_post_sequence():
    audio = threading.Thread(target=read_post_sequence_audio)
    options = threading.Thread(target=read_post_options)
    audio.start()
    options.start()

def read_post_sequence_audio(typeofmessage):
    NSSpeechImmediateBoundary = 0
    ## need to replace the message variable with the message pulled from facebook ###
    message = 'Joe Bloggs posted: I love it, it is good, weed is amazing man oh man oh man'
    time.sleep(1)
    speak_text(message + 'Please dial one to read the next ' + typeofmessage + '. two to read the ' + typeofmessage + ' again. three to add a reaction. four to comment. five to share this ' + typeofmessage + ',dial nine to listen again, dial zero to go back')
    
def read_post_options(typeofmessage):
    try:
        answer = input_with_timeout("answer:", 15)
    except TimeoutExpired:
        while not ve.isSpeaking():
            read_post_sequence_audio(typeofmessage)
    else:    
        #read the next post.
        if (int(answer)==1):
            ### need function here to read the next wall post###
            read_post_sequence(typeofmessage)

        #read the same post again
        elif (int(answer)==2):
            ### need function here to re-read the same wall post ###
            read_post_sequence(typeofmessage)

        #add a reaction to the post
        elif (int(answer)==3):
            reaction_list_sequence()

        #comment on the post
        elif (int(answer)==4):
            comment_list_sequence()
            
        #share this post
        elif (int(answer)==4):
            share_sequence()
            
        #share the post
        elif (int(answer)==9):
            read_post_sequence()
            
        #share the post
        elif (int(answer)==0):
            news_feed_sequence()
            
##################################################################################################
            
def news_feed_sequence(typeofmessage):
    audio = threading.Thread(target=news_feed_sequence_audio, args=(typeofmessage,))
    options = threading.Thread(target=news_feed_options, args=(typeofmessage,))
    audio.start()
    options.start()

def news_feed_sequence_audio(typeofmessage):
    NSSpeechImmediateBoundary = 0
    ## this needs to be changed to read the first/next news post#
    message = "this is the next post"
    speak_text(message + 'Please dial one to add a reaction. two to add or view comments. three to share this post. four to listen to the next post, dial nine to listen again, dial zero to go back')
    
def news_feed_options(typeofmessage):
    try:
        answer = input_with_timeout("answer:", 15)
    except TimeoutExpired:
        while not ve.isSpeaking():
            news_feed_sequence(typeofmessage)
    else:
        if (int(answer)==1):
            
            reaction_list_sequence(typeofmessage)
        elif (int(answer)==2):
            ### needs extra variables to comment on the current post ####
            comments_list(typeofmessage)
        elif (int(answer)==3):
            ### needs extra variables to share the current post ####
            share_sequence(typeofmessage)    
        elif (int(answer)==4):
            ### this needs a function to listen to the next news post
            news_feed_sequence_audio(typeofmessage)        
        elif (int(answer)==5):
            reaction = 'sad'
        elif (int(answer)==6):
            reaction = 'angry'

            
################# ADDING A COMMENT TO A POST #####################################  

def comments_list(typeofmessage):
    audio = threading.Thread(target=comment_list_audio, args=(typeofmessage,))
    options = threading.Thread(target=comment_list_options, args=(typeofmessage,))
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
            ### create a new comment for the site ###
            write_comment_sequence(typeofmessage)
        elif (int(answer)==2):

            read_post_sequence(typeofmessage)
        elif (int(answer)==9):

            comments_list(typeofmessage)
        elif (int(answer)==0):
            read_post_sequence(typeofmessage)

#####################################################################            

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
    time.sleep(1)
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
            
            
#################### RECORD AND POST TO WALL ################################
def write_post_sequence(typeofmessage):
    audio = threading.Thread(target=write_post_audio, args=(typeofmessage,))
    audio.start()
        
    
def write_post_audio(typeofmessage):
    NSSpeechImmediateBoundary = 0
    time.sleep(1)
    speak_text('Please record your '+ typeofmessage + ' after the beep')
    time.sleep(1)
    sine(frequency=600.0, duration=0.5)  # plays a 1s sine wave at 440 Hz
    NSSpeechImmediateBoundary = 0
    text = ""
    while (text == ""):
        text = transcribe_streaming_mic.main(0)
    time.sleep(1)
    speak_text('You said ' + text +'. please dial 1 to post. dial 0 to record again.')
    and_post(typeofmessage, text)


def and_post(typeofmessage, post):
    audio = threading.Thread(target=post_message, args=(typeofmessage,post))
    audio.start()
    
def post_message(typeofmessage, post):
    NSSpeechImmediateBoundary = 0
    try:
        answer = input_with_timeout("answer:", 15)
    except TimeoutExpired:
        listen_and_post(typeofmessage)
    else:
        if (int(answer)==0):
            write_post_sequence(typeofmessage)
        elif (int(answer)==1):
            time.sleep(1)
            #post the message to your wall
            speak_text('Your ' + typeofmessage +' has been posted.')
             
            news_feed_sequence_audio(typeofmessage)
            

############################################################################################## 



#################### RECORD AND POST COMMENT ################################
def write_comment_sequence(typeofmessage):
    audio = threading.Thread(target=write_comment_audio, args=(typeofmessage,))
    audio.start()
        
    
def write_comment_audio(typeofmessage):
    NSSpeechImmediateBoundary = 0
    speak_text('Please record your comment after the beep.')
    time.sleep(1)
    sine(frequency=600.0, duration=0.5) 
    listen_and_comment(typeofmessage)
    
def listen_and_comment(typeofmessage):
    audio = threading.Thread(target=listen_to_comment, args=(typeofmessage,))
    audio.start()
    
def listen_to_comment(typeofmessage):
    NSSpeechImmediateBoundary = 0
    text = ""
    while (text == ""):
        text = transcribe_streaming_mic.main(0)
    time.sleep(1)
    speak_text('Your comment has been posted.')
    after_comment(typeofmessage)
    
def after_comment(typeofmessage):
    audio = threading.Thread(target=after_comment_audio, args=(typeofmessage,))
    options = threading.Thread(target=after_comment_options, args=(typeofmessage,))
    audio.start()
    options.start()
    
def after_comment_audio(typeofmessage):
    NSSpeechImmediateBoundary = 0
    speak_text('Please dial one to continue with this comment tree, dial two to listen to the next comment, dial zero to go back, dial nine to listen again.')
    
def after_comment_options(typeofmessage):
    NSSpeechImmediateBoundary = 0
    try:
        answer = input_with_timeout("answer:", 15)
    except TimeoutExpired:
        while not ve.isSpeaking():
            after_comment(typeofmessage)
    else:
        if (int(answer)==1):

            messaging_sequence()
        elif (int(answer)==2):
            messaging_sequence()
        elif (int(answer)==9):
            opening_sequence()
        elif (int(answer)==0):
            after_comment()
            

############################################################################################## 
            

######################## SHARING A POST #######################################
def share_sequence(typeofmessage):
    audio = threading.Thread(target=share_list_audio, args=(typeofmessage,))
    options = threading.Thread(target=share_list_options, args=(typeofmessage,))
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
            share_sequence(typeofmessage)
    else:
        if (int(answer)==1):
            write_sharecomment_sequence(typeofmessage, 1)
        elif (int(answer)==2):
            write_sharecomment_sequence(typeofmessage, 0)
            read_post_sequence(typeofmessage)
        elif (int(answer)==9):
            share_list_sequence(typeofmessage)
        elif (int(answer)==0):
            read_post_sequence(typeofmessage)
            
            
 #################################################################################################           


#################### ADD COMMENT TO SHARE ################################
def write_sharecomment_sequence(typeofmessage, shareit):
    if (shareit ==1):
        audio = threading.Thread(target=write_sharecomment_audio, args=(typeofmessage,))
        audio.start()
    else:
        sharecomment_sequence("")
        
    
def write_sharecomment_audio(typeofmessage):
    NSSpeechImmediateBoundary = 0
    speak_text('Please record your comment after the beep.')
    time.sleep(1)
    sine(frequency=600.0, duration=0.5)  # plays a 1s sine wave at 440 Hz
    NSSpeechImmediateBoundary = 0
    text = ""
    while (text == ""):
        text = transcribe_streaming_mic.main(0)
    sharecomment_sequence(text)

def sharecomment_sequence(text):
    audio = threading.Thread(target=sharethepost, args=(text,))
    audio.start()    

def sharethepost(message):
    ### code here to share the post ###
    NSSpeechImmediateBoundary = 0
    if (message != ""):
        comment = message
    speak_text('The post has been shared. ')
    news_feed_sequence("news post")
    
       

############################################################################################## 

def read_message():
    speak_text('Joe Bloggs posted: This is the latest message ')
    
def messaging_sequence():
    audio = threading.Thread(target=messages_sequence_audio)
    options = threading.Thread(target=messages_options)
    audio.start()
    options.start()
        
def messages_sequence_audio():
    NSSpeechImmediateBoundary = 0
    
    ####### need a function here to collect the message ####
    message = 'Joe Bloggs posted: This is the latest message '
    time.sleep(1)
    speak_text(message + 'Please dial one to respond to this message, dial two for the next message, dial three to read the rest of the conversation, dial four to search for someone else, dial nine to listen again, dial zero to go back.')

def messages_options(): 
    NSSpeechImmediateBoundary = 0
    try:
        answer = input_with_timeout("answer:", 30)
    except TimeoutExpired:
        while not ve.isSpeaking():
            messaging_sequence()
    else:
        if (int(answer)==1):
            write_message_sequence()
        elif (int(answer)==2):
            ### this needs a funtion to go to the next persons message ###
            messaging_sequence()
        elif (int(answer)==3):
            ### this needs a function to go the next message with this person ####
            messaging_sequence()
        elif (int(answer)==4):
            search_and_message()
        elif (int(answer)==5):
            messaging('blah')
        elif (int(answer)==8):
            messaging_search()
        elif (int(answer)==9):
            messages_sequence()
        elif (int(answer)==0):
            opening_sequence()
            

    
###############################################################################################

#################### RECORD AND POST MESSAGE ################################
def write_message_sequence():
    audio = threading.Thread(target=write_message_audio)
    audio.start()        
    
def write_message_audio():
    NSSpeechImmediateBoundary = 0
    time.sleep(1)
    speak_text('Please record your message after the beep.')
    time.sleep(1)
    sine(frequency=600.0, duration=0.5)  # plays a 1s sine wave at 440 Hz
    listen_and_message()
    
def listen_and_message():
    audio = threading.Thread(target=listen_to_message)
    audio.start()
    
def listen_to_message():
    NSSpeechImmediateBoundary = 0
    ###listens to the person saying the message ###
    text = ""
    while (text == ""):
        text = transcribe_streaming_mic.main(0)
        time.sleep(1)
    print(text)
    speak_text(text) ## check to see if it works ##
    #### code here to message the appropiate person ####
    speak_text('Your message has been posted.')
    after_message()
    
def after_message():
    audio = threading.Thread(target=after_message_audio)
    options = threading.Thread(target=after_message_options)
    audio.start()
    options.start()
    
def after_message_audio():
    NSSpeechImmediateBoundary = 0
    speak_text('Please dial one to continue with this conversation, dial two to listen to the next latest message, dial zero to go back, dial nine to listen again.')
    
def after_message_options():
    NSSpeechImmediateBoundary = 0
    try:
        answer = input_with_timeout("answer:", 15)
    except TimeoutExpired:
        while not ve.isSpeaking():
            after_comment()
    else:
        if (int(answer)==1):
            ### the messages will be read again ###
            messaging_sequence()
        elif (int(answer)==2):
            ### the next message from a different person will be read
            messaging_sequence()
        elif (int(answer)==9):
            opening_sequence()
        elif (int(answer)==0):
            after_message()
            

############################################################################################## 

##################### SEARCH FOR AND MESSAGE A NEW PERSON ##########################
            
def search_and_message():    
    audio = threading.Thread(target=search_and_message_audio)
    audio.start()

def search_and_message_audio():
    NSSpeechImmediateBoundary = 0
    time.sleep(1)
    speak_text('Please state your friends name after the beep')
    time.sleep(1)
    sine(frequency=600.0, duration=0.5)  # plays a 1s sine wave at 440 Hz
    listen_and_find()


def listen_and_find():
    audio = threading.Thread(target=listen_to_name)
    audio.start()
    
def listen_to_name():
    NSSpeechImmediateBoundary = 0
    text = ""
    while (text == ""):
        text = transcribe_streaming_mic.main(0)
    time.sleep(1)
    check_name(text)

def check_name(text):
    audio = threading.Thread(target=name_check, args=(text,))
    audio.start()

    
def name_check(name):
    NSSpeechImmediateBoundary = 0
    speak_text('Is your name spelt like this:')
    NSSpeechImmediateBoundary = 0
    for i in name.replace(" ",""):
        speak_text(i)
        time.sleep(0.5)
    NSSpeechImmediateBoundary = 0
    speak_text('Please dial one for yes, dial two for no')
    
    NSSpeechImmediateBoundary = 0
    answer = input_with_timeout("answer:", 15)

    if (int(answer)==1):
        ## function to view latest messages from this person##
        messaging_sequence()
    elif (int(answer)==2):
        search_and_message_spell()
    elif (int(answer)==9):
        opening_sequence()
    elif (int(answer)==0):
        after_comment()
        
########### SPELL NAME ############

def search_and_message_spell():    
    audio = threading.Thread(target=search_and_message_spelling_audio)
    audio.start()

def search_and_message_spelling_audio():
    NSSpeechImmediateBoundary = 0
    time.sleep(1)
    speak_text('Please spell out your friends name after the beep.')
    time.sleep(1)
    sine(frequency=600.0, duration=0.5)  # plays a 1s sine wave at 440 Hz

    listen_and_find_spelling()


def listen_and_find_spelling():
    audio = threading.Thread(target=listen_to_name_spelling)
    audio.start()
    
def listen_to_name_spelling():
    NSSpeechImmediateBoundary = 0
    text = ""
    while (text == ""):
        text = transcribe_streaming_mic.main(1).replace("space", " ")
    time.sleep(1)
    check_name(text)
    
    
####################################################################################

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
        elif (int(int(answer)>3 and int(answer)<9)):
            NSSpeechImmediateBoundary = 0
            speak_text(answer + ' is not a valid option')
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
