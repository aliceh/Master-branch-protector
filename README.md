# Master branch protector

This is a simple web service listening for organization events to know when a repository has been created. When a repository is created, the protection on master branch is automatically enabled, and an issue is created in the repository where a designated person is notified with a @mention that outlines the protections that were added.

Prerequisites
=============

Prior to installing the dependencies, you may need to install the following libraries. We recomend that you run the application in virtualenv.


* python3, python3-pip, python3-distutils, python3-lib2to3

And if you are using virtualenv (recommended):


* python3-venv, python3-virtualenv 

Ubuntu:

    `sudo apt-get install python3 python3-pip python3-distutils python3-lib2to3'
    
    If you are using virtualenv (recommended):
    `sudo apt-get install python3-venv python3-virtualenv' 

Running the Master branch protector application
===============================================


If you are using virtualenv (recommended):


Setting up virtualenv
---------------------

{mkdir -p env

cd ~/env

export VENV=~/env

python3 -m venv $VENV

$VENV/bin/pip install --upgrade pip setuptools}

Running the application:

git clone https://github.com/aliceh/Master-branch-protector

If you are using virtualenv (recommended):
$VENV/bin/pip3 install -r ~Master-branch-protector/requirements.txt 

python master_branch_protector.py --port 6543 --token "2343455666777655433222233454322"
