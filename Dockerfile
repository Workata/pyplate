FROM python:3.12-rc

RUN apt-get update

WORKDIR /workspace

# * install needed libs
COPY requirements/base.txt requirements/base.txt
RUN pip install --upgrade pip
RUN pip3 install -r requirements/base.txt

COPY ./src ./
CMD ["python", "./main.py"]
