#Nabil Rahiman
#NYU, Abudhabi
#email:nr83@nyu.edu
#18/Feb/2018


if [ $# -ne 3 ]
then
	echo "usage error: serverIP serverPort  numberOfClients"
	exit -1
fi

i=1
while [ $i -le $3 ]
do
	test -e c$i && rm c$i
	i=`expr $i + 1`
done

i=1
while [ $i -le $3 ]
do
	mkfifo c$i
	i=`expr $i + 1`
done

i=1
while [ $i -le $3 ]
do
	nc  $1 $2 < c$i&
	i=`expr $i + 1`
done

i=1
while [ $i -le $3 ]
do
	t=`expr 4 + $i`
	eval "exec $t>c$i"
	i=`expr $i + 1`
done


i=1
fd=5
while [ $i -le $3 ]
do
	typec=`expr $i % 3`
	case $typec in
		0)
			echo -ne "USER user1\n" >&$fd
			;;
		1)
			echo -ne "USER user2\nPASS pass2\n" >&$fd
		
			;;
		2)
			echo -ne "USER user3\nPASS pass3\nPWD\nLS\n" >&$fd
			;;
		*)
			echo -ne "something wron\n"
			;;

	esac
	i=`expr $i + 1`
	fd=`expr $fd + 1`
done

i=1
fd=5
while [ $i -le $3 ]
do
	typec=`expr $i % 3`
	case $typec in
		0)
			echo -ne "PASS 1" >&$fd
			;;
		1)
			echo -ne "LS\nPWD\nLS\nPWD\n" >&$fd
		
			;;
		2)
			echo -ne "PWD\nLS\nPWD\nLS\nPWD\nLS\nPWD\n" >&$fd
		
			;;
		*)
			echo -ne "something wron\n"
			;;
	esac
	i=`expr $i + 1`
	fd=`expr $fd + 1`
done
echo "Basic test completed"
