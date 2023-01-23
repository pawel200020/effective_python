const sio = io();

//connect to io() i  to łączy nas z serwerem z którego przyszedł ten plik nic nie trzeba podawać ww argumentach, chyba że przyszło z innego serwera to wtedy  możemy wyspecifikować jaki serwer ma być przez np url
///klient podobnie jak serwer działa na zasadziie event handlers

sio.on('connect', () => {
    console.log('connected');
    sio.emit('sum', { numbers: [2, 3] }, (result) => {
        console.log(result);
    }); //jeśli sio ma 3 argument to chce uzyskać response od servera
});
sio.on('mult', (data, cb) => {
        const result = data.nums[0] * data.nums[1];
        console.log(result);
        cb(result);
    })
    //odbijanie piłeczki
    // sio.on('sum_result', (data) => {
    //     console.log(data);
    // });
    // sio.on('connect', () => {
    //     console.log('connected');
    //     sio.emit('sum', { numbers: [2, 3] }); //arg (event name, data dla servera które chcemy wysłać(JSON))
    // });



sio.on('disconnect', () => {
    console.log('disconnected');
})

sio.on('client_count', (count) => {
    console.log(count + " connected clients")
})