from plyer import notification
#import pyttsx3
import winsound

def beep():
    frequency = 2500  # Set Frequency To 2500 Hertz
    duration = 100  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)

'''def voice_notify(Message):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    en_voice_id = "com.apple.speech.synthesis.voice.Alex"
    #en_voice_id = "com.apple.speech.synthesis.voice.damayanti"
    engine.setProperty('voice', en_voice_id)
    engine.say(Message)
    engine.runAndWait()'''

def text_notify(Message):
    notification.notify(
    title = "Notification Alert!!!!!",
    message  = Message,
    app_icon = 'tomato.ico', #image that appears next to tite and message
    timeout = 10)
    
 
