HOST="pi-zero"
INSTALL_DIR="~/pyled"

ssh $HOST "rm -rf $INSTALL_DIR && mkdir -p $INSTALL_DIR"
scp -r remote/* $HOST:$INSTALL_DIR