# Blog

A blog is a discussion or information website consisting of discrete text entries, often in an informal diary style. Entries are usually displayed in reverse chronological order, with the most recent entry appearing first, at the top of the web page. 

This blog aims to be simple, fast and light. Without straying from what a blog is, simply a place to share information.

## Quickstart

First of all, clone this repo.

``
git clone https://github.com/DD21S/simple-blog.git
``

Then, in the project directory, you install the requirements.

``
pip install -r requirements.txt
``

Now, make the migrations.

``
python3 manage.py migrate
``

Create a superuser.

``
python3 manage.py createsuperuser
``

Run collectstatic.

``
python3 manage.py collectstatic
``

And finally, run the project.

``
python3 manage.py runserver
``

Ready, now your blog is running :&#41;

---

It's recommended to use a virtual enviroment to run Python web applications.

Create one with this command:

``
python3 -m venv venv
``

## About this project

This project is developed with the Django web framework. Among other things, tests for views, models and urls which allows a more stable and consistent development and expansion of the application. Also, this blog uses the Django admin site for creating posts.

### Notes

This project is not ready to be deployed on a web server. Rather, it's made to be run on a local server. Feel free to make any necessary modifications to deploy it.  