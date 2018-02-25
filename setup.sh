#Nabil Rahiman
#NYU , Abudhabi
#email: nr83@nyu.edu
#Setup script for mininet

if [ $# -ne 2 ]
then
	echo "usage error: <NUMBER_OF_CLIENTS> [client_type]"
	echo "Example: bash setup.sh 2 nc"
	echo "Example: bash setup.sh 2 ftp"
	exit -1
fi

eval "exec 1>/dev/null"
eval "exec 2>/dev/null"

test -e sandbox && rm -r sandbox
mkdir sandbox

base_dir=`echo $PWD`
echo $base_dir

cd sandbox

mkdir ftp_client_dirs
cd ftp_client_dirs
i=0
while [ $i -le $1 ]
do
	echo $PWD
	mkdir local_dir_c$i
	cd local_dir_c$i
	dd if=/dev/urandom of=local_file_client$i.txt bs=1048576 count=1
	cp $base_dir/FTPclient .
	cd ..
	i=`expr $i + 1`
done

cd ..
mkdir ftp_server_dirs
cd ftp_server_dirs
i=0
while [ $i -le $1 ]
do
	mkdir client_dir_c$i
	cd client_dir_c$i
	dd if=/dev/urandom of=server_file_client$i.txt bs=1048576 count=100
	cd ..
	i=`expr $i + 1`
done
cd ../..

test -e test.sh && rm test.sh
ln -s  test_$2.sh test.sh
