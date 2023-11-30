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
    
    err_time: float = 1
    
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
    
    A1: float
    
    err_mu1: float
    
    err_sigma1: float
    
    x1: np.array(float)
    
    mu2: float
    
    sigma2: float
    
    A2: float
    
    err_mu2: float
    
    err_sigma2: float
    
    x2: np.array(float)
    
    mu1, sigma1, A1, err_mu1, err_sigma1, x1, mu2, sigma2, A2, err_mu2, err_sigma2, x2 = analyse.cobalt(energyCo, Co, np.sqrt(err_Co2))
    
    print('\nFirst peak of cobalt-60:')
    
    R1: float
    
    errR1: float
    
    R1, errR1 = analyse.get_resolution(mu1, sigma1, err_mu1, err_sigma1)
    
    print('\nSecond peak of cobalt-60:')
    
    R2: float
    
    errR2: float
    
    R2, errR2 = analyse.get_resolution(mu2, sigma2, err_mu2, err_sigma2)
    
    plt.figure()
    plt.errorbar(energyCo, Co, yerr=np.sqrt(err_Co2), fmt='.', linestyle='none')
    plt.plot(x1, fit.gaussian(x1, mu1, sigma1, A1),\
             label=f'μ={mu1: .2f}±{err_mu1: .2f}; σ={sigma1: .2f}±{err_sigma2: .2f}')
    plt.plot(x2, fit.gaussian(x2, mu2, sigma2, A2),\
             label=f'μ={mu2: .2f}±{err_mu2: .2f}; σ={sigma2: .2f}±{err_sigma2: .2f}')
    plt.xlabel(r'$E$ [keV]')
    plt.ylabel(r'Counts per second [s$^{-1}$]')
    plt.title(r'Spectra for $^{60}$Co')
    plt.grid(True)
    plt.legend()
    plt.savefig('../Plots/60Co-background.pdf')
    
    mu: float
    
    sigma: float
    
    A: float
    
    err_mu: float
    
    err_sigma: float
    
    x: np.array(float)
    
    mu, sigma, A, err_mu, err_sigma, x = analyse.cesium(energyCs, Cs, np.sqrt(err_Cs2))    
    
    print('\nPeak of cesium-137:')
    
    R: float
    
    errR: float
    
    R, errR = analyse.get_resolution(mu, sigma, err_mu, err_sigma)
    
    mu_back: float
    
    sigma_back: float
    
    err_mu_back: float
    
    err_sigma_back: float
    
    x_back: np.array(float)
    
    mu_back, sigma_back, A_back, err_mu_back, err_sigma_back, x_back = analyse.cesium_back(energyCs, Cs, np.sqrt(err_Cs2))    
    
    plt.figure()
    plt.errorbar(energyCs, Cs, yerr=np.sqrt(err_Cs2), fmt='.', linestyle='none')
    plt.plot(x, fit.gaussian(x, mu, sigma, A),\
             label=f'μ={mu: .2f}±{err_mu: .2f}; σ={sigma: .2f}±{err_sigma: .2f}')
    plt.plot(x_back, fit.gaussian(x_back, mu_back, sigma_back, A_back),\
             label=f'μ={mu_back: .1f}±{err_mu_back: .1f}; σ={sigma_back: .0f}±{err_sigma_back: .0f}')
    plt.xlabel(r'$E$ [keV]')
    plt.ylabel(r'Counts per second [s$^{-1}$]')
    plt.title(r'Spectra for $^{137}$Cs')
    plt.grid(True)
    plt.legend()
    plt.savefig('../Plots/137Cs-background.pdf')
    
    m_e: float
    
    m_e_err: float
    
    m_e, m_e_err = analyse.get_electron_mass(mu, err_mu, mu_back, err_mu_back)
    
    print(f'Mass of the electron: ({m_e: .0f}±{m_e_err: .0f})keV.')
    
main()
