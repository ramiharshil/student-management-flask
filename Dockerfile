FROM python:3.7.10-alpine3.13

# Make a directory for application
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the source code
COPY . /app 

EXPOSE 5002

# RUN the application
CMD ["python","app.py"]
