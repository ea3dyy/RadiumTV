# -*- coding:utf-8 -*-
#########################################################
##IMPORTACIO DE LLIBRERIES
#########################################################
import Tkinter
from Tkinter import Canvas
from Tkinter import *
import RPi.GPIO as GPIO
from io import open
import sys
import subprocess
import unicodedata
import time
import datetime
from datetime import date
import webbrowser

#########################################################
###PROPIETATS DE LA FINESTRA
#########################################################
finestra=Tkinter.Tk()
finestra.title("Neo Vintage Radio")
finestra.geometry("1280x760")
finestra.configure(bg='#999900')
canvas=Canvas(finestra, width=1280, heigh=720, bg='#00FFFF')

#######################################################
##VARIABLES INICIALS I GLOBALS
#######################################################
# Variables de reproduccio
arxiu_text=open("broadcast.txt","r")

# Variables de les linies de text
variable_linies= arxiu_text.readlines()

xuta=subprocess.call("mpc current", shell=True) 
global n
n=1

# rectangle superior de internet radio
canvas.create_rectangle(10,0, 1012,60, fill="#933A00")

# separa botons
canvas.create_rectangle(10,210, 1014,230, fill="#933A00")

titol1 = Tkinter.Label(finestra, text="Internet Ràdio", font=("Arial Black",20), bg="#933A00", fg="white").place(x=410,y=10)
# rectangle de la dreta on van els controls
#canvas.create_rectangle(730,200, 1012,65, fill="#933A00")


# requadre blau displai
canvas.create_rectangle(730,200, 1012,65, fill="blue")


#################################################
##REQUADRE DE BAIX DRET MARRO
#################################################
canvas.create_rectangle(730,530, 1012,240, fill="#933A00")
####Requadre interior blau
canvas.create_rectangle(740,520, 870,250, fill="#00FFFF")

########################################################################
##data a la capsalera
########################################################################
today = datetime.date.today()
anyo = today.year
mes =today.month
dia = today.day
#avui = today.strftime("%d/%m/%y")
mostra_dia = Tkinter.Label(finestra, text=dia, font=("Arial Black",16), bg="#933A00", fg="white").place(x=800,y=15)
guionet = Tkinter.Label(finestra, text="-", font=("Arial Black",18), bg="#933A00", fg="white").place(x=837,y=15)
mostra_mes = Tkinter.Label(finestra, text=mes, font=("Arial Black",16), bg="#933A00", fg="white").place(x=858,y=15)
guionet2 = Tkinter.Label(finestra, text="-", font=("Arial Black",18), bg="#933A00", fg="white").place(x=878,y=15)
mostra_any = Tkinter.Label(finestra, text=anyo, font=("Arial Black",16), bg="#933A00", fg="white").place(x=892,y=15)
#####################################
# Funció del rellotge
#####################################
time1 =''
global clock
clock = Label(finestra, font=('Arial', 18), bg="blue", fg="white")
clock.pack()
clock.place (x=820, y=70)

def reloj ():
    global time1
    time2 = time.strftime ('%H:%M:%S')
    if time2 != time1:
        time1 = time2
        clock.configure (text=time2)
    clock.after(500,reloj)
reloj ()
#####################################################################
##BOTONS D EMISSORES MEMORITZADES DE 1 A 10
#####################################################################
# Funcions dels botons
# Funcio de la MEM1
def mem01():
    # Reinicia la variable que es reprodueix
    reprod =Tkinter.Label(finestra, text="                                          ",font=("Arial",15), bg="#933A00", fg="#933A00").place(x=735,y=105)
    # Nou valor de la variable
    global n
    n=1
    titol_play=variable_linies[1]
    reprod =Tkinter.Label(finestra, text=titol_play, font=("Arial",12), bg="red", fg="white").place(x=736,y=105)


####Executa play
    subprocess.call("mpc stop", shell=True) 
    subprocess.call("mpc play 1", shell=True)  



