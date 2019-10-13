import asyncio
import json
import logging
import websockets
import requests
import threading

logging.basicConfig()

STATE = json.loads(requests.get("http://127.0.0.1:5000/Simon/generateGame").text)

USERS = set()

TIMER = {"value" : 0}

def state_event():
    STATE["type"] = "state"
    return json.dumps(STATE)

def users_event():
    return json.dumps({"type": "users", "count": len(USERS)})

def timer_event():
    return json.dumps({"type": "timer", **TIMER})


async def notify_state():
    if USERS:  # asyncio.wait doesn't accept an empty list
        message = state_event()
        await asyncio.wait([user.send(message) for user in USERS])


async def notify_users():
    if USERS:  # asyncio.wait doesn't accept an empty list
        message = users_event()
        await asyncio.wait([user.send(message) for user in USERS])

async def notify_timer():
    if USERS:  # asyncio.wait doesn't accept an empty list
        message = timer_event()
        await asyncio.wait([user.send(message) for user in USERS])
async def notify_subState():
    if USERS:  # asyncio.wait doesn't accept an empty list
        subSequence = list()
        i = 1
        while i <= STATE["round"]: 
            subSequence.append(STATE["sequence"][i])
            i += 1
        message = {"type": "round", "sequence" : subSequence}
        await asyncio.wait([user.send(json.dumps(message)) for user in USERS])

async def register(websocket):
    USERS.add(websocket)
    await notify_users()


async def unregister(websocket):
    USERS.remove(websocket)
    await notify_users()

@asyncio.coroutine
async def timerTo0():
    TIMER["value"] = 10
    while TIMER["value"] >= 0:
        await notify_timer()
        TIMER["value"] -= 1
        await asyncio.sleep(1)
    STATE["round"] += 1
    await notify_state()
    await notify_subState()

def loop_in_thread(loop):
    if STATE["round"] > 10:
        return
    asyncio.set_event_loop(loop)
    loop.run_until_complete(timerTo0())

async def counter(websocket, path):
    # register(websocket) sends user_event() to websocket
    await register(websocket)
    try:
        await websocket.send(state_event())
        async for message in websocket:
            data = json.loads(message)
            if data["action"] == "start":
                await notify_subState()
            elif data["action"] == "play":
                    loop = asyncio.get_event_loop()
                    task = threading.Thread(target=loop_in_thread, args=(loop,))
                    task.start()
            else:
                logging.error("unsupported event: {}", data)
                
    finally:
        await unregister(websocket)

start_server = websockets.serve(counter, "localhost", 6789)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()