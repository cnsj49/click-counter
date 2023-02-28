from flask import Flask, jsonify, render_template, request, redirect
import os
import redis

app = Flask(__name__)

redis_host = os.environ.get('REDIS_HOST')
redis_port = os.environ.get('REDIS_PORT')
redis_password = os.environ.get('REDIS_PASSWORD')
redis_conn = redis.Redis(host=redis_host,port=redis_port,password=redis_password)

#@app.route('/', methods=['GET', 'POST'])
#def home():
#    click_count = redis_conn.get('click_count') or 0
    #if request.method == 'POST':
    #    redis_conn.incr('click_count')
    #    click_count = redis_conn.get('click_count') or 0
    #return render_template('index.html', click_count=click_count.decode())
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        redis_conn.set('click_count', 0)
    click_count = redis_conn.get('click_count')
    if click_count:
        click_count = click_count.decode()
    else:
        click_count = 0
    return render_template('index.html', click_count=click_count)


@app.route('/click', methods=['POST'])
def click():
    redis_conn.incr('click_count')
    click_count = redis_conn.get('click_count').decode()
    return jsonify(click_count=click_count)

@app.route('/click-count')
def click_count():
    click_count = redis_conn.get('click_count')
    if click_count is None:
        click_count = 0
    else:
        click_count = int(click_count.decode())
    return (click_count)

@app.route('/reset')
def reset():
    redis_conn.set('click_count', 0)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