## Funcio de la MEM2 
def mem02():
    # Reinicia la variable que es reprodueix
    reprod =Tkinter.Label(finestra, text="                                          ",font=("Arial",15), bg="#933A00", fg="#933A00").place(x=735,y=105)
    # Nou valor de la variable
    global n
    n=2
    titol_play=variable_linies[n]
    reprod = Tkinter.Label(finestra, text=titol_play, font=("Arial",12),  bg="red", fg="white").place(x=735,y=105)

####Executa play
    subprocess.call("mpc stop", shell=True) 
    subprocess.call("mpc play 2", shell=True)  

# Funcio de la MEM3
def mem03():
    # Reinicia la variable que es reprodueix
    reprod =Tkinter.Label(finestra, text="                                          ",font=("Arial",15), bg="#933A00", fg="#933A00").place(x=735,y=105)
    global n 
    n=3
    titol_play=variable_linies[n]
    
    # Nou valor de la variable
    reprod =Tkinter.Label(finestra, text=titol_play, font=("Arial",12), bg="red", fg="white").place(x=735,y=105)

    subprocess.call("mpc stop", shell=True) 
    subprocess.call("mpc play 3", shell=True)  

# Funcio de la MEM4
def mem04():
   # Reinicia la variable que es reprodueix
    reprod =Tkinter.Label(finestra, text="                                          ",font=("Arial",15), bg="red", fg="white").place(x=735,y=105)
    # Nou valor de la variable
    global n
    n=4
    titol_play=variable_linies[n]
    reprod =Tkinter.Label(finestra, text=titol_play, font=("Arial",12), bg="red", fg="white").place(x=735,y=105) 

    subprocess.call("mpc stop", shell=True)
    subprocess.call("mpc play 4", shell=True) 
    
    
#Funcio de la MEM5
def mem05():
   # Reinicia la variable que es reprodueix
    reprod =Tkinter.Label(finestra, text="                                          ",font=("Arial",15), bg="red", fg="white").place(x=735,y=105)
    # Nou valor de la variable
    global n
    n=5
    titol_play=variable_linies[n]
    reprod =Tkinter.Label(finestra, text=titol_play, font=("Arial",12), bg="red", fg="white").place(x=735,y=105) 

    subprocess.call("mpc stop", shell=True)
    subprocess.call("mpc play 5", shell=True) 
   

# Funcio de la MEM6
def mem06():
   # Reinicia la variable que es reprodueix
    reprod =Tkinter.Label(finestra, text="                                          ",font=("Arial",15), bg="#933A00", fg="#933A00").place(x=735,y=105)
    # Nou valor de la variable
    global n
    n=6
    titol_play=variable_linies[n]
    reprod =Tkinter.Label(finestra, text=titol_play, font=("Arial",12), bg="red", fg="white").place(x=735,y=105)

    subprocess.call("mpc stop", shell=True) 
    subprocess.call("mpc play 6", shell=True)
  
# Funcio MEM7
def mem07():
   # Reinicia la variable que es reprodueix
    reprod =Tkinter.Label(finestra, text="                                          ",font=("Arial",15), bg="#933A00", fg="#933A00").place(x=735,y=105)
    # Nou valor de la variable
    global n
    n=7
    titol_play=variable_linies[n]
    reprod =Tkinter.Label(finestra, text=titol_play, font=("Arial",12), bg="red", fg="white").place(x=735,y=105)
    subprocess.call("mpc stop", shell=True) 
    subprocess.call("mpc play 7", shell=True)  

# Funcio de la MEM8
def mem08():
   # Reinicia la variable que es reprodueix
    reprod =Tkinter.Label(finestra, text="                                          ",font=("Arial",15), bg="#933A00", fg="#933A00").place(x=735,y=105)
    # Nou valor de la variable
    global n
    n=8
    titol_play=variable_linies[n]
    reprod =Tkinter.Label(finestra, text=titol_play, font=("Arial",12), bg="red", fg="white").place(x=735,y=105)
    subprocess.call("mpc stop", shell=True) 
    subprocess.call("mpc play 8", shell=True)  

