from flask import Flask, render_template

app = Flask(__name__)

@app.route('/FizzBuzz')
def fizzbuzz():
    numbers = range(1, 101)
    return render_template('fizzbuzz_template.html', numbers=numbers)

if __name__ == '__main__':
    app.run(debug=True)