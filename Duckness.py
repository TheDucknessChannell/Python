from gtts import gTTS 
  
# import Os module to start the audio file
import os 
  
mytext = 'what do you want to convert'
  
# Language we want to use 
language = 'en'
  

myobj = gTTS(text=mytext, lang=language, slow=False)
  

myobj.save("nameoffile.mp3") 
  
# Play the converted file 
os.system("start nameoffile.mp3") 