FROM python:3.11

RUN apt-get update


WORKDIR /workspace

# * install needed libs
COPY requirements/ requirements/
RUN pip install --upgrade pip
RUN pip3 install -r requirements/dev.txt

# * modify bashrc to setup custom cli
COPY .devcontainer/scripts/custom_cli.sh .devcontainer/scripts/custom_cli.sh
RUN cat .devcontainer/scripts/custom_cli.sh >> ~/.bashrc
