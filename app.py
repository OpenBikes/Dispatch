from flask import Flask, request, render_template
from flask_socketio import SocketIO
import redis


app = Flask(__name__)
app.config.from_object('config')

socketio = SocketIO(app)

r = redis.StrictRedis(
    host=app.config['REDIS_HOST'],
    port=app.config['REDIS_PORT'],
    db=app.config['REDIS_DB_NBR']
)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/indicate_position', methods=['PUT'])
def indicate_position():
    payload = request.get_json(force=True)
    r.hmset(payload['truck_id'], payload)
    socketio.emit('position_update', payload)
    return '', 201


if __name__ == '__main__':
    socketio.run(app)
