FROM kennethreitz/pipenv as requirements

RUN pipenv install && pipenv lock --requirements > /requirements.txt

FROM python:3.6.7-alpine3.7

COPY --from=requirements /requirements.txt requirements.txt

RUN cat requirements.txt && pip install -r requirements.txt

ADD wait.py wait.py

CMD ["python", "wait.py"]