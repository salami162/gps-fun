# we use the pipefail option below, which is bash specific.
SHELL := /bin/bash

SERVICE_NAME=www-connect-conf

.PHONY: clean
clean:
	find . -name "*.pyc" -delete
