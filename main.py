import os
from urllib.parse import urlparse, unquote

lines = []

with open('urls.txt', 'r') as f:
    lines = f.readlines()

for line in lines:
    o = urlparse(line.replace('\n', ''))
    filename = str(unquote(o.path.replace('/aws-resources-example/', '')))
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, 'w') as f:
        f.write(f"""<html><meta http-equiv="refresh" content="0; url=https://jennas-lee.github.io/aws-resources-example/{os.path.dirname(filename)}/"></meta></html>""")