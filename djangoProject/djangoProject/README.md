
```
// on your chrome console
var socket = new WebSocket('ws://localhost:8080/room/2');

socket.onmessage = function(event) {
  console.log("Received message:", event.data);
};
```
## Something needs to install:
* channels
* daphne
* redis (TBD)

## Test daphne:
```angular2html
daphne djangoProject.asgi:application --port 8000 // any port is Ok
```
