# Makefile for test automation with Poetry & Playwright

.PHONY: setup install test test-ui debug report allure-report clean clean-allure shell

setup:
	poetry install
	poetry run playwright install

generate-report:
	@if ! command -v allure >/dev/null 2>&1; then \
		echo "❌ Allure CLI not found. Install it via: brew install allure"; \
		exit 1; \
	fi
	poetry run allure generate allure-results --clean -o allure-report
	open allure-report/index.html


# Run all tests
test:
	poetry run pytest tests/

# Run UI tests with visible browser and slow motion
test-ui:
	@echo "Running tests in Poetry environment"
	rm -rf allure-results allure-report*
	poetry run pytest tests/ui \
		--headed \
#		--slowmo=200 \
		--video=retain-on-failure \
		--alluredir=allure-results


#	make generate-report


# Debug mode (verbose, slow motion, headed)
debug-ui:
	poetry run pytest tests/ui \
	--headed \
	--slowmo=300 \
	--capture=tee-sys \
	--log-cli-level=INFO \
	--tracing=retain-on-failure


# Run tests and generate + open timestamped Allure report
report:
	rm -rf allure-report*
	poetry run pytest tests/ --alluredir=allure-results
	@timestamp=$$(date +"%Y%m%d-%H%M%S"); \
	poetry run allure generate allure-results --clean -o allure-report-$$timestamp && \
	open allure-report-$$timestamp/index.html

# Just generate and open a report from existing results
allure-report:
	@timestamp=$$(date +"%Y%m%d-%H%M%S"); \
	poetry run allure generate allure-results --clean -o allure-report-$$timestamp && \
	open allure-report-$$timestamp/index.html

# Clean reports
clean:
	rm -rf allure-results allure-report* test-results

clean-allure: clean

# Open Poetry shell
shell:
	poetry shell
