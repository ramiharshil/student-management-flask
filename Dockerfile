FROM python:3.6.13-alpine3.13

# Make a directory for application
WORKDIR /app

# Install dependencies
RUN pip3 install Flask
RUN pip3 install Flask_marshmallow
RUN pip3 install SQLAlchemy
RUN pip3 install Flask-SQLAlchemy

# Copy the source code
COPY . . 

EXPOSE 5001

# RUN the application
CMD ["python","app.py"]
