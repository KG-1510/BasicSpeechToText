import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak into mic: ")
    audio = r.listen(source)

try:
    print("You said: " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Didn't understand what you said!")
except sr.RequestError as e:
    print("Cannot obtain results; {0}".format(e))

# code by Kushagra Gupta