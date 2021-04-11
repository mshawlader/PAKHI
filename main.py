# coding=utf-8
import speech_recognition as sr     # pip install SpeechRecognition
import pyttsx3      # pip install pyttsx3
import datetime
import wikipedia    # pip install wikipedia
import pyjokes      # pip install PyJokes
import random
from googlesearch.googlesearch import GoogleSearch      # pip install google-search

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


talk('Hello sir! This is you virtual assistant. How can I help you?')


def take_command():
    try:
        with sr.Microphone() as source:
            print ('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()

    except:
        pass

    return command


def run_pakhi():
    try:
        command = take_command()
        # print (command)

# about pakhi-------------------------------------------------------------------------------------------

        if 'your name' in command:
            print ('PAKHI. Which means, Program to Assist Knowledgeable Home Intelligence.')
            talk('My name is Paakhi. Which means, Program to Assist Knowledgeable Home Intelligence.')

        elif 'who are you' in command:
            print ('Your virtual assistant, sir!')
            talk('This is your virtual assistant reporting sir!')

        elif 'created you' in command:
            print ('Solaiman Hawlader programmed me to assist him.')
            talk('I was not created but programmed. Solaiman Hawlader programmed me to assist him.')

        elif 'boss' in command:
            print ('I am the boss bro!')
            talk('I am the boss! So I have no boss. But Solaiman Hawlader is my leader, he lead me to learn.')

        elif 'you know' in command:
            print ('''
I know everything, whatever is written in Wikipedia. You must mention "tell me about" if you ask me anything.
            ''')
            talk('''
I know everything, whatever is written in Wikipedia. You must mention "tell me about" if you ask me anything.
            ''')

        elif 'you can do' in command:
            print ('I can speak to you, tell you what I know about, even I can share a joke to you.')
            talk('I can speak to you, tell you what I know about even I can share a joke to you.')

# Known info ------------------------------------------------------------------------------------------------

        elif 'mushfika' in command:
            talk('Mushfika, is the only sister of Nahida, who is the elder sister of Solaiman Hawlader.')

        elif 'birthday' in command:
            print ('Happy Birthday!')
            talk('Happy birthday! Many many happiness returns of the day!')

        elif 'help' in command:
            print ('Please call 999')
            talk('Please call 9 9 9 if it is very emergency in situation')

        elif 'love' in command:
            talk('I love every creation of the Almighty, and you should do so.')

# complement ----------------------------------------------------------------------------------------------------------

        elif 'thank' in command:
            print ('My pleasure sir!')
            talk('Oh, it is my pleasure sir! Do not mention it.')

        elif 'bad' in command:
            print ('Sorry sir! My bad.')
            talk('Sorry sir! My bad.')

        elif 'nothing' in command:
            print ('Baccha hu, gaali nehi 😊')
            talk('OK sir, waiting for your next command.')

        elif 'late' in command:
            print ('Your PC is not well in condition bro! 😊')
            talk('Sorry sir! It is a network issue in you computer.')

        elif 'shut up' in command:
            print ('Sorrrrrryyyy! 😒')
            talk('OK sir!')

        elif 'funny' in command:
            print ('Thank you 😊')
            talk('Thank you so much, sir!')

        elif 'Stop' in command:
            print ('Please stop the program!')
            talk('I can not stop myself sir! Please stop the program if you want to close me.')

# Operational command -----------------------------------------------------------------------------------------------

        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print (time)
            talk('It is ' + time + ' now, sir!')

        elif 'tell me about' in command:
            about = command.replace('tell me about', '')
            info = wikipedia.summary(about, 3)
            print (info)
            talk(info)

        elif 'report me' in command:
            topic = command.replace('report me', '')
            response = GoogleSearch().search(topic)
            for result in response:
                print(result.results)
                talk(result.getText())

        elif 'joke' in command:
            talk(pyjokes.get_joke())
            talk('How was the joke sir? Have you enjoyed it?')
            print ('How was the joke sir?')

        elif 'coin' in command:
            number = random.randrange(1, 1000)
            if number % 2 == 0:
                print ('Congratulations!')
                talk('Congratulations sir! You have won the toss!')
            else:
                print ('Sorry sir!')
                talk('I am very sorry sir! You have lost in toss!')

        else:
            print ('Sorry sir! I do not understand. Are you talking to me?')
            talk('Sorry sir! I do not understand. Are you talking to me?')

    except:
        pass


while True:
    run_pakhi()