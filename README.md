# Master branch protector

This is a simple web service listening for organization events to know when a repository has been created. When a repository is created, the protection on master branch is automatically enabled, and an issue is created in the repository where a designated person is notified with a @mention that outlines the protections that were added.

# Instructions to run on Ubuntu


sudo apt-get update

sudo apt-get install -y python3

sudo apt-get install -y python-pip

sudo apt-get install -y python3-venv

sudo apt-get install -y python3-distutils python3-lib2to3 python3-virtualenv

mkdir -p environment

cd ~/environment

export VENV=~/environment/env

python3 -m venv $VENV

$VENV/bin/pip install --upgrade pip setuptools

git clone https://github.com/aliceh/Master-branch-protector

$VENV/bin/pip install -r ~Master-branch-protector/requirements.txt 

