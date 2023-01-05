import socketio
#callbacks
#broadcast
sio = socketio.Server() 
app = socketio.WSGIApp(sio,static_files={
    '/': './public/'
})
client_count = 0

#przykład callback w drugą stronę - tutaj server wywołuje event i oczekuje odpowiedzi
#zadziała niezależnie od connect event
#raczej rzadko występuje

#drugi sposób
def cb(data):
    print('this came from client: ',data)

def task(sid):
    sio.sleep(3)
    print('bg task')
    #sio.emit('mult',{'nums': [5,9]},callback=cb)
    #my coś chcemy od klienta
    result = sio.call('mult',{'nums': [5,9]},to=sid)
    print(result)


@sio.event
def connect(sid, environ): #args
    global client_count
    client_count+=1
    print(sid,'connected')
    sio.start_background_task(task, sid)
    #broadcast do wszystkich
    sio.emit('client_count',client_count)

@sio.event
def disconnect(sid):
    global client_count
    client_count-=1
    print(sid,'disconnect')
    #broadcast
    sio.emit('client_count',client_count)


#callbacks - gdy klient wyśle jakiś request i oczekuje że server zwróci mu coś
#klient chce od nast
@sio.event
def sum(sid,data):
    result = data['numbers'][0]+data['numbers'][1]
    print(sid," this is what was send by server and received from client: ",result)
    return result #callback
    pass
