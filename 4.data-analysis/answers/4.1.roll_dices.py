#!/usr/bin/env python3

import argparse
import numpy as np
import matplotlib.pyplot as plt

def roll_dice(nb_dices):
  """
  Simulates rolling a specified number of 6-sided dice and returns the sum.

  Parameters:
    nb_dices (int): The number of dice to roll.

  Returns:
    int: The sum of the values from rolling `nb_dices` 6-sided dice.
  """
  return np.sum(np.random.randint(1, 7, nb_dices))

def run(nb_dices=10, nb_rolls=10000):
  """
  Runs a simulation of rolling dice multiple times and plots the distribution.

  Parameters:
    nb_dices (int): The number of dice to roll in each trial.
    nb_rolls (int): The number of trials (dice rolls) to perform.

  This function simulates rolling `nb_dices` dice `nb_rolls` times, stores the
  sum of each roll, and plots a histogram of the results to illustrate the 
  distribution of sums.
  """
  # Generate a list of sums from dice rolls
  dice_sums = [roll_dice(nb_dices) for _ in range(nb_rolls)]
    
  # Plotting the histogram
  plt.hist(dice_sums, bins=30, density=True, color='skyblue', edgecolor='black')
  plt.xlabel("Sum of rolls")
  plt.ylabel("Frequency")
  plt.title(f"Distribution of the sum of rolls of {nb_dices} dices")
  plt.show()

if __name__ == "__main__":

  # Argument parsing
  parser = argparse.ArgumentParser(description="Simulate rolling dice and plot the sum distribution.")
  parser.add_argument("-d", "--nb_dices", type=int, default=10, help="Number of dice to roll in each trial")
  parser.add_argument("-r", "--nb_rolls", type=int, default=10000, help="Number of trials (rolls) to perform")

  args = parser.parse_args()

  run(nb_dices=args.nb_dices, nb_rolls=args.nb_rolls)
