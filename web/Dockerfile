FROM python:3.10
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
# RUN pip install poetry && \
#     poetry config virtualenvs.create false && \
#     rm -rf .venv
COPY . /code/
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    rm -rf .venv
RUN poetry install
# CMD python run.py
CMD gunicorn --bind 0.0.0.0:8080 -w 3 run:app
# CMD uvicorn run:app --host 0.0.0.0 --port 8080 --workers 3