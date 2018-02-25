# netlab

mininet@mininet-vm:~/sanbox$ bash setup.sh
usage error: <NUMBER_OF_CLIENTS> [client_type]
Example: bash setup.sh 2 nc
Example: bash setup.sh 2 ftp
mininet@mininet-vm:~/sanbox$ bash setup.sh 2 nc
mininet@mininet-vm:~/sanbox$ sudo python run.py
creating network topology[ftp server and 2 clients]
Please vereify the client[id].log
server is running
('clients are connected:', [26715, 26716])
mininet@mininet-vm:~/sanbox$ cat client1.log
Hello from server
331 User name okay, need password
230 User logged in, proceed
200 Command OK
/home/mininet/sanbox/sandbox/ftp_server_dirs/client_dir_c1
221 Service closing control connection. Logged out if appropriate.
mininet@mininet-vm:~/sanbox$ cat client2.log
Hello from server
331 User name okay, need password
230 User logged in, proceed
200 Command OK
/home/mininet/sanbox/sandbox/ftp_server_dirs/client_dir_c2
221 Service closing control connection. Logged out if appropriate.





mininet@mininet-vm:~/sanbox$ bash setup.sh 2 ftp
mininet@mininet-vm:~/sanbox$ sudo python run.py
creating network topology[ftp server and 2 clients]
Please vereify the client[id].log
server is running
('clients are connected:', [27087, 27089])
mininet@mininet-vm:~/sanbox$ cat client1.log
Hello from server
ftp> USER user1
331 User name okay, need password
ftp> PASS pass1
230 User logged in, proceed
ftp> CD sandbox/ftp_server_dirs/client_dir_c1
200 Command OK
ftp> PWD
/home/mininet/sanbox/sandbox/ftp_server_dirs/client_dir_c1
ftp> !CD sandbox/ftp_client_dirs/local_dir_c1
ftp> !PWD
/home/mininet/sanbox/sandbox/ftp_client_dirs/local_dir_c1
ftp> QUIT
221 Service closing control connection. Logged out if appropriate.
mininet@mininet-vm:~/sanbox$ cat client2.log
Hello from server
ftp> USER user2
331 User name okay, need password
ftp> PASS pass2
230 User logged in, proceed
ftp> CD sandbox/ftp_server_dirs/client_dir_c2
200 Command OK
ftp> PWD
/home/mininet/sanbox/sandbox/ftp_server_dirs/client_dir_c2
ftp> !CD sandbox/ftp_client_dirs/local_dir_c2
ftp> !PWD
/home/mininet/sanbox/sandbox/ftp_client_dirs/local_dir_c2
ftp> QUIT
221 Service closing control connection. Logged out if appropriate.

