#!/usr/bin/python

import argparse

def find_max_profit(prices):
  min_price = int(prices[0])
  best_profit = 0
  for price in prices:
    if price < min_price:
      min_price = price
    elif (price - min_price) > best_profit:
      best_profit = price - min_price
  
  return best_profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))