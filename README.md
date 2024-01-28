a tiny UnCMS project 🐭
=======================

This is a tiny project which documents some core functions of [UnCMS](https://github.com/uncms-dev/uncms) and demonstrating how to make friends with UnCMS's helper models and admin classes.
This is probably the most absurdly highly-commented code you will ever read;
it's intended as a crash-course in building sites with UnCMS.

This is a companion repository for UnCMS's documentation.

Suggested reading order:

* This list
* `settings/base.py` for UnCMS-specific settings
* `tiny_project/apps/news/models.py` for how to create page content models & the most useful helper classes
* `tiny_project/apps/news/admin.py` for how to register such things
* `tiny_project/apps/news/views.py` to use RequestPageManager for fun and profit
* `tiny_project/apps/content/models.py` for an example of inline models on page content models
* `tiny_project/apps/content/admin.py` immediately after that, for how to actually register them
* `templates/base.html`

Quickstart:

```
# add your SECRET_KEY herein :)
nano tiny_project/settings/local.py
createdb tiny_project
# A minimum of 3.8 is required. Later versions should work fine.
# Shortcut for "delete venv, recreate venv, install requirements" is
# ./scripts/bootstrap.sh
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
./manage.py runserver
```
