# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 19:00:40 2023

@author: Iván
"""

import numpy as np

import fit

def cobalt(x: np.array(float), y: np.array(float), err_y: np.array(float)):
    
    params = np.loadtxt('../Data/60Co.Spe', skiprows=2067, max_rows=1)
    
    n: float = params[0]
    
    m: float = params[1]
    
    x1: np.array(float) = x[int(round((1100-n)/m)):int(round((1260-n)/m))]
    
    y1: np.array(float) = y[int(round((1100-n)/m)):int(round((1260-n)/m))]
    
    err_y1: np.array(float) = err_y[int(round((1100-n)/m)):int(round((1260-n)/m))]
    
    mu1: float
    
    sigma1: float
    
    A1: float
    
    err_mu1: float
    
    err_sigma1: float
    
    mu1, sigma1, A1, err_mu1, err_sigma1 = fit.fit(x1, y1, err_y1)
    
    x2: np.array(float) = x[int(round((1260-n)/m)):int(round((1420-n)/m))]
    
    y2: np.array(float) = y[int(round((1260-n)/m)):int(round((1420-n)/m))]
    
    err_y2: np.array(float) = err_y[int(round((1260-n)/m)):int(round((1420-n)/m))]
    
    mu2: float
    
    sigma2: float
    
    A2: float
    
    err_mu2: float
    
    err_sigma2: float
    
    mu2, sigma2, A2, err_mu2, err_sigma2 = fit.fit(x2, y2, err_y2)
    
    return (mu1, sigma1, A1, err_mu1, err_sigma1, x1, mu2, sigma2, A2, err_mu2, err_sigma2, x2)

def cesium(x: np.array(float), y: np.array(float), err_y: np.array(float)):
    
    params = np.loadtxt('../Data/137Cs.Spe', skiprows=2067, max_rows=1)
    
    n: float = params[0]
    
    m: float = params[1]
    
    x: np.array(float) = x[int(round((575-n)/m)):int(round((750-n)/m))]
    
    y: np.array(float) = y[int(round((575-n)/m)):int(round((750-n)/m))]
    
    err_y: np.array(float) = err_y[int(round((575-n)/m)):int(round((750-n)/m))]
    
    mu: float
    
    sigma: float
    
    A: float
    
    err_mu: float
    
    err_sigma: float
    
    mu, sigma, A, err_mu, err_sigma = fit.fit(x, y, err_y)
    
    return(mu, sigma, A, err_mu, err_sigma, x)

def get_resolution(mu: float, sigma: float, err_mu: float, err_sigma: float):
    
    R: float = 235*sigma/mu
    
    errR: float = R*np.sqrt((err_sigma/sigma)**2+(err_mu/mu)**2)
    
    print(f'\nResolution: ({R: .2f}±{errR: .2f})%\n')
    
    return (R, errR)