import json
import os

import pandas
import redis.asyncio as redis

from common import MyDataModel

REDIS_HOST = os.getenv("REDIS_HOST")
RSTREAM_ID = os.getenv("RSTREAM_ID")



class RedisStreamReader:
    """
    Thin redis client wrapper for reading from a single stream 
    
    """
    def __init__(self):
        self.redis_client = redis.StrictRedis(
            host=REDIS_HOST,
            port=6379,
            decode_responses=True
        )
        self.last_read = 0

    async def read_most_recent(self, n: int = 1_000) -> pandas.DataFrame:
        """
        Wrapper around redis client XREVRANGE for a single
        stream that processes and returns as dataframe
        
        """
        # Read from Redis Stream
        stream_data = await self.redis_client.xrevrange(
            name=RSTREAM_ID,
            count=n,
        )

        # Process timestamps and observations into lists
        timestamps = []
        observations = []
        for (obs_id, obs_data) in stream_data:

            # Truncate trailing "-0", "-1", ...
            #   used by redis Streams to avoid collisions
            #   of stream items added at the same timestamp ⏰
            timestamps.append(
                float(obs_id.split("-")[0])/1.e12
            )
            
            # Using MyDataModel conveniently validates the
            #   data returned by XREAD and converts into a 
            #   dict with all the correct data types 👍
            observations.append(
                MyDataModel.model_validate(obs_data).model_dump()
            )

        # Set last-observed so next time only get new data
        self.last_read = timestamps[-1]
        
        # Compile data into a dataframe
        return pandas.concat([
            pandas.DataFrame(timestamps, columns=["timestamp"]),
            pandas.DataFrame(observations, columns=list(MyDataModel.model_fields.keys())),
        ], axis=1)
        