# Funcio de la MEM9
def mem09():
   # Reinicia la variable que es reprodueix
    reprod =Tkinter.Label(finestra, text="                                          ",font=("Arial",15), bg="#933A00", fg="#933A00").place(x=735,y=105)
    # Nou valor de la variable
    global n
    n=9
    titol_play=variable_linies[n]
    reprod =Tkinter.Label(finestra, text=titol_play, font=("Arial",12), bg="red", fg="white").place(x=735,y=105)
    subprocess.call("mpc stop", shell=True) 
    subprocess.call("mpc play 9", shell=True)  


# Funcio de la MEM10
def mem10():
   # Reinicia la variable que es reprodueix
    reprod =Tkinter.Label(finestra, text="                                          ",font=("Arial",15), bg="#933A00", fg="#933A00").place(x=735,y=105)
    # Nou valor de la variable
    global n
    n=10
    titol_play=variable_linies[n]
    reprod =Tkinter.Label(finestra, text=titol_play, font=("Arial",12), bg="red", fg="white").place(x=735,y=105)
    subprocess.call("mpc stop", shell=True) 
    subprocess.call("mpc play 10", shell=True)

###############
# Funcions SDR
###############
def sdr():
    subprocess.call("mpc stop", shell=True)
    reprod =Tkinter.Label(finestra, text="                                          ",font=("Arial",15), bg="#933A00", fg="#933A00").place(x=735,y=105)
    reprod =Tkinter.Label(finestra, text="No disponible fins la versió 1.1",font=("Arial",15), bg="red", fg="white").place(x=735,y=105)

#################################################
# FUNCIONS DELS BOTONS DE CONTROL DE REPRODUCCIO
#################################################
# FUNCIO REBOBINA <<<<
def rebobina():
    global n
    n= n-1
    if n < 1:
       n=1
       titol_play=variable_linies[n]
       subprocess.call("mpc play 1", shell=True)
       titol_play=variable_linies[n]      
       reprod =Tkinter.Label(finestra, text="                                               ",font=("Arial",15), bg="#933A00", fg="#933A00").place(x=735,y=105)
       reprod =Tkinter.Label(finestra, text=titol_play, font=("Arial",12), bg="red", fg="white").place(x=735,y=105)
    
    # en cas que no sigui inferioe a 1
    titol_play=variable_linies[n]
    reprod =Tkinter.Label(finestra, text="                                          ",font=("Arial",15), bg="#933A00", fg="#933A00").place(x=735,y=105)
    reprod =Tkinter.Label(finestra, text=titol_play, font=("Arial",12), bg="red", fg="white").place(x=735,y=105)

    # executa mpc
    subprocess.call("mpc prev", shell=True)
    
####FUNCIO PLAY
def play():
    subprocess.call("mpc play", shell=True)

    
    #reprod =Tkinter.Label(finestra, text="titol_play", font=("Arial",15), bg="#red", fg="white").place(x=735,y=105)

####FUNCIO FAST FORWARD >>>>
def endavant():
    global n
    n= n+1
    titol_play=variable_linies[n]
    reprod =Tkinter.Label(finestra, text="                                          ",font=("Arial",15), bg="#933A00", fg="#933A00").place(x=735,y=105)
    # Nou valor de la variable
    reprod =Tkinter.Label(finestra, text=titol_play, font=("Arial",12), bg="red", fg="white").place(x=735,y=105)
    # executa mpc
    subprocess.call("mpc next", shell=True)
    
# Funcio parar
def parar():
    subprocess.call("mpc pause", shell=True)

########################################
# FUNCIONS EMISSORES ESTRANGERES
########################################
##ARGENTINA
def argentina():
    global n
    n=11
    titol_play=variable_linies[n]
   # Reinicia la variable que es reprodueix
    reprod =Tkinter.Label(finestra, text="                                          ",font=("Arial",15), bg="#933A00", fg="#933A00").place(x=735,y=105)
    # Nou valor de la variable
    
    reprod =Tkinter.Label(finestra, text=titol_play, font=("Arial",12), bg="red", fg="white").place(x=735,y=105)

    subprocess.call("mpc stop", shell=True) 
    subprocess.call("mpc play 11", shell=True)

