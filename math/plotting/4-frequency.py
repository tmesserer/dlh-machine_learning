#!/usr/bin/env python3
"""Module for plotting with matplotlib and pyplot"""
import numpy as np
import matplotlib.pyplot as plt


def frequency():
    """function that plots a graph"""
    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)
    plt.figure(figsize=(6.4, 4.8))

    # your code here
    plt.xlabel('Grades')
    plt.ylabel('Number of Students')
    plt.title('Project A')
    plt.ylim(0, 30)
    plt.xlim(0, 100)
    plt.xticks(np.arange(0, 101, step=10))
    plt.hist(student_grades, bins=np.arange(0, 101, 10),
             histtype='bar', edgecolor='black')
    plt.show()
