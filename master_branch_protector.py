#!/usr/bin python
import logging
import json
import requests
import ipaddress
import argparse
import time
from flask import Flask, request
from github import Github

logging.basicConfig(filename='master_branch_protector.log',level=logging.INFO)


app = Flask(__name__)
parser = argparse.ArgumentParser()
parser.add_argument('-t','--token', dest='github_token',
                    help='Github access token for enabling protection on branches and adding comments.')
parser.add_argument('-p','--port', type=int, default=80, dest='port_number', help='The port on which the webserver will listen.')

parser.add_argument('-m','--mention', dest='github_mention', help='The github username to use in @mention.')
args = parser.parse_args()

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return 'OK'
    elif request.method == 'POST':
        # Store the IP address of the requester
        request_ip = ipaddress.ip_address(u'{0}'.format(request.remote_addr))
        logging.info("IP : " +str(request_ip))
        load=request.get_json()
        if load==None:
            load=json.loads(request.form['payload'])
        if 'action' in load:
            action = str(load['action'])
            logging.info("ACTION : "+action)
            repo_name=str(load['repository']['name'])
            logging.info("REPO NAME : "+ repo_name)
            org_and_repo=str(load['repository']['full_name'])
            logging.info("ORG/REPO : "+org_and_repo)
            if action=='created':
                g=Github(args.github_token)
                repo=g.get_repo(org_and_repo)
                master_branch = None
                for i in range(1,5):
                    logging.info("TRYING for master BRANCH")
                    time.sleep(.5)
                    if repo.get_branch("master"):
                        master_branch=repo.get_branch("master")
                        logging.info("GOT master BRANCH")
                        break
                if (master_branch != None):
                    was_protected = master_branch.protected is True
                    counter=0
                    while (not (master_branch.protected is True)) and counter < 5:
                        time.sleep(.5)
                        logging.info("MASTER BRANCH PROTECTION STATUS : "+ str(master_branch.protected))
                        master_branch=repo.get_branch("master")
                        master_branch.edit_protection()
                        counter += 1
                    logging.info("MASTER BRANCH PROTECTION STATUS : "+ str(master_branch.protected))
                    if (not was_protected) and (master_branch.protected is True):
                        issue=repo.create_issue("Master branch protection")
                        issue.create_comment("@"+ args.github_mention + ", protection was enabled on master branch")
                        logging.info("Comment sent to @" + args.github_mention)

    return 'OK'
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=args.port_number, debug=True)
