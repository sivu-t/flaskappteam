=============
Flaskbasic
=============

Flaskbasic Python Flask App

Description
===========
Flaskbasic was created by the Dev team at Kinetic Skunk. It is built using python, flask and sqlite to store student results in a database. The aim is to keep records of every students results and be able to view them.


Note
====

This project has been set up using PyScaffold 3.1. For details and usage
information on PyScaffold see https://pyscaffold.org/.

Installation
=============
*python*
   $ https://www.python.org/downloads/
*pip*
  $ python get-pip.py.
*pyscaffold*
  $ pip install --upgrade pyscaffold


How to install flaskbasic on PC
===========================
*Clone repository*
  $ git clone https://github.com/DarrenMun/newflask
  $ git ckeckout new-branch-name
  $ git fetch
  $ git pull

*Creating pip environment*
  $ pip install pipenv
*Using Pipenv and getting into shell*
  $ cd into project folder
  $ pipenv shell

  *If a requirements.txt file already exists
  $ pipenv install -r requirements.txt
  $ pipenv lock

Run application local on your PC
================================
python application.py

Deploying to MiniShift
======================
*First install Minishift*

  **Instructions for installation [https://github.com/minishift/minishift
  welcome-to-minishift]
Step 1
    - Download the release for windows [https://github.com/minishift/minishift/releases]
Step 2
    - Download VM software VirtualBox
    [https://www.virtualbox.org/wiki/Downloads]
        - No need to Create a Virtual Machine/Will automatically be created
Step 3
    - Open minishift extract file, CD to extracted file path with CMD
        - Run to start command
        $ minishift start --vm-driver virtualbox
            - Will download and install the Openshift Binary 'oc' version
            - Will download minishift-centos-iso 300 - 400 mb
            - Starting OpenShift container image
            - Will show that the server started
Step 4
    - Copy the IP address in your URL
Step 5
    - Logging in
        - Username : developer
        - Password : <any value>

    - Admin Login
        - In Terminal paste (oc login -u system:admin) if not working
        - Paste : (@FOR /f "tokens=*" %i IN ('minishift oc-env') DO @call %i)
        - Set your user as an admin
            - Paste in terminal (oc adm policy add-cluster-role-to-user cluster-admin "YOUR NAME")
            - Youtube video Link (Push local docker images to openshift registry - minishift)
Successfully installed Minishift working locally *Thumbs Up*
    - To stop Minishift command ($ minishift stop)
    - To delete your Minishift ($ minishift delete)

Commands on deploying onto MINISHIFT
====================================

$ oc new-app https://github.com/DarrenMun/newflask
$ oc start-build newflask
