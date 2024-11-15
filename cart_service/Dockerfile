# Use an official Python runtime as the base image
FROM python:3.12

# Set the working directory
WORKDIR /cart_service

# Copy the requirements file into the image
COPY ../requirements.txt /cart_service/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application code into the container (from the context)
COPY ./ /cart_service/

# Expose the application port
EXPOSE 8000

# Command to run the app with --reload for development
CMD ["uvicorn", "cart_service.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

