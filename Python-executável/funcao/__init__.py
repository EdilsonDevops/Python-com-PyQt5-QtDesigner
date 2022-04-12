import webbrowser
import winsound


# Abrindo mp3
def net():
    winsound.PlaySound("music/net.wav", winsound.SND_FILENAME)


def dis():
    winsound.PlaySound("music/dis.wav", winsound.SND_FILENAME)


def pri():
    winsound.PlaySound("music/pri.wav", winsound.SND_FILENAME)


def goo():
    winsound.PlaySound("music/goo.wav", winsound.SND_FILENAME)


def twi():
    winsound.PlaySound("music/twi.wav", winsound.SND_FILENAME)


def you():
    winsound.PlaySound("music/you.wav", winsound.SND_FILENAME)


def inicio():
    winsound.PlaySound("music/inicio.wav", winsound.SND_FILENAME)


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
