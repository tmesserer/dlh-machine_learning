#!/usr/bin/env python3

if __name__ == '__main__':
    posterior = __import__('100-continuous').posterior

    print(posterior(26, 130, 0.17, 0.23))

"""
alexa@ubuntu-xenial:bayesian_prob$ ./100-main.py 
0.6098093274896221
alexa@ubuntu-xenial:bayesian_prob$
"""