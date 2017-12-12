# django-clean-project
- **My default django project layout**

### Requirements
- **Clone the repository** - <i>(**Will require a virtualenvwrapper setup**)</i>
- **Simply create a a virtualenv folder and activate**<br>
`mkvirtualenv project-name`<br>
`workon project-name`<br>

- **Add environmental variables in postactivate script, directory located:**<br>
**`~/.virtualenvs/project-name/bin/postactivate`**<br>
`export DJANGO_SETTINGS_MODULE=config.settings.local`<br>
`export PYTHONPATH=$PYTHONPATH:$HOME/Project/project-name/config`<br>
`export LOCAL_SECRET_KEY='DJANGOPASSWORDHERE`<br>
`export DATABASE_PASSWORD='SETYOURPASSWORDHERE`<br>

- **Pip install**
`pip install -r requirements.txt`

- **Run `127.0.0.1:8000` locally to test it out!**
