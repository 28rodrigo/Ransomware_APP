#instalar xtrlock para bloquear teclado e rato
#apt install xtrlock
#obter o path dos ficheiros
SCRIPT=`realpath -s $0`
SCRIPTPATH=`dirname $SCRIPT`
echo $SCRIPTPATH
# configurar o servico para bloquear o boot

#copiar código a correr no boot para a pasta /opt
chmod +x $SCRIPTPATH/inout
cp $SCRIPTPATH/boot_block.py /opt/
cp $SCRIPTPATH/inout /opt/
echo 'Done 1'
#copiar servico para a pasta especifica
cp $SCRIPTPATH/block.service /etc/systemd/system/
#ativar o servico
systemctl daemon-reload
systemctl enable block.service
echo 'Done 2'


#chmod +x $SCRIPTPATH/startscript.sh
#copiar script para init.d/
#cp $SCRIPTPATH/startscript.sh /etc/init.d/


#cd /etc/rc2.d/
#fazer um link para o script, para ser executado no inicio.
#ln /etc/init.d/startscript.sh S01startscript.sh -s
#copiar o script python para a home

cp $SCRIPTPATH/block.py /opt/
echo 'Done 3'

