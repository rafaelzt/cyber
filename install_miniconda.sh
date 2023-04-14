#!/bin/bash

export MYPATH="$HOME/miniconda3"
CHECK_SHELL=$(cat /etc/passwd | grep $USER | grep bash | wc -l)

echo "Installing conda"
if [[ $OSTYPE -eq 'linux-gnu' ]]; then
  URL_SCRIPT="https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh"
else
  URL_SCRIPT="https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh"
fi

if [[ $CHECK_SHELL -eq 1 ]]; then
  SHELL_FILE="$HOME/.bashrc" 
else
  SHELL_FILE="$HOME/.zshrc" 
fi

curl -L $URL_SCRIPT -o ./Miniconda3-latest-x86_64.sh
sleep 5

sh Miniconda3-latest-x86_64.sh -b -p $MYPATH

echo "Initial conda configuration"
$MYPATH/bin/conda init $(echo $SHELL | cut -d "/" -f 3)
$MYPATH/bin/conda config --set auto_activate_base false
echo -e "Reload $SHELL_FILE"
source $SHELL_FILE 

echo -e "Create conda environment (42AI-$USER)"
$MYPATH/bin/conda create --name 42AI-$USER python=3.7 jupyter pandas pycodestyle numpy -y

$MYPATH/bin/conda info --envs

echo "alias conda_act=\"conda activate 42AI-$USER\"" >> $SHELL_FILE
echo "alias conda_deact=\"conda deactivate\"" >> $SHELL_FILE

source $SHELL_FILE 
rm -f Miniconda3-latest-x86_64.sh
