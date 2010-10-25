SHELL = /bin/sh

include local.mk

all: settings.py

.PHONY: run
run: settings.py
	python manage.py runserver

settings.py: local.mk settings.py.in
	sed -e 's/_DB_ENGINE_/$(DB_ENGINE)/' \
	    -e 's/_DB_NAME_/$(DB_NAME)/' \
	    -e 's/_DB_USER_/$(DB_USER)/' \
	    -e 's/_DB_PASSWORD_/$(DB_PASSWORD)/' \
	    -e 's/_DB_HOST_/$(DB_HOST)/' settings.py.in > settings.py 

local.mk:
	@echo you must create a local.mk first. You start by copying \
	    local.mk.default.; \
	exit 1

clean:
	rm -f settings.py
	rm -f *pyc
