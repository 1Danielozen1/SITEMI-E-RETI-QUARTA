import pygame
import random
from pygame import mixer
import numpy as np
import sys
import serial, time
import threading, queue
import time
"""
Author: Di Mantua Daniele
Game: Flappy Chad
"""

a = queue.Queue()
b = queue.Queue()

class Read_Microbit(threading.Thread):
    def __init__(self,port):
        threading.Thread.__init__(self)
        self._running = True
        self.port = port
      
    def terminate(self):
        self._running = False
        
    def run(self):
        #serial config
        port = self.port
        s = serial.Serial(port)
        s.baudrate = 115200
        while self._running:
            data = s.readline().decode()
            acc = [x for x in data[1:-3].split(", ")]
            #print(acc)
            a.put(acc[0])
            b.put(acc[1])
            time.sleep(0.01)

porta = input("Inserisci il nome della porta: ")
rm = Read_Microbit(porta)          
print("TASTIERA:\n-'W' fa saltare il personaggio\n-'Space bar' fa ricominciare il gioco una volta che si ha perso\n\nMICROBIT:\n-'pultante A' fa saltare il personaggio\n-'pulsante B' fa ricominciare il gioco una volta che si ha perso\n- Premere contemporaneamente i pulsalti fanno chiudere il gioco")

pygame.init()

#Carico le immagini
sfondo = pygame.image.load('immagini/sfondo.jpg')
personaggio = pygame.image.load('immagini/GigaChad.png')
pavimento = pygame.image.load('immagini/pavimento.png')
f = pygame.image.load('immagini/gameover.png')
titolo = pygame.image.load('immagini/titolo.png')
spunt_giu = pygame.image.load('immagini/spuntone.png')
spunt_su = pygame.transform.flip(spunt_giu,False,True)  

#Costanti
SCHERMO = pygame.display.set_mode((288,512)) #288,512
FPS = 60
VELOCITA = 2
FONT = pygame.font.SysFont('century', 30,bold=True)
SCRITTA = FONT.render("PUNTEGGIO:",1,(255,255,255))
SCRITTA_IN = FONT.render("PREMI",1,(0,0,0))
SCRITTA_IN2 = FONT.render("PER",1,(0,0,0))
SCRITTA_IN3 = FONT.render("INIZIARE",1,(0,0,0))
W = FONT.render("'w'",1,(255,0,0))
diff = 300

pygame.display.set_caption("FlappyChad")

class spunt_class:
    def __init__(self):
        self.x = diff
        self.y = random.randint(-75,150)
    def avanza_e_disegna(self):
        self.x -= VELOCITA
        SCHERMO.blit(spunt_giu,(self.x,self.y+235))
        SCHERMO.blit(spunt_su,(self.x,self.y-235))
    def controllo(self,personaggio,personaggiox,personaggioy): #controllo che il personaggio non si sia schiantato contro un ostacolo
        toll = 5 #serve per definire meglio i bordi del personaggio affinché non tocchi senza effetivamente aver toccato l'ostacolo
        personaggio_lato_dx = personaggiox+ personaggio.get_width()-toll  #mi calcolo tutte le dimensioni dei vari ostacoli e personaggi
        personaggio_lato_sx = personaggiox + toll
        spunt_lato_dx = self.x + spunt_giu.get_width()
        spunt_lato_sx = self.x
        personaggio_lato_su = personaggioy+toll
        personaggio_lato_giu = personaggioy + personaggio.get_height()-toll
        spunt_lato_su = self.y+85
        spunt_lato_giu = self.y+235
        if personaggio_lato_dx > spunt_lato_sx and personaggio_lato_sx < spunt_lato_dx:
            if personaggio_lato_su < spunt_lato_su or personaggio_lato_giu > spunt_lato_giu:
                F_to_pay_respect()
    def incrementa(self,personaggio,personaggiox): #controlla se il personaggio sta passando tra due tubi
        toll = 5  
        personaggio_lato_dx = personaggiox+ personaggio.get_width()-toll
        personaggio_lato_sx = personaggiox + toll
        spunt_lato_dx = self.x + spunt_giu.get_width()
        spunt_lato_sx = self.x
        if personaggio_lato_dx > spunt_lato_sx and personaggio_lato_sx < spunt_lato_dx:
            return True


