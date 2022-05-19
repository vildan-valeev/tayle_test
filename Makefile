include .env

.SILENT:

.DEFAULT_GOAL := help

ENV_FILE = ./.env

export $(shell sed 's/=.*//' .env)

_APP = app
_BOT = bot

help:
	@echo "Base commands"
	@echo "\tmake deploy\t-> \trunning project"
	@echo "\tmake development\t-> \trunning project (all services in docker-compose) in development env"
	@echo "\tmake lints\t-> \trunning project (all services in docker-compose) in develop env"
	@echo "\tmake tests\t-> \trunning project (all services in docker-compose) in develop env"

	@echo ""
	@echo "For Django App:"
	@echo "\tmake $(_APP)_run\t-> \trunning Django application in local env"
	@echo "\tmake $(_APP)_test\t-> \trunning test for Django application in local env"
	@echo "\tmake $(_APP)_lint\t-> \trunning lints for Django application in local env"
	@echo ""

	@echo "For Aiohttp App:"
	@echo "\tmake $(_BOT)_run\t-> \trunning Trade Bot application in local env"
	@echo "\tmake $(_BOT)_test\t-> \trunning tests for Trade Bot"
	@echo "\tmake $(_BOT)_lint\t-> \trunning lints for Trade Bot"

development:
	sh scripts/development.sh



lints: bot_lint app_lint
tests: bot_test app_test


bot_run:
	$(MAKE) --directory=$(_BOT) bot_run
.PHONY: bot

bot_lint:
	sh scripts/lint_bot.sh

bot_test:
	sh scripts/test_bot.sh


app_run:
	$(MAKE) --directory=$(_APP) app_run
.PHONY: app

app_lint:
	sh scripts/lint_app.sh

app_test:
	sh scripts/test_app.sh

deploy:
	sh scripts/deploy.sh
