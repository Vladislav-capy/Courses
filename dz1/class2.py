import datadz
class Game(datadz.data.Model):
    id=datadz.data.Column(datadz.data.Integer,primary_key=True)
    title=datadz.data.Column(datadz.data.String(100))
    genre=datadz.data.Column(datadz.data.String(100))
    rating=datadz.data.Column(datadz.data.Integer)