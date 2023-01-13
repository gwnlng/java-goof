FROM python:3.12.0a4
WORKDIR /TestCode

COPY . TestCode/
RUN pip install -r TestCode/requirements.txt

ENV AWS_CONTAINER_CREDENTIALS_RELATIVE_URI="/creds"
RUN python -u TestCode/testprint.py
