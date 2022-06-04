# Blog

This project is developed with Django.

## Quickstart

First of all, clone this repo.

```
git clone https://github.com/DD21S/simple-blog.git
```

Then, in the project directory, install the requirements.

```
pip install -r requirements.txt
```

Now, make the migrations.

```
python manage.py migrate
```

Create a superuser.

```
python manage.py createsuperuser
```

Run collectstatic.

```
python manage.py collectstatic
```

And finally, run the project.

```
python manage.py runserver
```

Ready, now your blog is running :&#41;

---

It's recommended to use a virtual enviroment to run Python web applications.

Create and activate one with these commands:

```
python3 -m venv venv
source venv/bin/activate
```
