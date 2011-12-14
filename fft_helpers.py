from scipy import *
from pylab import *

def fft_plot():
    f = 3 # hz
    fs = 2000.0 # sampling freq

    L = 128

    x = arange(0, L, 1/fs)
    y = 5*sin(2*pi*f*x) + sin(2*pi*f*3*x) + 10*sin(2*pi*(f+3)*5*x)

    fmax = fs / 2

    N = 1024
    yft = fft(y, N)
    faxis = linspace(-fmax, fmax, N)

    yshift = fftshift(abs(yft))

    return (x, y, faxis, yshift)

def plot_stuff(x, y, fx, ft):
    subplot(211)
    plot(x, y)
    subplot(212)
    mid = len(fx)/2
    plot(fx[mid:], ft[mid:])


