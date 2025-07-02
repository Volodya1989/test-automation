# Makefile for test automation with Poetry & Playwright

.PHONY: setup install test report clean shell

# Initial setup: install dependencies and Playwright browsers
setup:
	poetry install
	poetry run playwright install


# Run all tests using Pytest
test:
	poetry run pytest tests/

# Run tests and generate Allure report
report:
	poetry run pytest tests/ --alluredir=allure-results
	poetry run allure serve allure-results

# Open Poetry shell
shell:
	poetry shell

# Clean up test results and reports
clean:
	rm -rf allure-results
