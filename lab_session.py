import matplotlib.pyplot as plt
from numpy import linspace
from scikits.audiolab import Sndfile, play

def get_ogg(f='src/orion.ogg'):
    return Sndfile(f)

def plot_frames(n=1024):
    y = orion.read_frames(n)
    plt.plot(y)
    return y

def snd_length(snd):
    return float(snd.nframes) / snd.samplerate

def spec_plot(snd, t=1):
    frame_cnt = snd.samplerate * t
    length = snd_length(snd)

    samples = snd.read_frames(frame_cnt)

    left_channel = samples[:, 0]
    print "Sound length: %f. Reading %d samples (%ds)" % (length, frame_cnt, t)

    time = linspace(0, t, snd.samplerate*t)
    plt.subplot(211)
    fft_size = 512
    plt.specgram(left_channel, NFFT=fft_size, xextent=(0, t))
    plt.subplot(212)
    plt.plot(time, left_channel)
    plt.show()
    return (time, left_channel)

if __name__=='__main__':
    snd = get_ogg()
    snd_samples = spec_plot(snd, t=2.5)

