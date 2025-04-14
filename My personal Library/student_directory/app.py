from flask import Flask, jsonify, render_template
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])

def get_students():
    with open('student_directory/students.json', 'r') as file:



        data = json.load(file)
    return render_template('index.html', students=data['students'])


if __name__ == "__main__":
    app.run(debug=True)
