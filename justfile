# list all available commands
default:
    just --list

# clean up all temporary files
clean:
    find {{ justfile_directory() }} -type d -name '.venv' -exec rm -rf {} +
    find {{ justfile_directory() }} -type d -name '.pytest_cache' -exec rm -rf {} +
    find {{ justfile_directory() }} -type d -name '__pycache__' -exec rm -rf {} +
    find {{ justfile_directory() }} -type f -name '*.bin' -exec rm -rf {} +
    find {{ justfile_directory() }} -type f -name '*.html' -exec rm -rf {} +
    find {{ justfile_directory() }} -type f -name '*.csv' -exec rm -rf {} +
    find {{ justfile_directory() }} -type d -name '.mypy_cache' -exec rm -rf {} +
    find {{ justfile_directory() }} -type d -name '.ruff_cache' -exec rm -rf {} +
    find {{ justfile_directory() }} -type d -name '.ipynb_checkpoints' -exec rm -rf {} +
    find {{ justfile_directory() }} -type d -name 'htmlcov' -exec rm -rf {} +

# install all required dependencies
configure:
    poetry install --sync

# run this if you want to upgrade the dependencies to their latest compatible version from PyPI
upgrade-dependencies:
    poetry upgrade --latest

# run this if you want to update the dependencies respecting the constraints from the `pyproject.toml`
update-dependencies:
    poetry lock

# run this if you want to re-lock the dependencies
lock-dependencies:
    poetry lock --no-update

apis_repository := "git@github.com:volur-ai/apis.git"
apis_repository_dir := `mktemp -d`

# generate code from APIs declarations
generate:
    git clone {{ apis_repository }} {{ apis_repository_dir }}
    cd {{ apis_repository_dir }} && buf generate --include-imports --include-wkt
    rm -rf gen
    cp -r {{ apis_repository_dir }}/gen/python gen

# fix auto-fixable issues
fix: configure
    poetry run ruff format src tests scripts && \
    poetry run ruff check --fix --unsafe-fixes src tests scripts

# validate code and configuration
validate: configure
    poetry check --lock && \
    poetry run ruff format --check src tests scripts *.ipynb && \
    poetry run ruff check src tests scripts *.ipynb && \
    poetry run mypy src tests scripts

test_args := ""

# run tests
test:
    poetry run pytest tests {{ test_args }}

configure-docs:
    poetry install --only docs --sync

# build documentation
build-docs:
    poetry run mkdocs build --strict

# serve documentation
serve-docs:
    poetry run mkdocs serve

# run CI locally
ci: validate test build-docs
