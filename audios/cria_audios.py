from gtts import gTTS

tts = gTTS('Olá, eu sou a Penny, há assistente virtual do Marcus', lang='pt-br')
tts.save('hello_marcus_v2.mp3')
