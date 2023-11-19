# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 15:26:14 2023

@author: Iván
"""

import numpy as np

import matplotlib.pyplot as plt

def read(file: str):
    
    time: float = np.loadtxt(f'../Data/{file}.Spe', skiprows=9, max_rows=1)[0]
    
    params: np.array(float)
    
    params = np.loadtxt(f'../Data/{file}.Spe', skiprows=2067, max_rows=1)
    
    n: float = params[0]
    
    m: float = params[1]
    
    x: np.array(float) = np.linspace(1, 2047, 2047)*m+n
    
    y: np.array(float)
    
    y = np.loadtxt(f'../Data/{file}.Spe', skiprows=12, max_rows=2047)/time
       
    plt.figure()
    plt.plot(x, y)
    plt.xlabel(r'$E$ [keV]')
    plt.ylabel(r'Counts per second [s$^{-1}$]')
    if file=='60Co':
        plt.title(r'Spectra for $^{60}$Co')
    elif file=='137Cs':
        plt.title(r'Spectra for $^{137}$Cs')
    else:        
        plt.title(f'Spectra for {file}')
    plt.grid(True)
    plt.savefig(f'../Plots/{file}.pdf')
    
    return (x, y)