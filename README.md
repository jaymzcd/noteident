# Note Identification of musical instruments via Spectral Analysis

## Introduction

This is an old hobby of mine from university. I'm trying to identify at least
*one* note from a guitar solo over time from a recording. Using FFTs and spectral
analysis I assume something is rougly possible. By using some knoweldge about
"expected" frequencies and some statistics.

It's also a good way to learn pylab some more (matplotlib/numpy) and get used to
using it for numerical work in combination with Sage. The idea/work that I
did to remind myself of the interest in this is: http://goo.gl/RtWhn

## Setup / Requirements

Use [audiolab](https://github.com/cournape/audiolab) to read in ogg files to a
numpy array. Then plot specgram.

http://matplotlib.sourceforge.net/api/mlab_api.html#matplotlib.mlab.specgram
http://www.ar.media.kyoto-u.ac.jp/members/david/softwares/audiolab/sphinx/index.html

The specgram plot will return a tuple consiting of ["periodograms"](http://en.wikipedia.org/wiki/Periodogram),
the frequency bins and the time axis data for the plot. Within the lab session
the individual PSDs can be plotted for example:

## Good resources

  * [Note frequencies](http://www.vaughns-1-pagers.com/music/musical-note-frequencies.htm)
  * [Ranges of instruments to a piano](http://www.bosendorfer-audio.co.uk/frequencies_of_music.html)


## Sample

Sample matches tab at section starting line 699.