##COLOMBIA
def colombia():
    global n
    n=58
    titol_play=variable_linies[n]
   # Reinicia la variable que es reprodueix
    reprod =Tkinter.Label(finestra, text="                                          ",font=("Arial",15), bg="#933A00", fg="#933A00").place(x=735,y=105)
    # Nou valor de la variable
    
    reprod =Tkinter.Label(finestra, text=titol_play, font=("Arial",12), bg="red", fg="white").place(x=735,y=105)

    subprocess.call("mpc stop", shell=True) 
    subprocess.call("mpc play 58", shell=True)

#BOLIVIA
def bolivia():
    global n
    n=106
    titol_play=variable_linies[n]
   # Reinicia la variable que es reprodueix
    reprod =Tkinter.Label(finestra, text="                                          ",font=("Arial",15), bg="#933A00", fg="#933A00").place(x=735,y=105)
    # Nou valor de la variable
    
    reprod =Tkinter.Label(finestra, text=titol_play, font=("Arial",12), bg="red", fg="white").place(x=735,y=105)

    subprocess.call("mpc stop", shell=True) 
    subprocess.call("mpc play 58", shell=True)
#Honduras
def honduras():
    global n
    n=160
    titol_play=variable_linies[n]
   # Reinicia la variable que es reprodueix
    reprod =Tkinter.Label(finestra, text="                                          ",font=("Arial",15), bg="#933A00", fg="#933A00").place(x=735,y=105)
    # Nou valor de la variable
    
    reprod =Tkinter.Label(finestra, text=titol_play, font=("Arial",12), bg="red", fg="white").place(x=735,y=105)

    subprocess.call("mpc stop", shell=True) 
    subprocess.call("mpc play 58", shell=True)

#Chile
def chile():
    global n
    n=239
    titol_play=variable_linies[n]
   # Reinicia la variable que es reprodueix
    reprod =Tkinter.Label(finestra, text="                                          ",font=("Arial",15), bg="#933A00", fg="#933A00").place(x=735,y=105)
    # Nou valor de la variable
    
    reprod =Tkinter.Label(finestra, text=titol_play, font=("Arial",12), bg="red", fg="white").place(x=735,y=105)

    subprocess.call("mpc stop", shell=True) 
    subprocess.call("mpc play 58", shell=True)

