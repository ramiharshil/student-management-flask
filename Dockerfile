FROM python:3
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
EXPOSE 5002
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
