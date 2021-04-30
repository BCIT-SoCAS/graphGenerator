# Welcome to Random Graph Generator

This is an open source project to support algorithms classes - feel free to download it and use

## Installation
You need to have Python version >=3.6 installed on the computer. If you don't, follow this tutorial:
https://www.python.org/downloads/
You should then be able to run the following command:

    python3 --version

Then, please check if you have `pip` installed as well:

    pip --version

It should come with Python - if the command above doesn't work, install it by following this link:
https://pip.pypa.io/en/stable/installing/
Once you'll have both of these, please download the [main.py](https://raw.githubusercontent.com/BCIT-SoCAS/graphGenerator/main/main.py) and [requirements.txt](https://raw.githubusercontent.com/BCIT-SoCAS/graphGenerator/main/requirements.txt) files into one folder.

Go then to this folder and run the following command:

    pip install -r requirements.txt

If there are no errors, you should be good :)

## How to run program?

Simple! Execute this command:

    python3 main.py

And answer the questions:

    How many nodes?
    5
    Weighted? 0 -> No, 1 -> Yes
    0
    Spring or shell layout? 0 -> Spring, 1 -> Shell
    1

And the results should be similar to this one:
![enter image description here](https://i.ibb.co/P4fHHNY/random-graph.png)


## Layout types

We use two, here is a [nice article](https://towardsdatascience.com/customizing-networkx-graphs-f80b4e69bedf) discussing all options:
![enter image description here](https://miro.medium.com/max/1400/1*1oMFO4lkf1nE6_8WK30W-A.png)


# Examples

Now, we provide some example questions you can ask students below

## KaTeX

You can render LaTeX mathematical expressions using [KaTeX](https://khan.github.io/KaTeX/):

The *Gamma function* satisfying $\Gamma(n) = (n-1)!\quad\forall n\in\mathbb N$ is via the Euler integral

$$
\Gamma(z) = \int_0^\infty t^{z-1}e^{-t}dt\,.
$$

> You can find more information about **LaTeX** mathematical expressions [here](http://meta.math.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference).


