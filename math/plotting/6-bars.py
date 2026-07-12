#!/usr/bin/env python3
# %%
"""Module for plotting with matplotlib and pyplot"""
import numpy as np
import matplotlib.pyplot as plt


def bars():
    """function that plots a graph"""
    np.random.seed(5)
    fruit = np.random.randint(0, 20, (4, 3))
    plt.figure(figsize=(6.4, 4.8))
    number_of_fruit = [x for x in fruit]
    # your code here
    print(fruit)
    number_of_fruit = [x for x in fruit]
    fruit_plot = {
        "apples": number_of_fruit[0],
        "bananas": number_of_fruit[1],
        "oranges": number_of_fruit[2],
        "peaches": number_of_fruit[3],
    }
    bottom_fruit = np.zeros(3)
    fruit_colors = {
        "apples": "red",
        "bananas": "yellow",
        "oranges": "orange",
        "peaches": "#ffe5b4",
    }

    plt.ylabel('Quantity of Fruit')
    plt.title('Number of Fruit per Person')
    plt.ylim(0, 80)

    for name, fruit_bar in fruit_plot.items():
        p = plt.bar(x=['Farrah', 'Fred', 'Felicia'],
                    height=fruit_bar,
                    width=0.5,
                    label=name,
                    bottom=bottom_fruit,
                    color=fruit_colors[name],
                    )
        bottom_fruit += fruit_bar
    plt.legend()
    plt.show()
