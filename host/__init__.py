from abc import ABC, abstractmethod
import socket
import threading
import time


class Host(ABC):
	def __init__(self, port):
		self.port = int(port)
		self.data_counter = 0
		self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self._lock = threading.Lock()

	def run(self):
		log_collector_thread = threading.Thread(target=self.log_connection, daemon=True)
		runner_thread = threading.Thread(target=self.run_logic, daemon=True)
		log_collector_thread.start()
		runner_thread.start()
		log_collector_thread.join()
		runner_thread.join()

	@abstractmethod
	def run_logic(self):
		pass

	def log_connection(self):
		while True:
			print('oi')
			time.sleep(1)
