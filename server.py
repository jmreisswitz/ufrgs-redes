import argparse

from host.server import Server

parser = argparse.ArgumentParser()
parser.add_argument('--port', help='server\'s port')
parser.add_argument('--prefix', help='file prefix')
parsed_args = parser.parse_args()


def main():
	try:
		server = Server(parsed_args.port)
		server.run()
	except Exception as e:
		print(e)


if __name__ == '__main__':
	main()
