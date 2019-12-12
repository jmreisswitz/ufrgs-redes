import argparse

from host.client import Client

parser = argparse.ArgumentParser()
parser.add_argument('--port', help='server\'s port')
parser.add_argument('--server', help='server\'s address')
parsed_args = parser.parse_args()


def main():
	try:
		client = Client(parsed_args.port, parsed_args.server)
		client.run()
	except Exception as e:
		print(e)


if __name__ == '__main__':
	main()
