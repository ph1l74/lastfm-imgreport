import trackgetter, imagemaker
from flask import Flask


app = Flask(__name__, static_url_path='/static')


def generate(username, period):
    top_artists = trackgetter.get_top_artist(username, period)
    image_report = imagemaker.make_report_image(top_artists)
    imagemaker.save_image(image_report, 'image_report')


@app.route('/')
def index():
    return '<html><body><img src="{}" /></body></html>'.format('/static/image_report.png')


@app.route('/g')
def gen():
    generate('ph1l74', '7day')
    return '<html><body>generated</body></html>'


if __name__ == '__main__':
     app.run(host='0.0.0.0', port='5000')
