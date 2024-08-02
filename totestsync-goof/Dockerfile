FROM python:3.13.0b4
WORKDIR /TestCode

COPY . TestCode/
RUN pip install -r TestCode/requirements.txt

ENV AWS_CONTAINER_CREDENTIALS_RELATIVE_URI="/creds"
RUN python -u TestCode/testprint.py
