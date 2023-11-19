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
    
    #print(y1)
    
    err_y1: np.array(float) = err_y[int(round((1100-n)/m)):int(round((1260-n)/m))]
    
    mu1: float
    
    sigma1: float
    
    cov1: np.array(float, float)
    
    mu1, sigma1, cov1 = fit.fit(x1, y1, err_y1)
    
    x2: np.array(float) = x[int(round((1260-n)/m)):int(round((1420-n)/m))]
    
    y2: np.array(float) = y[int(round((1260-n)/m)):int(round((1420-n)/m))]
    
    err_y2: np.array(float) = err_y[int(round((1260-n)/m)):int(round((1420-n)/m))]
    
    mu2: float
    
    sigma2: float
    
    cov2: np.array(float, float)
    
    mu2, sigma2, cov2 = fit.fit(x2, y2, err_y2)
    
    return (mu1, sigma1, x1, mu2, sigma2, x2)

def cesium(x: np.array(float), y: np.array(float), err_y: np.array(float)):
    
    params = np.loadtxt('../Data/137Cs.Spe', skiprows=2067, max_rows=1)
    
    n: float = params[0]
    
    m: float = params[1]
    
    x: np.array(float) = x[int(round((575-n)/m)):int(round((750-n)/m))]
    
    y: np.array(float) = y[int(round((575-n)/m)):int(round((750-n)/m))]
    
    err_y: np.array(float) = err_y[int(round((575-n)/m)):int(round((750-n)/m))]
    
    mu: float
    
    sigma: float
    
    cov: np.array(float, float)
    
    mu, sigma, cov = fit.fit(x, y, err_y)
    
    return(mu, sigma, x)

def get_resolution(mu: float, sigma: float, cov):
    
    R: float = 235*sigma/mu
    
    errR: float = R*np.sqrt((cov[1, 1]/sigma)**2+(cov[0, 0]/mu)**2)
    
    print(f'\nResolution: ({R}±{errR})%')
    
    return (R, errR)