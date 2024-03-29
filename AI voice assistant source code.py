""" This code is written and hotsed  by Debosmit Neogi """
import pyttsx3 # text to -> speech library
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import smtplib 
#smtplib -> sends email by accesing gmail
import os # this module helps to access files from local device
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-62) # rate -> helps to slow down the voice of the assistant
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning;lord Debosmit")
    elif hour>12 and hour<=18:
        speak("Good afternoon;lord Debosmit")
    else:
        speak("Good evening;lord Debosmit")
    speak("I am Gopal; Sir,how may i help you?")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('my_email', 'password')
    server.sendmail('my_email', to, content)
    server.close()

def searchOnGoogle(query, outputList): 
    speak("The top five search results from Google are listed below.")
    for output in search(query, tld="co.in", num=10, stop=5, pause=2):
        print(output) 
        outputList.append(output) 
    return outputList 

def openLink(outputList): 
    speak("Here’s the first link for you.")
    webbrowser.open(outputList[0])
if __name__ == "__main__":
    wishMe()
    
    while 1:
     
        query = takeCommand().lower()
        if query==0:
            continue;
        if "quit" in str(query) or "exit" in str(query) or "bye" in str(query) or "sleep" in str(query) : 
            speak("ok bye,debosmit") 
            break
        if "who made you" in str(query) or "who created you" in str(query):
            text="The almighty;the exceptional;the one in a billion;unbelievably talented;the greatest of all time ;sir;debosmit created me"
            speak(text)
        if "who are you?":
            speak("")
       
         

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
 
        elif 'open youtube' in query:
            #query = query.replace("open youtube", "")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query or 'open stack overflow' in query or 'open stack over flow' in query:
            webbrowser.open("stackoverflow.com")
            
        elif 'open coding' in query:
            webbrowser.open_new_tab("prepbytes.com/prepbytes-expert-coder"+'doc/')  
        
        elif 'open interview book' in query or 'open interview preparation book' in query:
            path="file:///C:/Users/Debosmit%20Neogi/Downloads/Cracking-the-Coding-Interview-6th-Edition-189-Programming-Questions-and-Solutions.pdf"
            os.startfile(path)
            
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            
        elif 'open slack' in query:
            try:
                slackPath="C:\\Users\\Debosmit Neogi\\AppData\\Local\\slack\\slack.exe"
                os.startfile(slackPath)
            except Exception as e:
                speak("sorry,cannot open salck")
                break
            
        elif 'open whatsapp' in query:
            try:
                webbrowser.open("web.whatsapp.com")
            except Exception as e:
                speak("sorry; cannot open whatsapp")
                break
     
        
        elif 'email to dad' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "dad_email"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry,I am not able to send this email")  
                break
                
        elif 'email to me' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "my_email"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send this email")
                break
                
        elif 'search' in query:            
            outputList = []
            query = takeCommand() 
            #speak('What should I search for ?')
            searchOnGoogle(query, outputList)
            speak('Should I open up the first link for you ?')
            query = command()
            if 'yes' in query or 'sure' in query:
                openLink(outputList)
            if 'no' in query:
                speak('Alright.')
        else:
            speak("sorry;try to come up with better question next time;peace out ")
            break
    
