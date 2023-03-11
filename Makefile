VENV_DIR = venv
PROJECT_DIR = backend
DJANGO_MANAGE = $(PROJECT_DIR)/manage.py
DJANGO_DB = $(PROJECT_DIR)/db.sqlite3
DEFAULT_SETTINGS = export DJANGO_SETTINGS_MODULE=core.settings &&
CONTEXT = export DJANGO_SQLITE_PATH=$(DJANGO_DB) && $(DEFAULT_SETTINGS)

ifeq ($(OS), Windows_NT)
	VENV = . $(VENV_DIR)/Scripts/activate &&
else
	VENV = . $(VENV_DIR)/bin/activate &&
endif

migrations:
	$(VENV) $(CONTEXT) python $(DJANGO_MANAGE) makemigrations

migrate:
	$(VENV) $(CONTEXT) python $(DJANGO_MANAGE) migrate

runserver:
	$(VENV) $(CONTEXT) python $(DJANGO_MANAGE) runserver 0.0.0.0:8000
