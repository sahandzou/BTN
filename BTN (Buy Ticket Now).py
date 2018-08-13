# -*- coding: utf-8 -*-
import requests
import time
import pygame
from bs4 import BeautifulSoup
music=0
musiccg=0
pygame.init()
while(1):

    try:

        r=requests.get('https://cinematicket.org/?p=ncinemadet&cid=556',timeout=10)

        pygame.mixer.music.stop()
        music=0

    except:
        print('NO CONNECTION')


        if music==0:
            pygame.mixer.music.load('/home/pi/Desktop/21.mp3')
            pygame.mixer.music.play()
            music=1
        #time.sleep(5)

    page=r.text
    soup=BeautifulSoup(page,'html.parser')
    movies=[]

    #print(soup.find_all("div",class_="showtime--items_step")[1].prettify())
    wow=soup.find_all("div",class_="showtime--items_step")
    #print(wow[0].find_all("div",class_="name").prettify())
        #print(soup.find("div",class_="name",).prettify())
    v=(str(wow[0]).find('هزارپا'))
    for cunt in range(len(wow)):
#       if cunt==len(wow)-1:
#               if v>0 :
#                   print(cunt)
#               break
        if v>0 :
            #print(cunt)
            v=(str(wow[cunt+1]).find('هزارپا'))
            break
        else:
            v=(str(wow[cunt+1]).find('هزارپا'))

    #print(str(wow[2]).find('هزارپا'))
    #print(cunt)
    #v1=(str(wow[cunt]).find('جمعه'))
    v1=(str(wow[cunt]).find('1397/05/09'))
    #v1=(str(wow[cunt]).find('پنجشنبه'))
    v2=(str(wow[cunt]).find('سه شنبه'))
    #v2=(str(wow[cunt]).find('سه شنبه'))
    #print(str(wow[cunt]))
    if((v1>0) or (v2>0)):
        print('YES HURRY UP :)')
        pygame.mixer.music.load('/home/pi/Desktop/22.mp3')
        pygame.mixer.music.play()
        time.sleep(120)

    else:
        print('NOT NOW :(')

    time.sleep(20)
