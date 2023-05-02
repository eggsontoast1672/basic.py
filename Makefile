VENVCMD = virtualenv
VENVDIR = venv
PYTHON = $(VENV)/bin/python
SRCDIR = basic

run: $(VENVDIR)
	$(PYTHON) $(SRCDIR)

venv:
	$(VENVCMD) $(VENVDIR)
