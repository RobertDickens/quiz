from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from question_generator import generate_two_number_addition_or_subtraction_question

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/quiz/addition')
def addition_quiz():
    question_data = generate_two_number_addition_or_subtraction_question('addition')
    return render_template('quiz.html', question=question_data['question_string'],
                           answers=question_data['all_answers'])


@app.route('/quiz/subtraction')
def subtraction_quiz():
    question_data = generate_two_number_addition_or_subtraction_question('subtraction')
    return render_template('quiz.html', question=question_data['question_string'],
                           answers=question_data['all_answers'])


if __name__ == '__main__':
    app.run(debug=True)
