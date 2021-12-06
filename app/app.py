from flask import Flask, request
from prometheus_flask_exporter import PrometheusMetrics
app = Flask(__name__)
metrics = PrometheusMetrics(app)


# static information as metric
metrics.info('app_info', 'Application info', version='1.0.3')

by_path_counter = metrics.counter(
    'by_path_counter', 'Request count by request paths',
    labels={'path': lambda: request.path}
)


@app.route('/')
@by_path_counter
def hello_world():
    return 'Hello World!'


@app.route('/simple')
@by_path_counter
def simple_get():
    return 'called /simple'


@app.route('/skip')
def skip():
    return 'called /skip : no metrics stored'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
