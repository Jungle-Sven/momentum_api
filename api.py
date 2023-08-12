from fastapi import FastAPI
import redis
import json

# Connect to the Redis server
redis_host = 'momentum_redis_container'  # Change this to the Redis server address if running on a different machine
redis_port = 6379         # Default Redis port
redis_db = 0              # Redis database number
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db)

app = FastAPI()

@app.get("/api/momentum")
def root():
    result = []
    #get data 
    symbols = ['BTC-USD', 'ETH-USD']
    for symbol in symbols:
        key_name = 'signal_' + symbol                
        data = redis_client.get(key_name)
        # Convert the bytes to a string
        data_str = data.decode('utf-8')
        # Convert the JSON string back to a Python data structure
        data = json.loads(data_str)

        result.append(data)

    #print(result)
    #json_str = result.to_json(orient='records')
    return {"data": result}
