import logging

from host import Host

logging.basicConfig(format='[%(name)s][%(levelname)s]: %(message)s', level=logging.WARNING)
logger = logging.getLogger(__name__)


class Server(Host):
	def __init__(self, port):
		super().__init__(port)
		self.name = __name__.split('.')[1]

	def run_logic(self):
		self._socket.bind(('127.0.0.1', self.port))
		logger.info('binded')
		self._socket.listen()
		logger.info('listening')
		conn, addr = self._socket.accept()
		self.receive_data(conn)

	def receive_data(self, conn):
		logger.info('Entering main loop')
		while True:
			data = conn.recv(1024)
			logger.info(data)
			logger.info(len(data))
			with self._lock:
				self.data_counter += len(data)
