FROM python:3.8.2-slim

RUN mkdir /vampi
#RUN apk --update add bash nano

ENV vulnerable=1
ENV tokentimetolive=600

COPY . /vampi
WORKDIR /vampi

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py"]
