import logging
import os
import time

from numpy.random import randint, normal
import randomname
import redis


from common import MyDataModel

REDIS_HOST = os.getenv("REDIS_HOST")
RSTREAM_ID = os.getenv("RSTREAM_ID")

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def main():
    r = redis.Redis(host=REDIS_HOST)
    int_tracker = 0
    float_tracker = 0.

    while True:
        int_tracker += randint(-1,2)
        float_tracker += normal()
        
        new_observation = MyDataModel(
            my_int=int_tracker,
            my_float=float_tracker,
            my_str=randomname.generate(),
        )

        r.xadd(RSTREAM_ID, new_observation.model_dump())
        logger.info(f"added new observation {new_observation} to redis stream {RSTREAM_ID}")
        time.sleep(1)



if __name__ == "__main__":
    main()

