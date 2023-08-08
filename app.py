import subprocess
from flask import Flask, Response

app = Flask(__name__)

@app.route('/stream.m3u8')
def stream():
    ffmpeg_cmd = [
        'ffmpeg',
        '-i', 'rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mp4',
        '-c:v', 'copy',
        '-c:a', 'copy',
        '-f', 'hls', '-hls_time', '10', '-hls_list_size', '6', '-hls_flags', 'delete_segments', 'stream.m3u8'
    ]
    subprocess.Popen(ffmpeg_cmd)
    return Response(open('stream.m3u8', 'rb').read(), content_type='application/vnd.apple.mpegurl')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090)
