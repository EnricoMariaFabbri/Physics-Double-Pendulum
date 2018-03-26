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

x1 = [0,posizioneXprimoFilo]
y1 = [0,posizioneYprimoFilo]
x2 = [posizioneXprimoFilo,posizioneXsecondoFilo]
y2 = [posizioneYprimoFilo,posizioneYsecondoFilo]

assi = grafico.gca()
assi.set_xlim([-15,15])
assi.set_ylim([-15,15])

origine = grafico.Circle((0,0), 0.1, color='black')
grafico.gcf().gca().add_artist(origine)

palla = grafico.Circle((posizioneXprimoFilo, posizioneYprimoFilo), 0.2, color='r',fill=False)
grafico.gcf().gca().add_artist(palla)

palla1 = grafico.Circle((posizioneXprimoFilo, posizioneYprimoFilo), 0.1, color='r',fill=False)
grafico.gcf().gca().add_artist(palla1)

palla2 = grafico.Circle((posizioneXprimoFilo, posizioneYprimoFilo), 0.3, color='g',fill=False)
grafico.gcf().gca().add_artist(palla2)

palla3 = grafico.Circle((posizioneXprimoFilo, posizioneYprimoFilo), 0.4, color='blue',fill=False)
grafico.gcf().gca().add_artist(palla3)

palla4 = grafico.Circle((posizioneXsecondoFilo, posizioneYsecondoFilo), 0.2, color='r',fill=False)
grafico.gcf().gca().add_artist(palla4)

palla5 = grafico.Circle((posizioneXsecondoFilo, posizioneYsecondoFilo), 0.1, color='r',fill=False)
grafico.gcf().gca().add_artist(palla5)

palla6 = grafico.Circle((posizioneXsecondoFilo, posizioneYsecondoFilo), 0.3, color='g',fill=False)
grafico.gcf().gca().add_artist(palla6)

palla7 = grafico.Circle((posizioneXsecondoFilo, posizioneYsecondoFilo), 0.4, color='blue',fill=False)
grafico.gcf().gca().add_artist(palla7)
grafico.plot(x1,y1)
grafico.plot(x2,y2)
grafico.show()
print(math.cos(alfa))
print(math.sin(alfa))

