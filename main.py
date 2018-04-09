import matplotlib.pyplot as grafico
import matplotlib.animation as animazioni
import math
import numpy as np


beta = float( input ('inserisci il primo angolo in gradi' ))
gamma = float( input ('inserisci il secondo angolo in gradi' ))
lunghezza = float( input ('inserisci la lunghezza del primo filo in cm' ))
lunghezza1 = float( input ('inserisci la lunghezza del secondo filo in cm' ))

alfa = math.radians(beta)
latoB = lunghezza * math.sin(alfa)
posizioneXprimoFilo = 0.0 + latoB
latoC = lunghezza * math.cos(alfa)
posizioneYprimoFilo = 0.0 - latoC

delta = math.radians(gamma)
latoD = lunghezza * math.sin(delta)
posizioneXsecondoFilo =  posizioneXprimoFilo + latoD
latoE = lunghezza * math.cos(delta)
posizioneYsecondoFilo = posizioneYprimoFilo - latoE

x1 = posizioneXprimoFilo
y1 = posizioneYprimoFilo
x2 = posizioneXsecondoFilo
y2 = posizioneYsecondoFilo

assi = grafico.gca()
assi.set_xlim([-15,15])
assi.set_ylim([-15,15])


origine = grafico.Circle((0,0), 0.1, color='black')
grafico.gcf().gca().add_artist(origine)

palla = grafico.Circle((posizioneXprimoFilo, posizioneYprimoFilo), 0.2, color='r',fill=False)
grafico.gcf().gca().add_artist(palla)

palla1 = grafico.Circle((posizioneXprimoFilo, posizioneYprimoFilo), 0.1, color='g',fill=False)
grafico.gcf().gca().add_artist(palla1)

palla2 = grafico.Circle((posizioneXprimoFilo, posizioneYprimoFilo), 0.3, color='blue',fill=False)
grafico.gcf().gca().add_artist(palla2)

palla4 = grafico.Circle((posizioneXsecondoFilo, posizioneYsecondoFilo), 0.2, color='r',fill=False)
grafico.gcf().gca().add_artist(palla4)

palla5 = grafico.Circle((posizioneXsecondoFilo, posizioneYsecondoFilo), 0.1, color='g',fill=False)
grafico.gcf().gca().add_artist(palla5)

palla6 = grafico.Circle((posizioneXsecondoFilo, posizioneYsecondoFilo), 0.3, color='blue',fill=False)
grafico.gcf().gca().add_artist(palla6)

figura1 = grafico.figure()

def updateLine1 (num, data, line):
    line.set_data(data[...,:num])

    return line,




plot = grafico.plot([0,x1,x1,x2],[0,y1,y1,y2])


line_ani = animazioni.FuncAnimation(figura1, updateLine1, 25, fargs=(data, plot),
                                   interval=50, blit=True)

grafico.show()
print(math.cos(alfa))
print(math.sin(alfa))



