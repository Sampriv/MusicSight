from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# List of musical notes
notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

@app.route('/')
def index():
    # Choose a random note from the list
    correct_note = random.choice(notes)

    # Shuffle the notes and create answer choices
    answer_choices = random.sample(notes, 4)

    return render_template('index.html', correct_note=correct_note, answer_choices=answer_choices)

@app.route('/check_answer', methods=['POST'])
def check_answer():
    selected_answer = request.form['answer']
    correct_note = request.form['correct_note']

    # Validate the user's answer
    if selected_answer == correct_note:
        result = 'Correct!'
    else:
        result = 'Wrong! Correct answer is {}'.format(correct_note)

    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
