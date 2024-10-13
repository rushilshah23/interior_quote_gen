from flask import Flask, send_from_directory, render_template
import os
import json


app = Flask(__name__, static_folder='../dist/static', template_folder='./templates')
app.config_dir = os.path.join(os.path.join("."), 'configs')


def load_nav_items():
    with open(os.path.join(app.config_dir, 'nav_items.json')) as f:
        return json.load(f) 


# Serve static files from the 'dist' folder
@app.route('/<path:path>')
def static_file(path):
    return send_from_directory(app.static_folder, path)

# Serve the index.html file at the root route
@app.route('/')
def index():
    nav_items = load_nav_items()
    return render_template('index.html', nav_items=nav_items)

if __name__ == '__main__':
    PORT = os.getenv('PORT', 3000)
    app.run(host='0.0.0.0', port=PORT, debug=True)
