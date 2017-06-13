import Config
from Database import database
from Service import Service

def load_config():
	service_list = database.db["service_info"].find()
	count = service_list.count()
	for i in range(count):
		service_obj = service_list[i]
		acn = service_obj['acronym']
		port = service_obj['port']
		input_type = service_obj['input']
		Config.SERVICES[acn] = Service(acn, port, input_type, None)
