FROM python:latest

WORKDIR /app-robot

COPY . .

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3"]

CMD ["robot.py"]