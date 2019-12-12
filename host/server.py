import logging

from host import Host

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class Server(Host):
	def run_logic(self):
		self._socket.bind('localhost', self.port)
		self._socket.listen()
		conn, addr = self._socket.accept()
		self.receive_data(conn)

	def receive_data(self, conn):
		while True:
			data = conn.recv(1024)
			logger.debug(data)
			logger.debug(len(data))
			with self._lock:
				self.data_counter += len(data)


