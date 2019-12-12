from datetime import datetime


class ConnectionLogger:
	filename = 'data.csv'

	@classmethod
	def log_data(cls, source, data):
		cls.log_to_file(source, data)

	@classmethod
	def log_to_file(cls, source, data):
		with open(f'{source}_{cls.filename}', 'a+') as file:
			file.write(f'{datetime.now()},{data}\n')

