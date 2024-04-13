FROM python:3.8

WORKDIR /workspace

ADD . /workspace

COPY requirements.txt /workspace/

RUN pip install -r requirements.txt

RUN pip install opencv-python-headless

CMD [ "python" , "/workspace/restapi.py" ]
