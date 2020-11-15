from flask import Flask, render_template, request, redirect
import re

app = Flask(__name__)

todo_items = []


@app.route('/')
def index():
    return render_template('index.html', todo_items=todo_items)


@app.route('/submit', methods=['POST'])
def submit():
    task = request.form['Task Name']
    priority = request.form['Priority']
    email = request.form['Email Address']

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return redirect('/')
    elif not task:
        return redirect('/')
    elif priority == 'Priority':
        return redirect('/')
    else:
        todo_items.append((task, priority, email))

    print(todo_items)
    return redirect('/')


@app.route('/clear', methods=['POST'])
def clear():
    del todo_items[:]
    return redirect('/')


if __name__ == '__main__':
    app.run()

