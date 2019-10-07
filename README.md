# Master branch protector

This application is a simple web service listening for [organization events](https://developer.github.com/webhooks/#events). When a repository is created, the protection on master branch is enabled by the app, and an issue is created in the repository where a designated person is notified with a @mention.

Prerequisites
================


The [organization events](https://developer.github.com/webhooks/#events)

Prior to installing the dependencies, you may need to install the following libraries. We recomend that you run the application in virtualenv.


* python3, python3-pip, python3-distutils, python3-lib2to3

With virtualenv (recommended):


* python3-venv, python3-virtualenv 

Ubuntu:
------

    sudo apt-get install python3 python3-pip python3-distutils python3-lib2to3
    
    If you are going to use virtualenv (recommended):
    sudo apt-get install python3-venv python3-virtualenv 

Running the Master branch protector application
===============================================



Setting up virtualenv (recommended)
---------------------

mkdir -p env

cd ~/env

export VENV=~/env

python3 -m venv $VENV

$VENV/bin/pip install --upgrade pip setuptools

Setting up the application dependencies
------------------------

git clone https://github.com/aliceh/Master-branch-protector

Without virtualenv:

pip3 install -r ~Master-branch-protector/requirements.txt 

With virtualenv (recommended):

$VENV/bin/pip3 install -r ~Master-branch-protector/requirements.txt 

Launching the application 
-------------------------

The application 


python master_branch_protector.py --port 6543 --token "2343455666777655433222233454322"
