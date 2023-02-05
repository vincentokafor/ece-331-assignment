import speech_recognition as sr
#start
r = sr.Recognizer()
print("Recognising your speech by Google...")

harvard = sr.AudioFile('vin.wav')
with harvard as source:
    audio = r.record(source)
    
    type(audio)
    
    r.recognize_google(audio)
    
    print("Ending Your Speech Recognition Now...")
       
    
    #Project by Vincent Okafor
    
