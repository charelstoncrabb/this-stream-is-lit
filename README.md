# this-stream-is-lit
Simple asynchronous live-update streamlit app read from a Redis Streams stream

The setup uses docker-compose, so in order to run things, the docker engine needs to be installed.

There are three containers ran:
1. `pump`: this is a simple synthetic data pump that randomly generates some data and writes it to a redis stream
2. `redis`: vanilla redis instance
3. `app`: the streamlit web-app that reads from the redis stream and displays the data in real time

To build the images, you can run the top level script:
```
$ ./build-docker.sh
```

To run the demo, simply use docker compose:
```
$ docker compose up
```

The streamlit webapp is then available at http://localhost:7890 🎉
