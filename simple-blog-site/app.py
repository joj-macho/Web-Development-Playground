from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length
import markdown2
import os
from pathlib import Path
from datetime import datetime


# Set Working Directory
BASE_DIRECTORY = Path(__file__).resolve().parent
os.chdir(BASE_DIRECTORY)

# Initialize the Flask application
app = Flask(__name__)

# Configure the application with a secret key and database URI
app.config['SECRET_KEY'] = os.urandom(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog_database.db'

# Initialize the SQLAlchemy object to interact with the database
db = SQLAlchemy(app)

# Register the markdown filter
@app.template_filter('markdown')
def render_markdown(content):
    return markdown2.markdown(content)

# Post Form class for creating and editing posts
class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=255)])
    body = TextAreaField('Body', validators=[DataRequired()])
    submit = SubmitField('Submit')

# Post class to represent the database model for blog posts.
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    body = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Post {self.title}>'

# Create the database
with app.app_context():
    db.create_all()


@app.route('/')
def index():
    '''Render the home page with a list of all blog posts.'''
    posts = Post.query.order_by(Post.date_created.desc()).all()
    return render_template('index.html', posts=posts)

@app.route('/post/<int:id>')
def post(id):
    '''Render a single blog post based on the provided ID.'''
    post = Post.query.get_or_404(id)
    post.body = markdown2.markdown(post.body)  # Convert Markdown to HTML
    return render_template('post.html', post=post)

@app.route('/posts')
def posts():
    '''Render the page with a list of all blog posts.'''
    posts = Post.query.order_by(Post.date_created.desc()).all()
    return render_template('posts.html', posts=posts)

@app.route('/create', methods=['GET', 'POST'])
def create():
    '''Render the page for creating a new blog post or handle form submission.'''
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, body=form.body.data)
        db.session.add(post)
        db.session.commit()
        flash('Post created successfully!', 'success')
        return redirect(url_for('post', id=post.id))
    return render_template('create_or_edit.html', form=form, action='Create')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    '''Render the page for editing an existing blog post or handle form submission.'''
    post = Post.query.get_or_404(id)
    form = PostForm(obj=post)
    if form.validate_on_submit():
        form.populate_obj(post)
        db.session.commit()
        flash('Post updated successfully!', 'success')
        return redirect(url_for('post', id=post.id))
    return render_template('create_or_edit.html', post=post, form=form, action='Edit')

@app.route('/delete/<int:id>')
def delete(id):
    '''Delete a blog post based on the provided ID.'''
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    flash('Post deleted successfully!', 'success')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)