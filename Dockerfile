FROM python:3.8

WORKDIR /code
COPY requirements.txt .
RUN pip install -U pip && pip install -r requirements.txt

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY . .

EXPOSE 5000
CMD ["flask", "run"]
