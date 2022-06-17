SCRIPT=`realpath -s $0`
SCRIPTPATH=`dirname $SCRIPT`
# Execute install script with sudo previledges
pkexec sh $SCRIPTPATH/install.sh

