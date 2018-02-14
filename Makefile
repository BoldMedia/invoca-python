init:
	pip install pipenv --upgrade
	pipenv install --dev --skip-lock

test:
	pytest
test-watch:
	ptw

clean:
	rm -rf build dist .egg requests.egg-info

install:
	pipenv install -e .
uninstall:
	pipenv uninstall invoca
reinstall:
	$(MAKE) uninstall && $(MAKE) install

example:
	echo "\n\nCalling Examples\n" && pipenv run python examples/transactions.py

fresh-example:
	$(MAKE) reinstall && $(MAKE) example


