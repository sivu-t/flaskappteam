import sys
import logging

class Log():
	def __init__(self):
		logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s',datefmt='%d-%b-%y %H:%M:%S')
	def debug(self,message):
		return logging.debug(message)

	def warning(self,message):
		return logging.warning(message)

	def info(self,message):
		return logging.info(message)

	def critical(self,message):
		return logging.critical(message)