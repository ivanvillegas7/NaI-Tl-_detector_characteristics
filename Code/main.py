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
    
    background: np.array(float)
    
    energy: np.array(float)
    
    background, energy = read.read(files[0])
    
    Co: np.array(float) = read.read(files[1])-background
    
    Cs: np.array(float) = read.read(files[2])-background
    
    read.read(files[3])
    
    mu1: float
    
    sigma1: float
    
    cov1: np.array(float, float)
    
    x1: np.array(float)
    
    mu2: float
    
    sigma2: float
    
    cov2: np.array(float, float)
    
    x2: np.array(float)
    
    mu1, sigma1, cov1, x1, mu2, sigma2, cov2, x2 = analyse.cobalt(energy, Co, np.sqrt(Co+background))
    
    print('\nFirst peak of cobalt-60:')
    
    R1: float
    
    errR1: float
    
    R1, errR1 = analyse.get_resolution(mu1, sigma1, cov1)
    
    print('\nSecond peak of cobalt-60:')
    
    R2: float
    
    errR2: float
    
    R2, errR2 = analyse.get_resolution(mu2, sigma2, cov2)
    
    plt.figure()
    plt.errorbar(energy, Co, yerr=np.sqrt(Co+background))
    plt.plot(x1, fit.gaussian(x1, mu1, sigma1),\
             label=f'μ={mu1}±{cov1[0, 0]}; σ={sigma1}±{cov1[1, 1]}')
    plt.plot(x2, fit.gaussian(x2, mu2, sigma2),\
             label=f'μ={mu2}±{cov2[0, 0]}; σ={sigma2}±{cov2[1, 1]}')
    plt.xlabel(r'$E$ [keV]')
    plt.ylabel(r'Counts per second [s$^{-1}$]')
    plt.title(r'Spectra for $^{60}$Co')
    plt.grid(True)
    plt.savefig('../Plots/60Co-background.pdf')

    mu: float
    
    sigma: float
    
    cov: np.array(float, float)
    
    x: np.array(float)
    
    mu, sigma, cov, x = analyse.cesium(energy, Cs, np.sqrt(Cs+background))
    
    print('\nPeak of cesium-137:')
    
    R: float
    
    errR: float
    
    R, errR = analyse.get_resolution(mu, sigma, cov)
    
    plt.figure()
    plt.errorbar(energy, Cs, yerr=np.sqrt(Cs+background))
    plt.plot(x, fit.gaussian(x, mu, sigma),\
             label=f'μ={mu}±{cov[0, 0]}; σ={sigma}±{cov[1, 1]}')
    plt.xlabel(r'$E$ [keV]')
    plt.ylabel(r'Counts per second [s$^{-1}$]')
    plt.title(r'Spectra for $^{137}$Cs')
    plt.grid(True)
    plt.savefig('../Plots/137Cs-background.pdf')
    
    R_mean: float = (R1+R2+R)/3
    
    errR_mean: float = np.sqrt(errR1**2+errR2**2+errR**2)/3
    
    print(f'\nResolution mean value: R=({R_mean}±{errR_mean})%')
    
main()