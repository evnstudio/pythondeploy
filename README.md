# pythondeploy
Auto deploy Nodejs without using thirdparty

## Requirment

  <li>Install Python
  <li>Install Paramiko

#

### On Server
<pre>

## Clone your repo in your server

git clone < repo >
cd < repo >

## Save username and password git

git config credential.helper store
git pull


</pre>

### On Pc
<pre>
wget https://raw.githubusercontent.com/envstudio/pythondeploy/master/pydeploy.py

# Check your config

nano pydeploy.py
then save

cd < repo >

/home/path/pydeploy.py commitname
</pre>


### This is fun project, Im am new python user, correct me if wrong
