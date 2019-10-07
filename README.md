# Master branch protector

This application is a simple web service listening for [organization events](https://developer.github.com/webhooks/#events) posted by a [github webhook](https://help.github.com/en/articles/about-webhooks). When a repository is created by the organization, the app enables protection on the master branch, and an issue is created in the repository where a designated person is notified with a @mention.

To run the app you will need an access token to a GitHub account of a member of the organization with admin privileges.

Only members with owner privileges for an organization or admin privileges for a repository can manage webhooks for an organization. For more information, see ["Permission levels for an organization."](https://help.github.com/en/articles/permission-levels-for-an-organization)

Prerequisites
================

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

1. Choose a post on your system where the web server will be listening to incoming requests from the Guthub webhook that you will create. Make sure that the port is open for incoming requests from GitHub.

2. Create a github webhook 

python master_branch_protector.py  -m "johnsmith" --port 6543 --token "2343455666777655433222233454322"
