FROM python:3-alpine

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir --pre .

EXPOSE 8000

CMD ["python", "src/main.py"]
