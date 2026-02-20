from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

# This endpoint receives the URL from your local Python script
@app.route('/update_video', methods=['POST'])
def update_video():
    video_url = request.json.get('url')
    # This sends the URL to the open browser window via WebSockets
    socketio.emit('new_video', {'url': video_url})
    return {"status": "success"}, 200

if __name__ == '__main__':
    socketio.run(app, debug=True)
