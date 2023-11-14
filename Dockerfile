# Dockerfile, Image, Container

#WORKDIR /usr/src/app

FROM python:3.8.12

ADD ./src/driver.py .

COPY  ./src/add_gui.py ./src/bnc_gui.py ./src/defaults.py ./src/expense.py ./src/functions.py ./src/parser.py ./src/rep_gui.py .

RUN pip install SQLAlchemy==1.4.29

CMD ["python", "./driver.py"]
