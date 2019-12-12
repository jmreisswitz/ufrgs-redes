from host import Host


class Client(Host):
	def __init__(self, port, server_address):
		super().__init__(port)
		self.server_address = server_address
		self.data_to_send = b'a'*1024

	def run_logic(self):
		self._socket.connect((self.server_address, self.port))
		while True:
			self.connection_loop()

	def connection_loop(self):
		data_received = self._socket.send(self.data_to_send)
		with self._lock:
			self.data_counter += data_received
