# inquisitor - Network (Cybersecurity)

This program performs ARP poisoning using specified IP and Mac addresses.
It also displays the names of files exchanged between a client and an FTP server in real time.

When the attack is stopped (CTRL+C), the ARP tables will be restored.

## Usage

Works on the Linux platform

```
usage: inquisitor.py [-h] ip_src mac_src ip_target mac_target

positional arguments:
  ip_src      IP-src
  mac_src     MAC-src
  ip_target   IP-target
  mac_target  MAC-target

optional arguments:
  -h, --help  show this help message and exit
```


## Run

```
make
```

- add all permission for ftp
  ```
  sudo chmod 777 /home/user42/Desktop/server
  sudo chmod 777 ./storage
  ```

### server

- connect to container
  ```
  make server
  ```
- check ARP table befor connection
  ```
  ip neigh
  ``` 

### client

- connect to container
  ```
  make client
  ```
- check ARP table befor connection
  ```
  arp -n
  ```

- connect to FileZilla and transfer files
  - http://localhost:5800/

  ```
  Host      : server
  Username  : ftpuser
  Password  : ftppass
  -> Quickconnect
  ```

### inquisitor

- show command
  ```
  make run
  ```

- show info
  ```
  make info
  ```
- connect to container
  ```
  make inquisitor
  ```
- execute
  ```
  ./inquisitor.py <IP-src> <MAC-src> <IP-target> <MAC-target>
  ```

