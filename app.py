from flask import Flask, jsonify, render_template
import psutil

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/system_stats')
def system_stats():
    cpu_percent = psutil.cpu_percent(interval=1)
    virtual_memory = psutil.virtual_memory().percent
    return jsonify({
        'cpu_percent': cpu_percent,
        'virtual_memory_percent': virtual_memory
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
