from datetime import datetime


class ConnectionLogger:
	filename = 'data.csv'

	@classmethod
	def log_data(cls, source, data, prefix):
		cls.log_to_file(source, data, prefix)
		cls.log_to_stdout(data)

	@classmethod
	def log_to_file(cls, source, data, prefix):
		with open(f'{prefix}_{source}_{cls.filename}', 'a+') as file:
			file.write(f'{datetime.now()},{data/8}\n')

	@classmethod
	def log_to_stdout(cls, data):
		print(f'received: {data} bytes')

