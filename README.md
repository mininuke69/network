# Network

## purpose
 Network (temp.name) is a library designed to simplify sockets

## how to install
 to install
 1. download as zip
 2. extract
 3. place the `network.py` in the working directory
 4. to import in your project, use `import network`

## documentation
 start by importing `network` into your project by using `import network`
 there are 2 classes, which are
 - `network.Server()` for servers
 - `network.Client()` for clients

  ### `network.Server()`

  when instantiated, creates a new AF_INET socket

  #### `Server.Create(port)`
  makes and binds a new server <br>
  returns 
  - `self.ip` (str) local ipv4 address 
  - `self.port` (int) port used for new server
  - `self.addr` (tuple) IP, port in tuple `('127.0.0.1', 6969)`
  - `self.hostname` (str) name of the current host `'DESKTOP-2T53H3I'`

  #### `Server.Start()`
  starts (activates) the server, returns `None`
  #### `Server.Stop()`
  stops (deactivates) the server, returns `None`
  #### `Server.AcceptConn()`
  waits untill new connection is found, then accepts it. <br>
  returns the found connection as a `socket.socket`
  #### `Server.Send(data, connection)`
  takes:
  - `data`, a string, which is the data you want to send
  - `connection`, a `socket.socket` object where you want to send the data to.

  returns the length of the sent data as an `int`
  #### `Server.Recv(buffer, connection)`
  waits  untill there is data from the `socket.socket`, then receives it <br>
  takes:
  - `buffer`, an `int`, representing the max length of the message to be received. the longer, the slower it will receive
  - `connection`, a `socket.socket` object, which is the socket you want to receive data from
  
  returns
  - received data as a `str`
  ### `network.Client`
  class to be used as client.
  #### `Client.Connect(addr)`
  connects to a server. `addr` has to be a tuple of the ipv4 address and port. for example `('127.0.0.1', 6969)`. this has to be a valid `network.Server()` server
  #### `Client.Send(data)`
  sends a string, encoded as utf-8, to the currenly connected server. returns the amount of bytes sent
  #### `Client.Recv(buffer)`
  waits untill there is data to receive, then receives and returns the data. <br>`buffer` is the max length of the received data. if it is any longer, the data gets cut off there. returns the received data as a string.