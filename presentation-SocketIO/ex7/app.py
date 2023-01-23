import socketio

sio = socketio.Server() #mamy dwie możliwości utorzenia serwera
app = socketio.WSGIApp(sio,static_files={
    '/': './public/'
})
client_count = 0
#możemy hostować static files podając ścieżki routingu i dostępu


#pobiera 2 argumenty sid - sesion ID bardzo ważne jest przypisane do klienta który się łączy, dict który zawiera szczegóły requesta klienta cookies, errors itd you can preform auth and autorization
# @sio.event
# def connect(sid, environ): #args
#     print(sid,'connected')

#przykład callback w drugą stronę - tutaj server wywołuje event i oczekuje odpowiedzi
#zadziała niezależnie od connect event
#raczej rzadko występuje
def cb(data):
    print('this came from client: ',data)

def task(sid):
    sio.sleep(3)
    print('bg task')
    #sio.emit('mult',{'nums': [5,9]},callback=cb)
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
    sio.emit('client_count',client_count)
    


# #odbijanie "piłeczki"
# @sio.event
# def sum(sid,data):
#     result = data['numbers'][0]+data['numbers'][1]
#     print(sid," ",result)
#     sio.emit('sum_result',{'result': result},to=sid) #ważne przy kliencie nie trzeba było podawać tego bo on pamięta skąd przyszło, natomiast tutaj serwer obsługuje dużo żądań stąd nie wie gdzie ma wysłać dlatego trzeba podać sid połączenia
#     pass


#callbacks - gdy klient wyśle jakiś request i oczekuje że server zwróci mu coś
@sio.event
def sum(sid,data):
    result = data['numbers'][0]+data['numbers'][1]
    print(sid," this is what was send by server and received from client: ",result)
    return result #callback
    pass
