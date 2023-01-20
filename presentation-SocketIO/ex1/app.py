import socketio

sio = socketio.Server() #mamy dwie możliwości utorzenia serwera
app = socketio.WSGIApp(sio,static_files={
    '/': './public/'
}) #web server hostujący aplikacje
#możemy hostować static files podając ścieżki routingu i dostępu


#pobiera 2 argumenty sid - sesion ID bardzo ważne jest przypisane do klienta który się łączy, dict który zawiera szczegóły requesta klienta cookies, errors itd you can preform auth and autorization
@sio.event
def connect(sid, environ): #args
    print(sid,'connected')

@sio.event
def disconnect(sid):
    print(sid,'disconnect')