def F_to_pay_respect():
    mixer.music.stop() #ferma la musica
    mixer.music.load('suoni\Dark_Souls.wav') #musica della morte
    mixer.music.set_volume(0.5)
    mixer.music.play(1)
    SCHERMO.blit(f, (0,0))
    visualizzaPt = FONT.render(str(punti),1,(255,255,255))
    SCHERMO.blit(visualizzaPt,(40,100))
    SCHERMO.blit(SCRITTA,(40,50))
    pygame.display.update()
    pygame.time.Clock().tick(FPS)
    ric = False
    while ric != True:

        try:
            acc2 = b.get(block=False)
            acc = a.get(block=False)
            if (acc2 == "True" and acc == "False"):
                inizializza_glob()
                mixer.music.stop()
                mixer.music.load('suoni\gigachad_8-bit.wav') #riparte la musica
                mixer.music.set_volume(0.3)
                mixer.music.play(0)
                ric = True
            elif(acc2 == "True" and acc == "True"):
                pygame.quit()
            a.task_done()
            b.task_done()
        except:
            pass

        for event in pygame.event.get():
            if(event.type == pygame.KEYDOWN
                and event.key == pygame.K_SPACE ):
                inizializza_glob()
                mixer.music.stop()
                mixer.music.load('suoni\gigachad_8-bit.wav') #riparte la musica
                mixer.music.set_volume(0.3)
                mixer.music.play(0)
                ric = True
            if event.type == pygame.QUIT:
                pygame.quit() 

def disegna_oggetti():
    SCHERMO.blit(sfondo, (0,0))
    for t in spunt:
        t.avanza_e_disegna()
    SCHERMO.blit(personaggio,(personaggiox,personaggioy))
    SCHERMO.blit(pavimento, (pavimentox, 400))
    visualizzaPt = FONT.render(str(punti),1,(255,255,255))
    SCHERMO.blit(visualizzaPt,(0,0))

def inizializza_glob():
    global personaggiox, personaggioy, personaggio_vely
    global pavimentox
    global spunt
    global punti
    global incrementa
    personaggiox,personaggioy = 60,150
    personaggio_vely = 0
    pavimentox = 0
    punti = 0
    spunt = []
    spunt.append(spunt_class())
    incrementa = False


#Inizializzo tutte le variabili globali
inizializza_glob()

ok = False
rm.start()  
"""MENU INIZIALE"""
while ok == False:
    SCHERMO.blit(sfondo, (0,0))
    SCHERMO.blit(SCRITTA_IN,(50,200))
    SCHERMO.blit(W,(190,200))
    SCHERMO.blit(SCRITTA_IN2,(100,250))
    SCHERMO.blit(SCRITTA_IN3,(50,300))
    SCHERMO.blit(titolo,(50,10))
    try:
        acc = a.get(block=False)
        acc2 = b.get(block=False)
        if (acc == "True" and acc2 == "False"):
            ok = True
        elif (acc2 == "True" and acc == "True"):  
            pygame.quit()
        a.task_done()
        b.task_done()
    except:
        pass

    for ev in pygame.event.get():
            if((ev.type == pygame.KEYDOWN
              and (ev.key == pygame.K_w or ev.key == pygame.K_SPACE))):
                    ok = True
            if ev.type == pygame.QUIT:
                pygame.quit()
                
    pygame.display.update()
    pygame.time.Clock().tick(FPS)

#Parte la musica appena inizia la prima partita
mixer.music.load('suoni\gigachad_8-bit.wav')
mixer.music.set_volume(0.3)
mixer.music.play(0)


"""CICLO MAIN"""
while True:
    #Avanza il pavmento verso il personaggio, mentre il personaggio cade
    pavimentox -= VELOCITA
    if pavimentox < -45: 
        pavimentox = 0
    personaggio_vely += 1
    personaggioy += personaggio_vely
    try:
        acc = a.get(block=False)
        acc2 = b.get(block=False)
        if (acc == "True" and acc2 == "False"):
            personaggio_vely = -9.3
        elif (acc2 == "True" and acc == "True"):  
            pygame.quit()
        a.task_done()
        b.task_done()
    except:
        pass
        #print("Coda vuota")
    #print(acc)

    #Comandi da tastiera
    for event in pygame.event.get():
        if(event.type == pygame.KEYDOWN
            and event.key == pygame.K_w):
            personaggio_vely = -10 #mi permette di far rimbalzare in alto il personaggio
        if event.type == pygame.QUIT:
            pygame.quit()


    #Gestione spunt
    if spunt[-1].x < 150: 
        spunt.append(spunt_class())

    #controlla se il presonaggio ha toccato il tubo
    for t in spunt:
        t.controllo(personaggio,personaggiox,personaggioy)
    
    #Questi if mi servono per incrementare il punteggio.
    if incrementa != True:
        for t in spunt:
            if t.incrementa(personaggio,personaggiox) == True:
                incrementa = True
                break
    if incrementa != False:
        incrementa = False
        for t in spunt:
            if t.incrementa(personaggio,personaggiox):
                incrementa=True
                break
            if incrementa == False:
                punti += 1

    #Controlla se il personaggio ho toccato il pavimento
    if personaggioy > 380 or personaggioy < 0:
        F_to_pay_respect()

    #Aggiornamento schermo
    disegna_oggetti()
    pygame.display.update()
    pygame.time.Clock().tick(FPS)