import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as grafico
from matplotlib.patches import Circle

"""˙z=m2gsinθ2cos(θ1−θ2)−m2sin(θ1−θ2)[l1z21cos(θ1−θ2)+l2z22]−(m1+m2)gsinθ1l1[m1+m2sin2(θ1−θ2)],
z˙2=(m1+m2)[l1z21sin(θ1−θ2)−gsinθ2+gsinθ1cos(θ1−θ2)]+m2l2z22sin(θ1−θ2)cos(θ1−θ2)l2[m1+m2sin2(θ1−θ2)]"""


teta1 = float(input('inserisci il primo angolo in gradi'))
teta2 = float(input('inserisci il secondo angolo in gradi'))
lunghezza1 = float(input('inserisci la lunghezza del primo filo in cm'))
lunghezza2 = float(input('inserisci la lunghezza del secondo filo in cm'))
massa1 = float(input('inserisci la massa del primo filo in kg'))
massa2 = float(input('inserisci la massa del secondo filo in kg'))

g = 9.18

def EquazioneDelMoto(PosizioneSistemaAggiornata,tempo, lunghezza1, lunghezza2, massa1, massa2):
    teta1, z1, teta2, z2 = PosizioneSistemaAggiornata

    cosenoRipetuto= np.cos(teta1-teta2)
    senoRipetuto = np.sin(teta1 - teta2)

    teta1primo = z1
    z1primo = (massa2*g*np.sin(teta2) - massa2*senoRipetuto*(lunghezza1*z1**2*cosenoRipetuto + lunghezza2*z2**2) -
             (massa1+massa2)*g*np.sin(teta1)) / lunghezza1 / (massa1 + massa2*senoRipetuto**2)
    teta2primo = z2
    z2primo = ((massa1+massa2)*(lunghezza1*z1**2*senoRipetuto - g*np.sin(teta2) + g*np.sin(teta1)*cosenoRipetuto) +
             massa2*lunghezza2*z2**2*senoRipetuto*cosenoRipetuto) / lunghezza2 / (massa1 + massa2*senoRipetuto**2)

    return teta1primo, z1primo, teta2primo, z2primo

# Maximum time, time point spacings and the time grid (all in s).
tmax, dt = 20, 0.01
tempo = np.arange(0, tmax+dt, dt)
# Initial conditions.

posizioneIniziale = [teta1, 0, teta2, 0]

# Do the numerical integration of the equations of motion
PosizioneSistemaAggiornata = odeint(EquazioneDelMoto, posizioneIniziale, tempo, args=(lunghezza1, lunghezza2, massa1, massa2))
# Unpack z and theta as a function of time
teta1, teta2 = PosizioneSistemaAggiornata[:,0], PosizioneSistemaAggiornata[:,2]

# Convert to Cartesian coordinates of the two bob positions.
PosizioneSferaX1 = lunghezza1 * np.sin(teta1)
PosizioneSferaY1 = -lunghezza1 * np.cos(teta1)
PosizioneSferaX2 = PosizioneSferaX1 + lunghezza2 * np.sin(teta2)
PosizioneSferaY2 = PosizioneSferaY1 - lunghezza2 * np.cos(teta2)

# Plotted bob circle radius
r = 0.05
# Plot a trail of the massa2 bob's position for the last trail_secs seconds.
trail_secs = 1
# This corresponds to max_trail time points.
max_trail = int(trail_secs / dt)

def make_plot(i):
    # Plot and save an image of the double pendulum configuration for time
    # point i.
    # The pendulum rods.
    ax.plot([0, PosizioneSferaX1[i], PosizioneSferaX2[i]], [0, PosizioneSferaY1[i], PosizioneSferaY2[i]], lw=2, c='k')
    # Circles representing the anchor point of rod 1, and bobs 1 and 2.
    c0 = Circle((0, 0), r/2, fc='k', zorder=10)
    c1 = Circle((PosizioneSferaX1[i], PosizioneSferaY1[i]), r, fc='b', ec='b', zorder=10)
    c2 = Circle((PosizioneSferaX2[i], PosizioneSferaY2[i]), r, fc='r', ec='r', zorder=10)
    ax.add_patch(c0)
    ax.add_patch(c1)
    ax.add_patch(c2)

    # The trail will be divided into ns segments and plotted as a fading line.
    ns = 20
    s = max_trail // ns

    for j in range(ns):
        imin = i - (ns-j)*s
        if imin < 0:
            continue
        imax = imin + s + 1
        # The fading looks better if we square the fractional length along the
        # trail.
        alpha = (j/ns)**2
        ax.plot(PosizioneSferaX2[imin:imax], PosizioneSferaY2[imin:imax], c='r', solid_capstyle='butt',
                lw=2, alpha=alpha)

    # Centre the image on the fixed anchor point, and ensure the axes are equal
    ax.set_xlim(-lunghezza1-lunghezza2-r, lunghezza1+lunghezza2+r)
    ax.set_ylim(-lunghezza1-lunghezza2-r, lunghezza1+lunghezza2+r)
    ax.set_aspect('equal', adjustable='box')
    grafico.axis()
    grafico.legend(["Tempo = ", i/100])
    grafico.savefig('frames/_img{:04d}.png'.format(i//di))
    grafico.cla()


# Make an image every di time points, corresponding to a frame rate of fps
# frames per second.
# Frame rate, s-1
fps = 10
di = int(1/fps/dt)
fig, ax = grafico.subplots()

for i in range(0, tempo.size, di):
    print(i // di, '/', tempo.size // di)
    make_plot(i)