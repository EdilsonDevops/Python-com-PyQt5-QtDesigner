import webbrowser
from playsound import playsound

# Abrindo audio
"""Necessário informar o caminho onde está o arquivo mp3 caso utilize playsound 
   para windows colocar o 'r' atrás das aspas duplas"""


def net():
    playsound(r"C:\\Users\\Edilson\\Desktop\\Python\\music\\net.mp3")


def pri():
    playsound(r"C:\\Users\\Edilson\\Desktop\\Python\\music\\pri.mp3")


def dis():
    playsound(r"C:\\Users\\Edilson\\Desktop\\Python\\music\\dis.mp3")


def you():
    playsound(r"C:\\Users\\Edilson\\Desktop\\Python\\music\\you.mp3")


def goo():
    playsound(r"C:\\Users\\Edilson\\Desktop\\Python\\music\\goo.mp3")


def twi():
    playsound(r"C:\\Users\\Edilson\\Desktop\\Python\\music\\twi.mp3")

# Abrindo a página da web


def google():
    webbrowser.open_new_tab("http://www.google.com/")


def youtube():
    webbrowser.open_new_tab("https://www.youtube.com/")


def twitch():
    webbrowser.open_new_tab("https://www.twitch.tv/")


def netflix():
    webbrowser.open_new_tab("https://www.netflix.com/br/")


def prime():
    webbrowser.open_new_tab("https://www.primevideo.com/offers/nonprimehomepage/ref=atv_nb_lcl_pt_BR")


def disney():
    webbrowser.open_new_tab("https://www.disneyplus.com/pt-br")
