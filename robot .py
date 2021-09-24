#para abrir sites
import subprocess as s
#para reconhecimento de voz
import speech_recognition as sr
#para encerrar o programa
import sys
#para sintetizar voz
import pyttsx3

class Execucao:
    
    def __init__(self,frase1):
        self.frase1=frase1
     
    
    def executa(self):
        if self.frase1=="what's up":
            en=pyttsx3.init()
            en.setProperty('rate',110)
            en.say("opening the what's up Ian...")
            en.runAndWait()
            s.Popen(['xdg-open','https://web.whatsapp.com/'])
            
        elif self.frase1=="search":
            en=pyttsx3.init()
            en.setProperty('rate',110)
            en.say('opening the google Ian...')
            en.runAndWait()
            s.Popen(['xdg-open','https://www.google.com/'])
            
        elif self.frase1=="f. c.":
            en=pyttsx3.init()
            en.setProperty('rate',110)
            en.say('opening the facebook Ian...')
            en.runAndWait()
            s.Popen(['xdg-open','https://www.facebook.com/'])
            
        elif self.frase1=="movie":
            en=pyttsx3.init()
            en.setProperty('rate',110)
            en.say('opening the netflix Ian...')
            en.runAndWait()
            s.Popen(['xdg-open','https://www.netflix.com/browse'])
                      
            
        #parando a execucao do programa
        elif self.frase1=="stop":
            en=pyttsx3.init()
            en.setProperty('rate',110)
            en.say('exiting Ian...')
            en.runAndWait()
            quit()
            #sys.exit()
        
        else:
            print('entendi:'+frase1)
            print('e nao tenho comando para isto.\n')

#capturando a voz
rec=sr.Recognizer()
with sr.Microphone() as cont:
    print('pode falar Ian')
    #transformando o som em objeto
    frase=rec.listen(cont)
#pega o texto e joga na variavel
frase1=rec.recognize_sphinx(frase)

print(frase1+'\n')

#chamando a classe
tarefa=Execucao(frase1)
tarefa.executa()

