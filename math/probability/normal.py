#!/usr/bin/env python3
"""Module for describing the poisson distribution"""
"""
π = 3.1415926536
e = 2.7182818285
er f(x) = ....
"""


class Normal:
    """ defines the class Normal for normal distributions """
    def __init__(self, data=None, mean=0., stddev=1.):
        """initiatilizes an instance under Normal
        Args:
            data: validity check, calculates it based on data if not given
            mean
            stddev
        """
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            # calc mean and stddev
            self.mean = sum(data)/len(data)
            var = sum(((x - self.mean) ** 2) for x in data) / len(data)
            std_calc = var ** (1/2)
            self.stddev = std_calc

    def z_score(self, x):
        """calculates the z score of a given x value
        Args:
            self
            x
        """
        return ((x - self.mean) / self.stddev)

    def x_value(self, z):
        """calculates the x value of a given z score
        Args:
            self
            z
        """
        return ((z * self.stddev) + self.mean)

    def pdf(self, x):
        """calculates the probability density function for a given x
        Args:
            self
            x
        """
        return ((1 / (self.stddev * (2 * 3.1415926536) ** (1/2)))
                * 2.7182818285 **
                (-((x - self.mean) ** 2) / (2 * (self.stddev ** 2)))
                )