####################
####################
##Engega la TV
####################
####################
def obretv():
    #########################################################
    ###PROPIETATS DE LA FINESTRA INTERNET TV
    #########################################################
    subprocess.call("mpc stop", shell=True)
    finestratv=Tkinter.Tk()
    finestratv.title("Internet TV")
    finestratv.geometry("1280x760")
    finestratv.configure(bg='#00FF00')
    canvas=Canvas(finestratv, width=1280, heigh=720, bg='#00FFFF')

    # rectangle superior de internet TV
    canvas.create_rectangle(10,0, 1012,60, fill="#933A00")

    # Titol dins del requadre
    titol1 = Tkinter.Label(finestratv, text="TV Internet", font=("Arial Black",20), bg="#933A00", fg="white").place(x=410,y=10)

 
    ########################################################################
    ##data a la capsalera tv
    ########################################################################
    today = datetime.date.today()
    anyo = today.year
    mes =today.month
    dia = today.day
    
    mostra_dia = Tkinter.Label(finestratv, text=dia, font=("Arial Black",10), bg="#933A00", fg="white").place(x=438,y=38)

    guionet = Tkinter.Label(finestratv, text="-", font=("Arial Black",10), bg="#933A00",      fg="white").place(x=452,y=38)

    mostra_mes = Tkinter.Label(finestratv, text=mes, font=("Arial Black",10), bg="#933A00", fg="white").place(x=464,y=38)

    guionet2 = Tkinter.Label(finestratv, text="-", font=("Arial Black",10), bg="#933A00", fg="white").place(x=482,y=38)

    mostra_any = Tkinter.Label(finestratv, text=anyo, font=("Arial Black",10), bg="#933A00", fg="white").place(x=495,y=38)

    #####################################
    # Funció del rellotge TV
    #####################################
    time1 =''
    clock = Label(finestratv, font=('Arial', 18), bg="blue", fg="white")
    clock.pack()
    clock.place (x=820, y=80)   

    def reloj ():
        global time1
        time2 = time.strftime ('%H:%M:%S')
        if time2 != time1:
             time1 = time2
             clock.configure (text=time2)
        clock.after(500,reloj)
    reloj ()

    #######################################################
    # FUNCIONS DELS CANALS PREFERENTS
    # #####################################################
    def mem01():
        tv1='https://www.rtve.es/play/videos/directo/la-1/'
        webbrowser.open(tv1,0,False)

    ## Funcio de la MEM2 
    def mem02():
        tv2='https://www.rtve.es/play/videos/directo/la-2/'
        webbrowser.open(tv2)

    ## Funcio de la MEM3
    def mem03():
        tv3='https://www.ccma.cat/tv3/directe/tv3/'
        webbrowser.open(tv3)

    def mem04():
        cat324='https://www.ccma.cat/tv3/directe/324/'
        webbrowser.open(cat324)


    # Funcio de la MEM6

    def mem06():
        antena3tv='https://www.atresplayer.com/directos/antena3/'
        webbrowser.open(antena3tv)

    # Funcio MEM7
    def mem07():
        cuatro='https://www.cuatro.com/en-directo/'
        webbrowser.open(cuatro)

    # Funcio de la MEM8
    def mem08():
        telecinco='https://www.telecinco.es/endirecto/'
        webbrowser.open(telecinco)

    # Funcio de la MEM9
    def mem09():
        lasexta='https://www.atresplayer.com/directos/lasexta/'
        webbrowser.open(lasexta)

    # Funcio de la MEM10
    def mem10():
        neox='https://www.atresplayer.com/directos/neox/'
        webbrowser.open(neox)

    # Funcio de la MEM11
    def mem11():
        neox='https://www.atresplayer.com/directos/nova/'
        webbrowser.open(neox)

     # Funcio de la MEM12
    def mem12():
        c24h='https://www.rtve.es/play/videos/directo/24h/'
        webbrowser.open(c24h)

     # Funcio de la MEM13
    def mem13():
        a3series='https://www.atresplayer.com/directos/atreseries/'
        webbrowser.open(a3series)

    # Funcio de la MEM14
    def mem14():
        diviniti='https://www.mitele.es/directo/divinity/'
        webbrowser.open(diviniti)

    # Funcio de la MEM15
    def mem15():
        energy='https://www.mitele.es/directo/energy/'
        webbrowser.open(energy)

    # Funcio de la MEM16
    def mem16():
        bemad='https://www.mitele.es/directo/bemad/'
        webbrowser.open(bemad)

    # Funcio de la MEM16
    def mem17():
        mega='https://www.atresplayer.com/directos/mega/'
        webbrowser.open(mega)

    # Funcio de la MEM17
    def mem18():
        mtmad24h='https://www.mitele.es/directo/mtmad-24h/'
        webbrowser.open(mtmad24h)

    def mem19():
        cnn='https://cnnespanol.cnn.com/'
        webbrowser.open(cnn)

    def mem20():
        rt='https://actualidad.rt.com/en_vivo'
        webbrowser.open(rt)

    def mem21():
        aljazeera='https://www.aljazeera.com/live'
        webbrowser.open(aljazeera)

    def mem22():
        rpt='https://www.rtp.pt/play/direto/rtpinternacional'
        webbrowser.open(rpt)

    def mem23():
        nasa='https://www.nasa.gov/crew-2'
        webbrowser.open(nasa)

    def mem24():
        btv='https://beteve.cat/en-directe/'
        webbrowser.open(btv)

    def mem25():
        vuittv='https://www.8tv.cat/en-directe.html'
        webbrowser.open(vuittv)

    def mem26():
        torotv='https://eltorotv.com/tv-en-directo'
        webbrowser.open(torotv)

    def mem27():
        skynews='https://news.sky.com/watch-live'
        webbrowser.open(skynews)

    def mem28():
        bloomberg='https://www.bloomberg.com/live/europe'
        webbrowser.open(bloomberg)

    def mem29():
        bbc='https://www.bbc.com/news/av/10462520'
        webbrowser.open(bbc)

    def mem30():
        france24='https://www.france24.com/fr/direct'
        webbrowser.open(france24)

    def mem31():
        euronews='https://es.euronews.com/live'
        webbrowser.open(euronews)

    def mem32():
        tnargentina24='https://tn.com.ar/envivo/24hs/'
        webbrowser.open(tnargentina24)

    def mem33():
        nhkjapan='https://www3.nhk.or.jp/nhkworld/en/live/'
        webbrowser.open(nhkjapan)

    def mem34():
        chile='https://www.tvn.cl/envivo/'
        webbrowser.open(chile)

    def mem35():
        mexico='https://directostv.teleame.com/mexicotravelchannelenvivo/'
        webbrowser.open(mexico)

    def mem36():
        mcolombia='http://www.mundomas.tv/senal-en-vivo/'
        webbrowser.open(mcolombia)

    def mem37():
        tanzania='https://directostv.teleame.com/hopechanneltanzanialive/'
        webbrowser.open(tanzania)

    def mem38():
        australia='https://directostv.teleame.com/3abninternacionalendirecto/'
        webbrowser.open(australia)

    def mem39():
        tres_abn='https://directostv.teleame.com/3abninternacionalendirecto/'
        webbrowser.open(tres_abn)

    def mem40():
        viajar='https://viajartv.tv/live/'
        webbrowser.open(viajar)
    #########
    # Boto de tancar
    #########
    tancar=Tkinter.Button(finestratv, text="Tancar", font=("Verdana",12), width=5, height=1, bg="red", fg="#FFFFFF", command = finestratv.destroy).place(x=900,y=12)

     #####################################################################
    ##BOTONS D EMISSORES MEMORITZADES DE 1 A 10
    #####################################################################

    memoria1=Tkinter.Button(finestratv, text="TVE la 1", font=("Verdana",15), width=8, height=2,     bg="#999900", fg="#FFFFFF", command = mem01).place(x=10,y=65)


    memoria2=Tkinter.Button(finestratv, text="TVE la 2", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem02).place(x=156,y=65)

    memoria3=Tkinter.Button(finestratv, text="TV3-Cat", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem03).place(x=302,y=65)

    memoria4=Tkinter.Button(finestratv, text="Canal 3/24", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem04).place(x=445,y=65)

    memoria5=Tkinter.Button(finestratv, text="Canal 33", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem04).place(x=590,y=65)

    memoria6=Tkinter.Button(finestratv, text="Antena3 TV", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem06).place(x=10,y=140)

    memoria7=Tkinter.Button(finestratv, text="Cuatro", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem07).place(x=156,y=140)

    memoria8=Tkinter.Button(finestratv, text="Telecinco", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem08).place(x=302,y=140)

    memoria9=Tkinter.Button(finestratv, text="La Sexta", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem09).place(x=445,y=140)

    memoria10=Tkinter.Button(finestratv, text="Neox", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem10).place(x=590,y=140)

    memoria11=Tkinter.Button(finestratv, text="Nova", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem11).place(x=735,y=140)

    memoria12=Tkinter.Button(finestratv, text="Canal 24h", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem12).place(x=880,y=140)

    memoria13=Tkinter.Button(finestratv, text="A 3 Series", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem13).place(x=10,y=215)

    memoria14=Tkinter.Button(finestratv, text="Divinity", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem14).place(x=156,y=215)

    memoria15=Tkinter.Button(finestratv, text="Energy", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem15).place(x=302,y=215)

    memoria16=Tkinter.Button(finestratv, text="Be Mad", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem16).place(x=445,y=215)

    memoria17=Tkinter.Button(finestratv, text="Mega", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem17).place(x=590,y=215)

    memoria18=Tkinter.Button(finestratv, text="Mt Mad", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem18).place(x=735,y=215)

    memoria19=Tkinter.Button(finestratv, text="BTV", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem24).place(x=880,y=215)

    memoria20=Tkinter.Button(finestratv, text="8 TV", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem25).place(x=10,y=290)

    memoria21=Tkinter.Button(finestratv, text="Al Jazeera", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem21).place(x=156,y=290)

    memoria22=Tkinter.Button(finestratv, text="RPT", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem22).place(x=302,y=290)

    memoria23=Tkinter.Button(finestratv, text="NASA", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem23).place(x=445,y=290)

    memoria24=Tkinter.Button(finestratv, text="CNN", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem19).place(x=590,y=290)

    memoria25=Tkinter.Button(finestratv, text="Rusia RT", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem20).place(x=735,y=290)

    memoria26=Tkinter.Button(finestratv, text="El Toro TV", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem26).place(x=880,y=290)

    memoria27=Tkinter.Button(finestratv, text="Sky News", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem27).place(x=10,y=365)

    memoria28=Tkinter.Button(finestratv, text="Bloomberg", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem28).place(x=156,y=365)

    memoria29=Tkinter.Button(finestratv, text="BBC", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem29).place(x=302,y=365)

    memoria30=Tkinter.Button(finestratv, text="France 24h", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem30).place(x=445,y=365)

    memoria31=Tkinter.Button(finestratv, text="Euronews", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem31).place(x=590,y=365)

    memoria32=Tkinter.Button(finestratv, text="TNArgentina", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem32).place(x=735,y=365)

    memoria33=Tkinter.Button(finestratv, text="NHK W Japan", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem33).place(x=880,y=365)


    memoria34=Tkinter.Button(finestratv, text="Chile", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem34).place(x=10,y=440)

    memoria35=Tkinter.Button(finestratv, text="México", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem35).place(x=156,y=440)

    memoria36=Tkinter.Button(finestratv, text="Colombia", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem36).place(x=302,y=440)

    memoria37=Tkinter.Button(finestratv, text="Tanzania", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem37).place(x=445,y=440)

    memoria38=Tkinter.Button(finestratv, text="Australia", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem38).place(x=590,y=440)

    memoria39=Tkinter.Button(finestratv, text="3ABN Intern", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem39).place(x=735,y=440)

    memoria40=Tkinter.Button(finestratv, text="Viajar", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem40).place(x=880,y=440)


    ######################################
    ##TANCAMENT DEL PROGRAMA
    ######################################
    canvas.pack()
    # sha acabat la importacio del  canvas 

    finestratv.mainloop()


