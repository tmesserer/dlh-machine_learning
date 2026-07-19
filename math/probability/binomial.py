#!/usr/bin/env python3
"""Module for describing the binomial distribution"""
π = 3.1415926536
e = 2.7182818285


class Binomial:
    """defines the class Binomial for binomial distributions"""
    def __init__(self, data=None, n=1, p=0.5):
        """
        Initiatilizes an instance under Binomial
        Args:
            self
            data: list of data to estimate the distribution
            n: bernoulli trials number
            p: probability of success
        """
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            if p <= 0 or p >= 1:
                raise ValueError("p must be greater than 0 and less than 1")
            self.n = int(n)
            self.p = float(p)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            # calc est mean and var
            est_mean = sum(data)/len(data)
            est_var = sum(((x - est_mean) ** 2)
                               for x in data) / len(data)

            # mu = n*p
            # var = np(1-p)
            # var/mu = 1-p
            # p1 = 1- var / mu
            # self.p1 = 1 - (self.est_var / self.est_mean)
            p1 = 1 - (est_var / est_mean)
            self.n = round(est_mean / p1)

            # n= mu / p
            # n = round(n_est, 0)
            # new p = mu / n
            self.p = est_mean / self.n
