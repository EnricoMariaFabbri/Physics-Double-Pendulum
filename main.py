import matplotlib.pyplot as grafico
import matplotlib.animation as animazioni
import math
import numpy as np


alfa = float( input ('inserisci il primo angolo in gradi' ))
beta = float( input ('inserisci il secondo angolo in gradi' ))
lunghezza1 = float( input ('inserisci la lunghezza del primo filo in cm' ))
lunghezza2 = float( input ('inserisci la lunghezza del secondo filo in cm' ))
massa1 = float( input ('inserisci la massa del primo filo in kg' ))
massa2 = float( input ('inserisci la massa del secondo filo in kg' ))
omega1= float (input('inserisci la prima velocità angolare'))
omega2= float (input('inserisci la seconda velocità angolare'))



latoB = lunghezza1 * math.sin(alfa)
posizioneXprimoFilo = 0.0 + latoB
latoC = lunghezza1 * np.cos(alfa)
posizioneYprimoFilo = 0.0 - latoC


latoD = lunghezza1 * math.sin(beta)
posizioneXsecondoFilo =  posizioneXprimoFilo + latoD
latoE = lunghezza1 * math.cos(beta)
posizioneYsecondoFilo = posizioneYprimoFilo - latoE

x1 = posizioneXprimoFilo
y1 = posizioneYprimoFilo
x2 = posizioneXsecondoFilo
y2 = posizioneYsecondoFilo
G = 9.18


def derivs(state, tempo):

    dydx = np.zeros_like(state)
    dydx[0] = state[1]

    del_ = state[2] - state[0]
    den1 = (massa1 + massa2)*lunghezza1 - massa2*lunghezza1*np.cos(del_)*np.cos(del_)
    dydx[1] = (massa2*lunghezza1*state[1]*state[1]*np.sin(del_)*np.cos(del_) +
               massa2*G*np.sin(state[2])*np.cos(del_) +
               massa2*lunghezza2*state[3]*state[3]*np.sin(del_) -
               (massa1 + massa2)*G*np.sin(state[0]))/den1

    dydx[2] = state[3]

    den2 = (lunghezza2/lunghezza1)*den1
    dydx[3] = (-massa2*lunghezza2*state[3]*state[3]*np.sin(del_)*np.cos(del_) +
               (massa1 + massa2)*G*np.sin(state[0])*np.cos(del_) -
               (massa1 + massa2)*lunghezza1*state[1]*state[1]*np.sin(del_) -
               (massa1 + massa2)*G*np.sin(state[2]))/den2

    return dydx



dt = 0.06
tempo = np.arange(0.0, 20, dt)

state = np.radians([alfa, omega1, beta, omega2])


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



plot = grafico.plot([0,x1,x1,x2],[0,y1,y1,y2])

plot.grid()


grafico.show()
print(math.cos(alfa))
print(math.sin(alfa))



