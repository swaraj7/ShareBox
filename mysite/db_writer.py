import requests
import psycopg2
from ShareBox.models import snippet

json_data = requests.get('http://www.shareboxes.herokuapp.com/snippet')
data = json_data.json()
p = snippet(snippet_name=data[0], snippet_privacy=data[1], snippet_expiry=data[2], snippet_file=data[3])
p.save()
