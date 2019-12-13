import argparse
import time

import pandas as pd
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument('--csv', help='file name')
parsed_args = parser.parse_args()


def simple():
	while True:
		df = pd.read_csv(parsed_args.csv, sep=',')
		df.plot()
		plt.show()
		time.sleep(3)


def auto_update():
	while True:
		df = pd.read_csv(parsed_args.csv, sep=',')
		df.plot()
		plt.draw()
		plt.pause(1)
		plt.close('all')



def main():
	auto_update()


if __name__ == '__main__':
	main()
