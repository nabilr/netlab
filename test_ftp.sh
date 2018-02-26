if [ $# -ne 3 ]
then
	echo "usage error: serverIP serverPort idx"
	exit -1
fi
idx=$3
test -e c$idx && rm c1
mkfifo c1
./FTPclient  $1 $2 < c1  >client$idx.log&  
eval "exec 8>c1"
echo -ne "USER user$idx\n" >&8
echo -ne "PASS pass$idx\n" >&8
echo -ne "CD sandbox/ftp_server_dirs/client_dir_c$idx\n" >&8
echo -ne "PWD\n" >&8
#echo -ne "LS\n" >&8
echo -ne "!CD sandbox/ftp_client_dirs/local_dir_c$idx\n" >&8
echo -ne "!PWD\n" >&8
#echo -ne "!LS\n" >&8
#echo -ne "GET server_file_client$idx.txt\n" >&8
#echo -ne "PUT server_file_client$idx.txt\n" >&8
echo -ne "QUIT\n" >&8

sleep 10
echo "Basic test completed"
