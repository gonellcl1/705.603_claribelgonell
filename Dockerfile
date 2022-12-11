FROM python:3.8
COPY . ./
RUN pip3 install -r requirements.txt
RUN [ "python", "-c", "import sage_data_client" ]
CMD ["model.py"]
ENTRYPOINT ["python"]
