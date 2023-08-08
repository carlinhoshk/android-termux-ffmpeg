import subprocess
from flask import Flask, render_template, Response

app = Flask(__name__)

def generate_hls_stream():
    ffmpeg_cmd = [
        'ffmpeg',
        '-i', 'rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mp4',
        '-c:v', 'copy',
        '-c:a', 'copy',
        '-f', 'hls',
        '-hls_time', '10',
        '-hls_list_size', '6',
        '-hls_flags', 'delete_segments',
        'static/hls/stream.m3u8'
    ]
    return subprocess.Popen(ffmpeg_cmd)

@app.route('/')
def index():
    return render_template('index.html')

def video_stream():
    process = generate_hls_stream()
    while True:
        try:
            process.wait()
        except subprocess.CalledProcessError:
            continue
        else:
            break

@app.route('/video_feed')
def video_feed():
    return Response(video_stream(), mimetype='application/vnd.apple.mpegurl')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090)
