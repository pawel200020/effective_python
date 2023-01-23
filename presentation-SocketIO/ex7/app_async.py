import socketio

sio = socketio.AsyncServer(async_mode='asgi') 
app = socketio.ASGIApp(sio,static_files={ #standard do komuniacji przy async io
    '/': './public/'
})

@sio.event
async def connect(sid, environ): #event handler muszą być async
    print(sid,'connected')
    pass

@sio.event
async def sum(sid,data):
    result = data['numbers'][0]+data['numbers'][1]
    print(sid," ",result)
    await sio.emit('sum_result',{'result': result},to=sid)
    pass

@sio.event
async def disconnect(sid):
    print(sid,'disconnect')
    pass
#pip install "uvicorn[standard]" - async support
# uvicorn app_async:app