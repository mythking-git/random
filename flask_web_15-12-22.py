from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    completed = db.Column(db.Boolean)
    due_date = db.Column(db.Date)

    def __init__(self, title, completed=False, due_date=None):
        self.title = title
        self.completed = completed
        self.due_date = due_date

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'completed': self.completed,
            'due_date': self.due_date,
        }

@app.route('/')
def index():
    todos = Todo.query.all()
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    title = request.form['title']
    completed = 'completed' in request.form
    due_date = request.form['due_date']
    todo = Todo(title, completed, due_date)
    db.session.add(todo)
    db.session.commit()
    return redirect('/')

@app.route('/update/<id>', methods=['POST'])
def update(id):
    todo = Todo.query.get(id)
    todo.title = request.form['title']
    todo.completed = 'completed' in request.form
    todo.due_date = request.form['due_date']
    db.session.commit()
    return redirect('/')

@app.route('/delete/<id>', methods=['POST'])
def delete(id):
    todo = Todo.query.get(id)
    db.session.delete(todo)
    db.session.commit()
    return redirect('/')
    
with app.app_context():
    db.create_all()