#######################################
##Música i Podcasts
#######################################

# Aqui fiquem les funcions de música i podcasts

######################################


#####################################################
##BOTONS DE LES MEMORITZADES DE 1 A 10
#####################################################
# Botons dels menu

memoria1=Tkinter.Button(finestra, text="Mem 1", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem01).place(x=10,y=65)

memoria2=Tkinter.Button(finestra, text="Mem 2", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem02).place(x=156,y=65)

memoria3=Tkinter.Button(finestra, text="Mem 3", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem03).place(x=302,y=65)

memoria4=Tkinter.Button(finestra, text="Mem 4", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem04).place(x=445,y=65)

memoria5=Tkinter.Button(finestra, text="Mem 5", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem05).place(x=590,y=65)

memoria6=Tkinter.Button(finestra, text="Mem 6", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem06).place(x=10,y=140)

memoria7=Tkinter.Button(finestra, text="Mem 7", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem07).place(x=156,y=140)

memoria8=Tkinter.Button(finestra, text="Mem 8", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem08).place(x=302,y=140)

memoria9=Tkinter.Button(finestra, text="Mem 9", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem09).place(x=445,y=140)

memoria10=Tkinter.Button(finestra, text="Mem 10", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem10).place(x=590,y=140)

#######################################
###Botons de musica i podcasts
#######################################
mus1=Tkinter.Button(finestra, text="Música 1", font=("Verdana",14), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem10).place(x=744,y=255)

