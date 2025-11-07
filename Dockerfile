FROM python:3.11

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=server.py
ENV FLASK_RUN_RELOAD=true

CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]

EXPOSE 8080