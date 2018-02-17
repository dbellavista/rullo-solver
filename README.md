# Rullo Solver

Author: Daniele Bellavista

Solver for https://play.google.com/store/apps/details?id=air.com.akkad.rullo

## Why

Rullo is a nice relaxing game, however the 2-4 mode require you to do some mental backtracking. So I decided to create a solver for it.

## Requirements

The script is in python3 but it's only a wrapper around `lp_solve` which you have to install (http://web.mit.edu/lpsolve/doc/)

* `sudo pacman -S lpsolve`
* `sudo apt-get install lp-solve`

## Usage

First of all you have to create a file containing the problem. The first N rows are expected to contain the input cell values,
the last two rows respectively the column sums (the horizontal constraints) and the row sums (the vertical constraints).

For instance

![alt text](https://raw.githubusercontent.com/dbellavista/rullo-solver/master/doc/problem1.png)

became:

```
4 7 14 15 17
7 19 6 18 11
12 17 18 12 12
2 12 13 18 2
16 1 10 5 1
2 55 41 32 41
39 30 59 27 16
```

Save the matrix as a text file and run `python3 ./solver.py ./problem.txt`.
The result will be the solution (`1 => on`, `0 => off`)

```
0 1 0 1 1
0 1 0 0 1
0 1 1 1 1
1 1 1 0 0
0 0 1 1 1
```
