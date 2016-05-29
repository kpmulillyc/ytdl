import pafy
from flask import Flask,render_template,jsonify,request


def humansize(nbytes):
    suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
    if nbytes == 0: return '0 B'
    i = 0
    while nbytes >= 1024 and i < len(suffixes)-1:
        nbytes /= 1024.
        i += 1
    f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
    return '%s %s' % (f, suffixes[i])




app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/doThisForPapa')
def doThisForPapa():
    url = request.args.get('txt')
    try:
        video = pafy.new(url)
        video2 = str(video).splitlines()
        thumb = video2[len(video2) - 1].split(" ")
        streams = video.streams
        urls = {}
        for i in streams:
            B = str(i.resolution) + " " + str(i.extension) + " " + str(humansize(i.get_filesize()))
            urls[B] = i.url
        return jsonify(urls=urls, video=video2[:len(video2) - 1], thumb=thumb[1])
    except:
        return jsonify(video="")

if __name__ == '__main__':
    app.run()
