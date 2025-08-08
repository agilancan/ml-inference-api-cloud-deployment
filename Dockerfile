# Use a minimal Python base image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy uv files first (for caching layers)
COPY uv.lock pyproject.toml /app/

# Install uv and dependencies
RUN pip install uv
RUN uv sync --frozen --no-cache

# Copy the rest of the application code
COPY . .

# Expose the port your FastAPI app runs on
EXPOSE 8080

# Run the app using uv so it finds dependencies
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]