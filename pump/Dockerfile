FROM this-stream-is-lit:base

COPY requirements.txt /usr/src/requirements.txt
RUN python3 -m venv venv
RUN venv/bin/pip install -r requirements.txt

COPY pump.py pump.py
CMD ["venv/bin/python3", "pump.py"]

