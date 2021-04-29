FROM python:alpine3.7
COPY . /app
WORKDIR /app
RUN pip3 install Flask
RUN pip3 install Flask_marshmallow
RUN pip3 install SQLAlchemy
RUN pip3 install Flask-SQLAlchemy
EXPOSE 5002
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
