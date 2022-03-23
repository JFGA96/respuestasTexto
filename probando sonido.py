import pyttsx3
from pyttsx3 import engine

engine=pyttsx3.init()

voice_id = 'spanish-latin-am'
engine.setProperty('voice',voice_id)

rate = engine.getProperty('rate')

engine.setProperty('rate',rate-50)

engine.say('hola')
engine.runAndWait