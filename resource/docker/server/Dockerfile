FROM python:3.10

WORKDIR /app

COPY ./resource/python/req.txt /app/req.txt

RUN pip install --no-cache-dir -r /app/req.txt

COPY ./server /app

CMD ["python", "main.py", "-rt", "dev"]