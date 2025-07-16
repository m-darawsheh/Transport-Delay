from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/get_info')
def get_info():
    return render_template('get_info.html')

if __name__ == '__main__':
    app.run(debug=True)