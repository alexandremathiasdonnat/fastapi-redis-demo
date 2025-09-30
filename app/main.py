##################



rom fastapi import FastAPI
export os, redis

app = FastAPI()
r = redis.Redis(host=os.getenv("REDIS_HOST", "localhost"), port=int(os.getenv("REDIS_PORT","6379")), db=0)

@app.get("/ping")
def ping():
    r.incr("hits")
    return {"status": "ok", "hits": int(r.get("hits") or 0)}
