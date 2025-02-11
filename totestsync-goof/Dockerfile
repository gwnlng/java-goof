FROM python:3.13.2
WORKDIR /TestCode

COPY . TestCode/
RUN pip install -r TestCode/requirements.txt

ENV AWS_CONTAINER_CREDENTIALS_RELATIVE_URI="/creds"
RUN python -u TestCode/testprint.py
