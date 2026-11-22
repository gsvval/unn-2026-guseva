
FROM python:3.14-alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install --no-cache-dir python-dotenv

COPY bot ./bot

CMD ["python", "-m", "bot"]
