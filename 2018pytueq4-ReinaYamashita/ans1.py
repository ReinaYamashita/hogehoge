# -*- coding: utf-8 -*-

# 以下に，適宜，クラス，関数，スクリプトなどを記述し，
# 課題4を解くこと．

import numpy as np
import scipy as sp
import scipy.fftpack as spf
from scipy.io.wavfile import read, write
import matplotlib.pyplot as plt

ifname = 'Noisedvoice1.wav'                                       
o1fname = 'K00500.wav'                                            


def LowPass( x, f, Fs=44100. ):
    N = len(x)
    fdelta = float(Fs)/N
    X = spf.fft( x )
    Ncut = int(f/fdelta)  # カットオフ周波数対応添え字                            
    flt = np.zeros(N)
    flt[0:Ncut] = 1
    flt[-Ncut+1:] = 1

    xflt = spf.ifft( X * flt ) # フィルタ処理                                     
    return xflt.real # 実部だけを返す                                             


y = read( ifname )

Fs = y[0]          # サンプリングレート                                         
Nmax = 65536*2       # FFT のため 2 のベキにしておく                            
yl = y[1][:Nmax,0] # 左音声の 0〜Nmax-1 までを信号とする                          
fc = 1000           # 1000Hz で遮断してみる                                        

yflt = LowPass( yl, fc, Fs )

write(o1fname, Fs, np.int16( np.real(yflt) ).reshape(Nmax,1) )





