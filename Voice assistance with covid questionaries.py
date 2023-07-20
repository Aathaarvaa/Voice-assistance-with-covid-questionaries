import pyttsx3
import datetime
import pyaudio
import speech_recognition as sr
import wikipedia
import pywhatkit as kit

machine = pyttsx3.init('sapi5')
voices = machine.getProperty('voices')
# print(voices[1].id)
machine.setProperty('voice', voices[1].id)


def speak(audio):          # defining the function speak
    machine.say(audio)
    machine.runAndWait()


def wishMe():              # defining the function wishme
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Su Prabhat...Namaskaar!")
    elif hour >= 12 and hour < 18:
        speak("Radhe Radhe.!")
    else:
        speak("Raam Raam ...Shubh Ratri!")

    speak("Hello ! I am your assistant ,Stella... How may I help you")


def takeCommand():      # to convert speech to text # defining function takeCommand
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio,language="en-in") #USING LANGUAGE "ENGLISH-INDIA"
        print (f"User said :{query}\n")

    except Exception as e:
        #print (e)

        print ("Say that again please.....")

    return query


if __name__ == '__main__':  # starting the main loop
    i = 1
    while (i < 4):
        speak("Please tell the password to unlock the system...")  #calling of speak function
        password = takeCommand().lower()                           # calling the takeCommand function and converting text to lower case
        if password == "nothing":                                  #checking the password
            speak("Welcome...")
            wishMe()                                               #calling the wishMe function
            while True:                                            #running infinite while loop
                query = takeCommand().lower()

                if "wikipedia" in query:                           # command given " ***** WIKIPEDIA "
                    speak ("Searching Wikipedia....")
                    query = query.replace ("wikipedia"," ")
                    results = wikipedia.summary(query,sentences = 2)
                    speak(" According to Wikipedia")
                    print(results)
                    speak (results)

                elif  " youtube" in query:                         # command given "***** YOUTUBE"
                    speak("Opening youtube....")
                    query = query.replace("youtube"," ")
                    kit.playonyt(query)


                elif "google" in query:                            # command given "***** GOOGLE"
                    speak("Opening google....")
                    query = query.replace("google"," ")
                    kit.search(query)


                elif " the time" in query:                         # command should contain "THE TIME " in it
                    Time = datetime.datetime.now().strftime("%H:%M:%S")
                    print("Current time(IST)",Time)
                    speak("The current time according to IST is")
                    speak(Time)

                elif  "convert text" in query:                     # command should contain "CONVERT TEXT" in it
                    speak("What should I convert....")
                    content = takeCommand()
                    kit.text_to_handwriting(content,rgb = (128,0,128), save_to = "new.png")

                elif  "shutdown" in query:                         # command should contain the word "SHUTDOWN"
                    speak("Shutting your device in 150 seconds...")
                    kit.shutdown(time=150)

                elif  "cancel" in query:                           #command should be having "CANCEL"
                    speak("Cancelling the command for shutting down")
                    kit.cancel_shutdown()

                elif  "corona" in query:                            #"CORONA" IS IMPORTANT
                    q = 0
                    speak("Play this quiz to know if yo show any symptoms...")
                    speak("Have you came in contact with any positive patient ")
                    ans = takeCommand().lower()
                    if ans == "yes":
                        q = q + 1
                    speak("Do you have fever or chills")
                    ans = takeCommand().lower()
                    if ans == "yes":
                        q = q + 1
                    speak("Do you cough or shortness of breath...")
                    ans = takeCommand().lower()
                    if ans == "yes":
                        q = q + 1
                    speak("Do you have body aches or head aches")
                    ans = takeCommand().lower()
                    if ans == "yes":
                        q = q + 1
                    speak("Do you have new loss of taste or smell")
                    ans = takeCommand().lower()
                    if ans == "yes":
                        q = q + 1
                    speak("Do you have sour throat..")
                    ans = takeCommand().lower()
                    if ans == "yes":
                        q = q + 1
                    if q > 2:
                        speak("You are showing some of the symptoms...It is advised to go for a checkup..")
                    else:
                        speak("Congratulations...You are not showing all the possible symptoms of corona...")

                elif "yourself" in query:                                                   #" DESCRIBE YOURSELF"
                    speak("Hello .....I am your customised voice assistant,Stella .....A handy and ready to help whenever you need me... A true friend more like a book to you. ")


                elif "how" in query:                                                        #"HOW ARE YOU"
                    speak("I am fine ....Hope you are in pink of your health too..")

                elif "me" in query:                                                         #"DESCRIBE ME"
                    speak("You are one of the most interesting and lovely person I have met till date...")

                elif "created" in query:                                                    #"WHO CREATED YOU"
                    speak("Wellll......Its a secret....")

                elif "smart" in query:                                                      #"ARE YOU SMART"
                    speak("I am the best  voice assistant....")

                elif "exit" in query:                                                       #"EXIT THE CODE"
                    speak("Sure ....Your program is being terminated...")
                    quit()


        else:                                            #RUNNING THE ELSE PART IF PASSWORD IS WRONG
            c = 3-i
            speak("Wrong password...Remember you only have three turns")
            speak(c)
            speak("Turns left..")
            i = i + 1
    speak("You have exhausted your attempts...The system is locked now....Please visit the head office..")



