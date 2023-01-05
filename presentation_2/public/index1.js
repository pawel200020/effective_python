const sio = io();

//connect to io() i  to łączy nas z serwerem z którego przyszedł ten plik nic nie trzeba podawać ww argumentach, chyba że przyszło z innego serwera to wtedy  możemy wyspecifikować jaki serwer ma być przez np url
///klient podobnie jak serwer działa na zasadziie event handlers

sio.on('connect', () => {
    console.log('connected');
});

sio.on('disconnect', () => {
    console.log('disconnected');
})