# Master branch protector

This is a simple web service listening for organization events to know when a repository has been created. When a repository is created, the protection on master branch is automatically enabled, and an issue is created in the repository where a designated person is notified with a @mention that outlines the protections that were added.

Prerequisites
-------------
Prior to installing the dependencies, you may need to install the following libraries...

* python3
* python3-pip, python3-distutils, python3-lib2to3
* python3-venv, python3-virtualenv (if you choose to use virtualenv)

Ubuntu:

    `apt-get install openssl build-essential python-dev swig memcached libmemcached6`

Fedora:

    `yum install openssl-devel python-devel swig memcached libmemcached; yum groupinstall 'Development tools'`

OS X:

Install homebrew, then run `brew install libevent openssl swig libmagic memcached libmemcached`
You will need  python3, python3-pip, python3-venv, python3-distutils, python3-lib2to3, python3-virtualenv

mkdir -p environment

cd ~/environment

export VENV=~/environment/env

python3 -m venv $VENV

$VENV/bin/pip install --upgrade pip setuptools

git clone https://github.com/aliceh/Master-branch-protector

$VENV/bin/pip install -r ~Master-branch-protector/requirements.txt 

python master_branch_protector.py --port 6543 --token "2343455666777655433222233454322"
