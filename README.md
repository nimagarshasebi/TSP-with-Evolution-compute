# Travelling Salesman Problem Solver

## Overview
This project is a Travelling Salesman Problem (TSP) solver implemented in Python. The TSP is a classic optimization problem where the goal is to find the shortest possible tour that visits each city exactly once and returns to the original city. In this implementation, we employ various genetic algorithms to approximate optimal solutions for the TSP.

## Files
- `main.py`: The main script that initializes the TSP solver, performs the evolutionary process, and visualizes the results.
- `dataset.txt`: Input file containing the distance matrix between cities.

## Classes

### `Country` Class
The `Country` class represents the set of cities and trips. It generates random trips for a specified number of salesmen.

### `TSP` Class
The `TSP` class encapsulates the TSP solver algorithms, including fitness evaluation, tournament selection, PMX and Edge crossover, inversion and scramble mutation, and functions to find the best and worst individuals. The `show_plot` method visualizes the evolution of the best and worst fitness values over generations.

## Algorithms

### PMX Crossover
The Partially Mapped Crossover (PMX) is a genetic operator used for crossover in TSP. It exchanges segments between two parents to create a child.

### Edge Crossover
Edge Crossover is another genetic operator for crossover. It builds a child by considering edges shared between parents.

### Inversion Mutation
Inversion Mutation randomly selects a subset of genes in an individual and reverses the order of genes within that subset.

### Scramble Mutation
Scramble Mutation shuffles the order of genes within a randomly chosen subset, introducing diversity in the population.

## Running the Code

1. Ensure you have Python installed on your system.
2. Install the required dependencies using:
    ```bash
    pip install matplotlib
    ```
3. Run the main script:
    ```bash
    python main.py
    ```

## Results Visualization

The results of the evolutionary process are visualized using a plot that displays the best and worst fitness values over generations.
