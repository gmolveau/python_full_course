# Virtual environment / virtualenv / venv / env

Virtualenv is a tool to create isolated Python environments. (if you want to learn more about it [go there](https://virtualenv.pypa.io/en/stable/)).

This tool will allow us to create a virtual environment for each project. Each project can install its own dependencies without contaminating other projects.

This also means that you will be able to share your project with a liste of every dependencies required, easily via a file called requirements.txt (more on this later).

## Usage

First we need to create the `venv` :

```bash
# python3 -m venv <name_of_venv>
# usually we name it venv
python3 -m venv venv
# creates a venv directory which contains the virtualenvironment
```

Then we need to activate it :

```bash
# macos and linux
source venv/bin/activate
# windows
source venv/Scripts/Activate.ps1
```

Note : some code editor like `pycharm` or `vscode` will automatically detect virtualenvironments.

Depending on your `shell` (`zsh` for example) you can have a visual indicator telling you that you're in a `venv`.

```bash
# example
(venv) $ ...
```

We can now install dependencies in our `venv` :

```bash
(venv) $ pip install flask
Collecting flask
  Using cached Flask-2.0.2-py3-none-any.whl (95 kB)
Collecting Jinja2>=3.0
  Using cached Jinja2-3.0.3-py3-none-any.whl (133 kB)
Collecting Werkzeug>=2.0
  Using cached Werkzeug-2.0.2-py3-none-any.whl (288 kB)
Collecting click>=7.1.2
  Using cached click-8.0.3-py3-none-any.whl (97 kB)
Collecting itsdangerous>=2.0
  Using cached itsdangerous-2.0.1-py3-none-any.whl (18 kB)
Collecting MarkupSafe>=2.0
  Using cached MarkupSafe-2.0.1-cp39-cp39-macosx_10_9_x86_64.whl (13 kB)
Installing collected packages: MarkupSafe, Werkzeug, Jinja2, itsdangerous, click, flask
Successfully installed Jinja2-3.0.3 MarkupSafe-2.0.1 Werkzeug-2.0.2 click-8.0.3 flask-2.0.2 itsdangerous-2.0.1
```

`flask` is now installed only in this `venv`, not globally. *yay*

To verify this, open a new terminal, don't activate the venv, and try to call flask. You should have an error. (of course, except if you installed flask earlier as a global dependency...)

Let's move forward in time and imagine that we developed a nice app. We want to share the list of dependencies required to dev/run/test the app. To export this list we use the command `freeze` :

```bash
(venv) $ pip3 freeze
click==8.0.3
Flask==2.0.2
itsdangerous==2.0.1
Jinja2==3.0.3
MarkupSafe==2.0.1
Werkzeug==2.0.2
```

Here we can see that by installing only `flask`, it pulled a lot of other dependencies with it.

To version this file and share it, we redirect the command to a file named `requirements.txt` :

```bash
(venv) $ pip3 freeze > requirements.txt
```

Here's an example of a real project : https://github.com/kellyjonbrazil/jc/blob/master/requirements.txt

This file, `requirements.txt` will be committed alongside your source code. But you must not commit the `venv` folder. So make sure to add it in the `.gitignore` file of your project.

Also make sure to update your requirements.txt every time you update/install a dependency. 🙃

Note : you can read a complete gitignore file here > https://www.toptal.com/developers/gitignore/api/python

To quit the `venv` :

``bash
(venv) $ deactivate
```