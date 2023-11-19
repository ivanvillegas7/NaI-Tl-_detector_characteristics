# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 15:27:22 2023

@author: Iván
"""

import numpy as np

import scipy.optimize as opt

def gaussian(x: np.array(float), mu: float, sigma: float):
    
    return np.exp(-(x-mu)**2/(2*sigma**2))/(sigma*np.sqrt(2*np.pi))

def fit(x: np.array(float), y: np.array(float), err_y: np.array(float)):
    
    params = opt.curve_fit(gaussian, xdata=x, ydata=y, sigma=err_y)
    
    mu: float = params[0]
    
    sigma: float = params[1]
    
    cov: np.array(float, float) = params[2]
    
    return (mu, sigma, cov)