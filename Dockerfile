FROM python:3.9.10-slim-buster
WORKDIR /BOT
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python3", "main.py"]