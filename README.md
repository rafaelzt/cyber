# Exercise 00
Using conda to install python version 3.7.x

## Create Env Var to change conda folder
´´´
export MYPATH="/goinfre/$USER/miniconda3"
´´´

## Download and Install conda
### Mac
´´´
curl -LO "https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh"
sh Miniconda3-latest-MacOSX-x86_64.sh -b -p $MYPATH
´´´
### Linux
´´´
curl -LO "https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh"
sh Miniconda3-latest-Linux-x86_64.sh -b -p $MYPATH
´´´

## Initial conda configuration
### ZSH
´´´
$MYPATH/bin/conda init zsh
$MYPATH/bin/conda config --set auto_activate_base false
source ~/.zshrc
´´´

### BASH
´´´
$MYPATH/bin/conda init bash
$MYPATH/bin/conda config --set auto_activate_base false
source ~/.bash_profile
´´´

## Create and environment
´´´
conda create --name 42AI-$USER python=3.7 jupyter pandas pycodestyle numpy
´´´

## Check environment
´´´
conda info --envs
conda activate 42AI-$USER
which python
python -V
python -c "print('Hello World!')
´´´
