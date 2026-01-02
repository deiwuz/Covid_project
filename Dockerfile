FROM python:3.14

RUN pip install uv

WORKDIR /app

COPY . .

RUN uv pip install . --system

CMD ["python", "main.py"]
