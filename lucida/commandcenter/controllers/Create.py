from flask import *
from QueryClassifier import query_classifier
from AccessManagement import login_required
from ThriftClient import thrift_client
from Service import Service
import Config

create = Blueprint('create', __name__, template_folder='templates')

@create.route('/create', methods=['GET', 'POST'])
@login_required
def create_route():
    options = {}
    if 'request' in request.args:
        if request.args['request'] == 'Update':
            Config.load_config()
            query_classifier.__init__(Config.TRAIN_OR_LOAD, Config.CLASSIFIER_DESCRIPTIONS)
        
    try:
        # Retrieve pre-configured services.
        services_list = []
        for service in thrift_client.SERVICES.values():
            if isinstance(service, Service):
                host, port = service.get_host_port()
                services_list.append((service.name, host, port))
        options['service_list']= sorted(services_list, key=lambda i: i[0])
    except Exception as e:
        log(e)
        options['error'] = e
    return render_template("create.html", **options)
