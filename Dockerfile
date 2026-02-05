FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Set PYTHONPATH to include src
ENV PYTHONPATH=/app/src

EXPOSE 8000

# Reverted to modular entry point
ENTRYPOINT ["python", "src/taiwan_finance_mcp_mega/server.py"]
CMD ["--mode", "http", "--port", "8000"]
