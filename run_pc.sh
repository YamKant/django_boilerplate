export POSTGRES_NAME=postgres
export POSTGRES_USER=yamkim
export POSTGRES_PASSWORD=postgres
export POSTGRES_HOST=localhost

# ENV FILE
export ENV_DEBUG_MODE=1

# RUN COMMAND
source .venv/bin/activate
code/manage.py runserver 0.0.0.0:8000
