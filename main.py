import trackgetter, imagemaker


def generate(username, period):
    top_artists = trackgetter.get_top_artist(username, period)
    image_report = imagemaker.make_report_image(top_artists)
    image_report.show()


generate('ph1l74', '7day')