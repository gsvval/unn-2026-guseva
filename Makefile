
.PHONY: test format format-check lint lint-fix typecheck check

test:
	uv run python -m unittest discover -s tests -v

format:
	uv run ruff format .

format-check:
	uv run ruff format --check .

lint:
	uv run ruff check .

lint-fix:
	uv run ruff check --fix .

typecheck:
	uv run mypy bot

check: format-check lint typecheck test
