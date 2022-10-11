FROM python:3.8
COPY . ./
RUN pip3 install -r requirements.txt
CMD ["3_NLTK_ClaribelGonell.py"]
ENTRYPOINT ["python"]