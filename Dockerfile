FROM python:3.8
COPY . ./
RUN pip3 install -r requirements.txt
RUN [ "python", "-c", "import nltk; nltk.download('all')" ]
CMD ["3_NLTK_ClaribelGonell.py"]
ENTRYPOINT ["python"]
