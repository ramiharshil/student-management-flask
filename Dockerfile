FROM python:3.6.9-lpine3.13

# Make a directory for application
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the source code
COPY . . 

EXPOSE 5002

# RUN the application
CMD ["python","app.py"]
