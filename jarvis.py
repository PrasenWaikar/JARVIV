#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os


# In[4]:


def speak(audio):
       pass      #For now, we will write the conditions later.


engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices') #getting details of current voice

engine.setProperty('voices', voices[1].id)

def speak(audio):

 engine.say(audio) 
 
 engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")
        
    elif hour>=12 and hour<18:
        speak("good afternoon")
        
    else:
        ("good evening!")
        
        
    speak("I am Jarvis, please tell me how may i help you")
    
    
def takeCommand():
    #takes microphone input from user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
        
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.
        
    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query


    

        
        
    
#Without this command, speech will not be audible to us.    
if __name__=="__main__" :
    
    wishMe()
    while True:
#if 1:
        
        query = takeCommand().lower()
        #logic for executing tasks based on query
        
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
            
        elif 'hello' in query:
            speak("How may I help you")
            
            
            
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        elif 'open google' in query:
            webbrowser.open("google.com")
            
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
            
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {strTime}")
            
        elif 'open visual studio code' in query:
            codePath= "C:\\Users\\prase\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)  
            
            
        elif 'play music' in query:
            music_dir = 'D:\\music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[6]))
            
            
        elif 'play video' in query:
            vid = 'D:\\video'
            vidd = os.listdir(vid)
            print(vid)    
            os.startfile(os.path.join(vid, vidd[0]))
            
            
       
       
            
                 
            
        
            

 


 


# In[ ]:




