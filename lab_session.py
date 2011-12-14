import sys
from pylab import *
from scikits.audiolab import Sndfile, play

def get_ogg(f='src/emajor_piano.ogg'):
    return Sndfile(f)

def snd_length(snd):
    return float(snd.nframes) / snd.samplerate

def spec_plot(snd, start=0, end=1, fft_size=512):
    total_length = snd_length(snd)
    sample_length = (end - start)

    frame_cnt = snd.samplerate * sample_length
    seek_frame = snd.samplerate * start

    if seek_frame:
        snd.seek(seek_frame)

    samples = snd.read_frames(frame_cnt)
    left_channel = samples[:, 0]

    print "Sound length: %f. Reading %d samples (%ds)" % \
        (total_length, frame_cnt, sample_length)

    time = linspace(start, end, frame_cnt)

    # Spectrogram first
    subplot(311)
    spec = specgram(left_channel, NFFT=fft_size,
        xextent=(start, end), cmap=cm.Spectral, Fs=snd.samplerate,
        noverlap=256, pad_to=2048)
    title('Spectrogram [%d samples]' % frame_cnt)

    # Plot the time series of this signal
    subplot(312)
    plot(time, left_channel)
    title('Time series (%0.2fs)' % sample_length)

    # Calcualte an FFT of this area only and plot proper freq
    # access for analysis
    N = 1024
    fmax = snd.samplerate / 2
    sig_ft = fftshift(abs(fft(left_channel, N)))
    fscale = linspace(-fmax, fmax, N)

    subplot(313)
    mid = N/2
    plot(fscale[mid:], sig_ft[mid:])
    title('Frequency Domain (to %dHz)' % fmax)

    show()

    return (time, left_channel, spec)

def get_psd(spec, freq):
    """
        Extracts the right PSD from the specgram output
    """
    f_index = len([1 for f in spec[1] if f < freq]) - 1
    psd = (spec[2], spec[0][f_index, :])
    print "Wanted: %sHz, got %sHz [index %s]" % (freq, spec[1][f_index], f_index)
    return ((freq, f_index, spec[1][f_index]), psd)

def hps(spec, base_freq, harmonics):
    freqs = [base_freq*h for h in range(1, harmonics + 1)]
    psds = list()
    psd_freqs = list()
    for freq in freqs:
        psd_data = get_psd(spec, freq)
        psds.append(psd_data[1][1])
        psd_freqs.append(psd_data[0])
    psds.insert(0, reduce(multiply, psds))
    return psds, psd_freqs

if __name__=='__main__':
    try:
        # (Expect to run this from *within* ipython session!)
        start = float(sys.argv[1])
        end = float(sys.argv[2])
        fft_size = float(sys.argv[3])
    except IndexError:
        start = 0
        end = 2
        fft_size = 512

    snd = get_ogg()
    snd_samples = spec_plot(snd, start=start, end=end, fft_size=fft_size)
    snd.close()
    spec = snd_samples[2]
    psds = hps(spec, 440, 3)