mus2=Tkinter.Button(finestra, text="Música 2", font=("Verdana",14), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem10).place(x=744,y=321)

podcast1=Tkinter.Button(finestra, text="Podcast 1", font=("Verdana",14), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem10).place(x=744,y=388)

podcast2=Tkinter.Button(finestra, text="Podcast 2", font=("Verdana",14), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem10).place(x=744,y=455)

#######################################
#Botons Extres
#######################################
## Tv SDR
tele=Tkinter.Button(finestra, text="TV", font=("Verdana",14), width=8, height=2, bg="blue", fg="#FFFFFF", command = obretv).place(x=880,y=255)
## sdr radio
sdr=Tkinter.Button(finestra, text="Ràdio SDR", font=("Verdana",14), width=8, height=2, bg="blue", fg="#FFFFFF", command = sdr).place(x=880,y=321)

## Air
airband=Tkinter.Button(finestra, text="Air", font=("Verdana",14), width=8, height=2, bg="blue", fg="#FFFFFF", command = sdr).place(x=880,y=455)

## HAM
ham=Tkinter.Button(finestra, text="HAM", font=("Verdana",14), width=8, height=2, bg="blue", fg="#FFFFFF", command = sdr).place(x=880,y=389)


#######################################
##BOTONS DELS CONTROLS
#######################################
# Botons de control
# Boto RW
enrere=Tkinter.Button(finestra, text="<<<", font=("Verdana",15), width=2, height=1, bg="#999900", fg="#FFFFFF", command = rebobina).place(x=740,y=155)

