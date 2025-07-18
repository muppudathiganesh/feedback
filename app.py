from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Store feedback in memory (for now)
feedback_list = []

@app.route('/', methods=['GET', 'POST'])
def feedback_form():
    if request.method == 'POST':
        name = request.form['name']
        comment = request.form['comment']
        feedback_list.append({'name': name, 'comment': comment})
        return redirect(url_for('thank_you', name=name))
    return render_template('form.html')

@app.route('/thank-you/<name>')
def thank_you(name):
    return render_template('thank_you.html', name=name)

@app.route('/all-feedbacks')
def all_feedbacks():
    return render_template('feedbacks.html', feedback_list=feedback_list)

if __name__ == '__main__':
    app.run(debug=True)
