FROM this-stream-is-lit:base

COPY requirements.txt requirements.txt
RUN python3 -m venv venv
RUN venv/bin/pip install -r requirements.txt

COPY app.py app.py
COPY redis_wrapper.py redis_wrapper.py
CMD ["venv/bin/streamlit", "run", "app.py", "--server.port=7890"]

