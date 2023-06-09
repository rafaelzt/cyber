#!/bin/sh

export MYPATH="/goinfre/$USER/miniconda3"

echo "Installing conda"
curl -LO "https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh"
sh Miniconda3-latest-MacOSX-x86_64.sh -b -p $MYPATH

echo "Initial conda configuration"
$MYPATH/bin/conda init zsh
$MYPATH/bin/conda config --set auto_activate_base false
source ~/.zshrc

echo "Create conda environment (42AI-\$USER)"
conda create --name 42AI-$USER python=3.7 jupyter pandas pycodestyle numpy -y

conda info --envs
