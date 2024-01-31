FROM python:3.12-rc

RUN apt-get update

WORKDIR /workspace

# * install needed libs
COPY requirements/ requirements/
RUN pip install --upgrade pip
RUN pip3 install -r requirements/prod.txt

COPY ./src ./
CMD ["python", "./main.py"]
