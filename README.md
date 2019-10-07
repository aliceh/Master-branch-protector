# Master branch protector

This application is a simple web service listening for [organization events](https://developer.github.com/webhooks/#events) posted by a [github webhook](https://help.github.com/en/articles/about-webhooks). When a repository is created by the organization, the app enables protection on the master branch, and an issue is created in the repository where a designated person is notified with a [@mention.](https://github.blog/2011-03-23-mention-somebody-they-re-notified/)

To run the app you will need:

*  an access token to a GitHub account of a member of the organization with admin privileges.

*  to create a webhook in GitHub. Only members with owner privileges for an organization or admin privileges for a repository can manage webhooks for an organization. For more information, see ["Permission levels for an organization."](https://help.github.com/en/articles/permission-levels-for-an-organization)

Prerequisites
================

Prior to installing the dependencies, you may need to install the following libraries. We recomend that you run the application in virtualenv.

```
python3, python3-pip, python3-distutils, python3-lib2to3
```

With virtualenv (recommended):

```
 python3-venv, python3-virtualenv 
````
Ubuntu:
------
```
sudo apt-get install python3 python3-pip python3-distutils python3-lib2to3
```    
If you are going to use virtualenv (recommended):
```    
sudo apt-get install python3-venv python3-virtualenv 
```
Running the Master branch protector application
===============================================



Setting up virtualenv (recommended)
---------------------
```
mkdir -p env

cd ~/env

export VENV=~/env

python3 -m venv $VENV

$VENV/bin/pip install --upgrade pip setuptools
```
Setting up the application dependencies
------------------------
```
git clone https://github.com/aliceh/Master-branch-protector
```
Without virtualenv:
```
pip3 install -r ~Master-branch-protector/requirements.txt 
````
With virtualenv (recommended):
```
$VENV/bin/pip3 install -r ~Master-branch-protector/requirements.txt 
```
Launching the application 
-------------------------

1. Choose a port on your system (such as 8080) where the web server will be listening to incoming requests from the Guthub webhook that you will create. Make sure that the port is open for incoming traffic.

2. Create a github webhook. 

* Go to the Settings page for your Organization
* Click Webhooks > Add webhook
* For Payload URL, use the URL of your system with the port where the webserver is listening. (Example: ```http://10.128.98.5:8080```)
* For Content type, both application/json and application/x-www-form-urlencoded work
* Leave the Secrets field blank
* Select Send me everything or Let me select individual events, and mark Repositories
* Finish by clicking Add webhook. You may be prompted to enter your GitHub password to confirm your action.

3. If you are using virtualenv, run the following.

```
source $VENV/bin/activate
```
4. Finally, launch the application from command line and pass the following arguments.
```
python3 master_branch_protector.py -m <github user name to use in @mention> -p <the port specified in the webhook on which the webserver is listening> -t <github token to access the organization events> 
```
## Example

Without virtualenv:

```
python3 master_branch_protector.py  -m "johnsmith" -p 6543 -t "2343455666777655433222233454322"
```
With virtualenv (recommended):

```
source $VENV/bin/activate

python3 master_branch_protector.py  -m "johnsmith" -p 6543 -t "2343455666777655433222233454322"
```
For help run 

```
python master_branch_protector.py -h
```