# Boto Play
reprodueix=Tkinter.Button(finestra, text=">", font=("Verdana",15), width=2, height=1, bg="#999900", fg="#FFFFFF", command = play).place(x=811,y=155)

# Boto FF
palante=Tkinter.Button(finestra, text=">>>", font=("Verdana",15), width=2, height=1, bg="#999900", fg="#FFFFFF", command = endavant).place(x=951,y=155)

#Boto STOP
para=Tkinter.Button(finestra, text="Stop", font=("Verdana",14), width=2, height=1, bg="#999900", fg="#FFFFFF", command = parar).place(x=881,y=155)
#######################################################
#BOTONS EMISSORES ESTRANGERES
#######################################################
argentina=Tkinter.Button(finestra, text="Argentina", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = argentina).place(x=10,y=240)

ext2=Tkinter.Button(finestra, text="Belice", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem08).place(x=156,y=240)

bolivia=Tkinter.Button(finestra, text="Bolivia", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = bolivia).place(x=302,y=240)

ext4=Tkinter.Button(finestra, text="Brasil", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem10).place(x=445,y=240)

chile=Tkinter.Button(finestra, text="Chile", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = chile).place(x=590,y=240)

colombia=Tkinter.Button(finestra, text="Colòmbia", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = colombia).place(x=10,y=315)

ext7=Tkinter.Button(finestra, text="Costa Rica", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem08).place(x=156,y=315)

ext8=Tkinter.Button(finestra, text="Ecuador", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem09).place(x=302,y=315)

ext9=Tkinter.Button(finestra, text="Guatemala", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem10).place(x=445,y=315)

ext10=Tkinter.Button(finestra, text="Guyana", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem10).place(x=590,y=315)

ext11=Tkinter.Button(finestra, text="Honduras", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = honduras).place(x=10,y=390)

ext12=Tkinter.Button(finestra, text="Costa Rica", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem08).place(x=156,y=390)

ext13=Tkinter.Button(finestra, text="Mèxic", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem09).place(x=302,y=390)

ext14=Tkinter.Button(finestra, text="Nicaragua", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem10).place(x=445,y=390)

ext15=Tkinter.Button(finestra, text="El Salvador", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem10).place(x=590,y=390)

ext16=Tkinter.Button(finestra, text="Panamà", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem10).place(x=10,y=460)

ext17=Tkinter.Button(finestra, text="Paraguai", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem08).place(x=156,y=460)

ext18=Tkinter.Button(finestra, text="Perú", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem09).place(x=302,y=460)

ext19=Tkinter.Button(finestra, text="Uruguai", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem10).place(x=445,y=460)

ext20=Tkinter.Button(finestra, text="Venessuela", font=("Verdana",15), width=8, height=2, bg="#999900", fg="#FFFFFF", command = mem10).place(x=590,y=460)




######################################
##TANCAMENT DEL PROGRAMA
######################################
canvas.pack()
# sha acabat la importacio del  canvas 
arxiu_text.close()
finestra.mainloop()

