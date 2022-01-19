# start from base
FROM python:3.9.1
ADD . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENV FLASK_APP=routes.py
ENV FLASK_ENV=development
EXPOSE 5001
CMD [ "flask", "run", "--host=0.0.0.0" ]
