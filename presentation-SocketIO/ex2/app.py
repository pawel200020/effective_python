import socketio

sio = socketio.Server()
app = socketio.WSGIApp(sio,static_files={
    '/': './public/'
})

@sio.event
def connect(sid, environ): #args
    print(sid,'connected')

@sio.event
def disconnect(sid):
    print(sid,'disconnect')

#odbijanie "piłeczki"
@sio.event
def sum(sid,data):
    result = data['numbers'][0]+data['numbers'][1]
    print(sid," ",result)
    sio.emit('sum_result',{'result': result},to=sid) #ważne przy kliencie nie trzeba było podawać tego bo on pamięta skąd przyszło, natomiast tutaj serwer obsługuje dużo żądań stąd nie wie gdzie ma wysłać dlatego trzeba podać sid połączenia

