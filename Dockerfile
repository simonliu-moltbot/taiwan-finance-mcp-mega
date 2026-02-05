FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Set PYTHONPATH to root of src
ENV PYTHONPATH=/app/src

EXPOSE 8000

# Run the self-contained main.py
ENTRYPOINT ["python", "src/main.py"]
CMD ["--mode", "http", "--port", "8000"]
