# zuri-crud

## Getting Started the first thing to do is to clone the repository:

$ git clone https://github.com/dejetem/zuri-crud.git
$ cd zuri-crud

## Create a virtual environment to install dependencies in and activate it:

```bash
$ python -m venv env
$ env\Scripts\activate.bat
```

## Then install the dependencies:

```bash
(env)$ pip install -r requirements.txt
```

Note the (env) in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by venv

## run the server:

```bash
(env)$ python manage.py runserver
```


# Tests

## To run the tests

```bash
(env)$ python manage.py test blog
```