# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 11:53:00 2023

@author: Iván
"""

import numpy as np

import matplotlib.pyplot as plt

from typing import List

import read

import fit

import analyse

def main():
    
    files: List[str] = ['background', '60Co', '137Cs', 'callibration']
    
    err_time: float = 0.01
    
    background: np.array(float)
    
    energy: np.array(float)
    
    energy, background = read.read(files[0])
    
    time_background: float = np.loadtxt('../Data/background.Spe',\
                                        skiprows=9, max_rows=1)[0]
    
    Co: np.array(float)
    
    energyCo: np.array(float)
    
    energyCo, Co = read.read(files[1])
    
    time_Co: float = np.loadtxt('../Data/60Co.Spe', skiprows=9, max_rows=1)[0]
    
    Co = Co-background
    
    err_Co2: np.array(float) = Co/time_Co**2+Co**2*err_time**2/time_Co**4+\
                              background/time_background**2+\
                              background**2*err_time**2/time_background**4
    
    Cs: np.array(float)
    
    energyCs: np.array(float)
    
    energyCs, Cs = read.read(files[2])
    
    time_Cs: float = np.loadtxt('../Data/137Cs.Spe', skiprows=9, max_rows=1)[0]
    
    Cs = Cs-background
    
    err_Cs2: np.array(float) = Cs/time_Cs**2+Cs**2*err_time**2/time_Cs**4+\
                              background/time_background**2+\
                              background**2*err_time**2/time_background**4
    
    read.read(files[3])
        
    mu1: float
    
    sigma1: float
    
    err_mu1: float
    
    err_sigma1: float
    
    x1: np.array(float)
    
    mu2: float
    
    sigma2: float
    
    err_mu2: float
    
    err_sigma2: float
    
    x2: np.array(float)
    
    mu1, sigma1, err_mu1, err_sigma1, x1, mu2, sigma2, err_mu2, err_sigma2, x2 = analyse.cobalt(energyCo, Co, np.sqrt(err_Co2))
    
    print('\nFirst peak of cobalt-60:')
    
    R1: float
    
    errR1: float
    
    R1, errR1 = analyse.get_resolution(mu1, sigma1, err_mu1, err_sigma1)
    
    print('\nSecond peak of cobalt-60:')
    
    R2: float
    
    errR2: float
    
    R2, errR2 = analyse.get_resolution(mu2, sigma2, err_mu2, err_sigma2)
    
    plt.figure()
    plt.errorbar(energyCo, Co, yerr=np.sqrt(Co+background))
    plt.plot(x1, fit.gaussian(x1, mu1, sigma1),\
             label=f'μ={mu1}±{err_mu1}; σ={sigma1}±{err_sigma2}')
    plt.plot(x2, fit.gaussian(x2, mu2, sigma2),\
             label=f'μ={mu2}±{err_mu2}; σ={sigma2}±{err_sigma2}')
    plt.xlabel(r'$E$ [keV]')
    plt.ylabel(r'Counts per second [s$^{-1}$]')
    plt.title(r'Spectra for $^{60}$Co')
    plt.grid(True)
    plt.savefig('../Plots/60Co-background.pdf')
    
    mu: float
    
    sigma: float
    
    err_mu: float
    
    err_sigma: float
    
    x: np.array(float)
    
    mu, sigma, err_mu, err_sigma, x = analyse.cesium(energyCs, Cs, np.sqrt(err_Cs2))    
    
    print('\nPeak of cesium-137:')
    
    R: float
    
    errR: float
    
    R, errR = analyse.get_resolution(mu, sigma, err_mu, err_sigma)
    
    plt.figure()
    plt.errorbar(energyCs, Cs, yerr=np.sqrt(Cs+background))
    plt.plot(x, fit.gaussian(x, mu, sigma),\
             label=f'μ={mu}±{err_mu}; σ={sigma}±{err_sigma}')
    plt.xlabel(r'$E$ [keV]')
    plt.ylabel(r'Counts per second [s$^{-1}$]')
    plt.title(r'Spectra for $^{137}$Cs')
    plt.grid(True)
    plt.savefig('../Plots/137Cs-background.pdf')
    
    print('\nMean value:')
    
    R_mean: float = (R1+R2+R)/3
    
    errR_mean: float = np.sqrt(errR1**2+errR2**2+errR**2)/3
    
    print(f'\nResolution mean value: R=({R_mean}±{errR_mean})%')
    
main()