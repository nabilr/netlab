if [ $# -ne 3 ]
then
	echo "usage error: serverIP serverPort idx"
	exit -1
fi
idx=$3
test -e c$idx && rm c1
mkfifo c1
nc  $1 $2 < c$idx  >client$idx.log&  
eval "exec 8>c$idx"
echo -ne "U" >&8
echo -ne "S" >&8
echo -ne "ER user$idx" >&8
echo -ne "\nPASS pass$idx\n" >&8
echo -ne "CD sandbox/ftp_server_dirs/client_dir_c$idx\n" >&8
echo -ne "PWD\n" >&8
echo -ne "QUIT\n" >&8

sleep 10
echo "Basic test completed"
