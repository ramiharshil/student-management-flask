FROM python:3.6.9-alpine3.13

# Make a directory for application
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install flask
RUN pip install flask_sqlalchemy
RUN pip install flask_marshmallow

# Copy the source code
COPY . . 

EXPOSE 5002

# RUN the application
CMD ["python","app.py"]
