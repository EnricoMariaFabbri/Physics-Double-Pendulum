import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as grafico
from matplotlib.patches import Circle
import os

#IMPORTANTE :  il programma viene eseguito due volte pero per notare bene la differenza tra i due pendoli è opportuno inserire un tempo
#di esecuzione alto.

cartella="frames/img-{:04d}.png"

def Pendolo(cartella):

    contatore6 = 0
    while contatore6 != 1:
        tmax = int(input('inserisci il tempo di esecuzione del moto in secondi'))
        if tmax < 1 or tmax > 100:
            print("inserire un tempo compreso tra 1 e 100")
        else:
            contatore6 = 1

    contatore3 = 0
    while contatore3 != 1:
        teta1 = float(input('inserisci l ampiezza del primo angolo in gradi'))
        if teta1 < 0 or teta1 > 360:
            print("inserire angolo positivo e minore di 360 gradi")
        else:
            contatore3 = 1

    teta1 = (teta1 * np.pi)/180.0

    contatore2 = 0
    while contatore2 != 1:
        teta2 = float(input('inserisci l ampiezza del secondo angolo in gradi'))
        if teta2 < 0 or teta2 > 360:
            print("inserire angolo positivo e minore di 360 gradi")
        else:
            contatore2 = 1

    teta2 = (teta2 * np.pi)/180.0

    contatore = 0
    while contatore != 1:
        lunghezza1 = float(input('inserisci la lunghezza del primo filo in metri'))
        if lunghezza1 < 0 or lunghezza1 > 10:
            print("La lughezza non puo essere negativa ne maggiore di 10")
        else:
            contatore = 1


    contatore1 = 0
    while contatore1 != 1:
        lunghezza2 = float(input('inserisci la lunghezza del secondo filo in metri'))
        if lunghezza2 < 0 or lunghezza2 > 10:
            print("La lughezza non puo essere negativa ne maggiore di 10")
        else:
            contatore1 = 1


    print("LA DIFFERENZA TRA LE DUE MASSE NON DEVE SUPERARE I 10 KG ALTRIMENTI NON SI DISTINGUONO PIU I MOVIMENTI DEL PENDOLO")

    contatore4 = 0
    while contatore4 != 1:
        massa1 = float(input('inserisci la massa della prima sfera in chilogrammi'))
        if massa1 < 0  or massa1 > 100:
            print("La massa non puo essere negativa ne maggiore di 20 kg")
        else:
            contatore4 = 1

    contatore5 = 0
    while contatore5 != 1:
        massa2 = float(input('inserisci la massa della seconda sfera in chilogrammi'))
        if massa2 < 0 or massa2 > 100 or abs(massa2 - massa1) > 10:
            print("La massa non puo essere negativa ne maggiore di 20 kg e la differenza tra le due masse non puo essere maggiore di 10 kg")
        else:
            contatore5 = 1

    g = 9.18

    def EquazioneDelMoto(PosizioneSistemaAggiornata,tempo, lunghezza1, lunghezza2, massa1, massa2):
        teta1, z1, teta2, z2 = PosizioneSistemaAggiornata

        # semplifico la mia equazione
        cosenoRipetuto= np.cos(teta1-teta2)
        senoRipetuto = np.sin(teta1 - teta2)

        teta1primo = z1
        z1primo = (massa2*g*np.sin(teta2) - massa2*senoRipetuto*(lunghezza1*z1**2*cosenoRipetuto + lunghezza2*z2**2) -
                 (massa1+massa2)*g*np.sin(teta1)) / lunghezza1 / (massa1 + massa2*senoRipetuto**2)
        teta2primo = z2
        z2primo = ((massa1+massa2)*(lunghezza1*z1**2*senoRipetuto - g*np.sin(teta2) + g*np.sin(teta1)*cosenoRipetuto) +
                 massa2*lunghezza2*z2**2*senoRipetuto*cosenoRipetuto) / lunghezza2 / (massa1 + massa2*senoRipetuto**2)

        return teta1primo, z1primo, teta2primo, z2primo


    dt = 0.01
    tempo = np.arange(0, tmax+dt, dt)


    # condizioni iniziali
    posizioneIniziale = [teta1, 0, teta2, 0]

    # integro la mia funzione del moto
    PosizioneSistemaAggiornata = odeint(EquazioneDelMoto, posizioneIniziale, tempo, args=(lunghezza1, lunghezza2, massa1, massa2))

    # aggiorno gli angoli cosi da creare movimento
    teta1, teta2 = PosizioneSistemaAggiornata[:,0], PosizioneSistemaAggiornata[:,2]

    # posiziono nel grafico le due sfere
    PosizioneSferaX1 = lunghezza1 * np.sin(teta1)
    PosizioneSferaY1 = -lunghezza1 * np.cos(teta1)
    PosizioneSferaX2 = PosizioneSferaX1 + lunghezza2 * np.sin(teta2)
    PosizioneSferaY2 = PosizioneSferaY1 - lunghezza2 * np.cos(teta2)

    # raggio ella sfera
    r = 0.05
    # Creo la scia del movimento ad ogni secondo
    scia_secs = 1
    # faccio in modo che la scia duri scia_secs/dt
    max_trail = int(scia_secs / dt)

    def disegnaGrafico(i):

        # disegno i due fili
        ax.plot([0, PosizioneSferaX1[i], PosizioneSferaX2[i]], [0, PosizioneSferaY1[i], PosizioneSferaY2[i]], lw=2, c='k')

        chiodo = Circle((0, 0), r/2, fc='k', zorder=10)
        sfera1 = Circle((PosizioneSferaX1[i], PosizioneSferaY1[i]), r, fc='b', ec='b', zorder=10)
        sfera2 = Circle((PosizioneSferaX2[i], PosizioneSferaY2[i]), r, fc='r', ec='r', zorder=10)
        ax.add_patch(chiodo)
        ax.add_patch(sfera1)
        ax.add_patch(sfera2)

        #
        ns = 20
        s = max_trail // ns

        for j in range(ns):
            imin = i - (ns-j)*s
            if imin < 0:
                continue
            imax = imin + s + 1
            # aggiungo l effetto di schiarimento alla scia
            alpha = (j/ns)**2
            ax.plot(PosizioneSferaX2[imin:imax], PosizioneSferaY2[imin:imax], c='r', solid_capstyle='butt',
                    lw=2, alpha=alpha)

        # sistemo il piano cartesiano
        ax.set_xlim(-lunghezza1-lunghezza2-r, lunghezza1+lunghezza2+r)
        ax.set_ylim(-lunghezza1-lunghezza2-r, lunghezza1+lunghezza2+r)
        ax.set_aspect('equal', adjustable='box')
        grafico.axis()
        grafico.legend(["Tempo = ", i/100])
        grafico.savefig(cartella.format(i//di))
        grafico.cla()

    # disegno un immagine ogni di
    fps = 10
    di = int(1/fps/dt)
    fig, ax = grafico.subplots()

    for i in range(0, tempo.size, di):
        print(i // di, '/', tempo.size // di)
        disegnaGrafico(i)


Pendolo(cartella)
def save():
    os.system("ffmpeg -framerate 10 -i frames/img-%04d.png -c:v "
              "libx264 -profile:v high -crf 20 -pix_fmt yuv420p primoPendolo.mp4")

save()

cartella1 = "frames1/img-{:04d}.png"

Pendolo(cartella1)

def save1():
    os.system("ffmpeg -framerate 10 -i frames/img-%04d.png -c:v "
              "libx264 -profile:v high -crf 20 -pix_fmt yuv420p secondoPendolo.mp4")

save1()