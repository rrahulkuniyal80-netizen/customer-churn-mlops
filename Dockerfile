FROM python:3.13-slim

RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

WORKDIR /main

COPY requirement.txt .

RUN pip install --no-cache-dir -r requirement.txt 

COPY . .

CMD ["python", "main.py"]
