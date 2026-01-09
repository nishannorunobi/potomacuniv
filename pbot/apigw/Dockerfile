# Use a slim, stable Python image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Install dependencies first (leverages Docker caching)
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Create a non-root user for security
RUN adduser --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# Copy the application code
COPY . .

# Run the FastAPI app using the official CLI
# It automatically chooses the best production settings
#CMD ["fastapi", "run", "backend.py", "--port", "8000"]

CMD ["uvicorn", "backend:app", "--host", "0.0.0.0", "--port", "8000"]
