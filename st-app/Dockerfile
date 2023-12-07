FROM this-stream-is-list:base

COPY requirements.txt /usr/src/requirements.txt

RUN python3 -m venv venv
RUN venv/bin/pip install -r requirements.txt
CMD ["streamlit", "run", "app.py", "--port=7890"]

