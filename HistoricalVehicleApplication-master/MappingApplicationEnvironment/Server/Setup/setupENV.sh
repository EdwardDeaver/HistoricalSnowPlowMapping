#!/bin/bash
# Script to setup work enviroment for the Historical Mapping Application
# Targets AMAZON LINUX
# Written by: Edward C. Deaver, IV


echo "SETTING UP YOUR ENVIROMENT "

#######################
## Install Erlang RabbitMQ Related

cd /opt
wget http://packages.erlang-solutions.com/site/esl/esl-erlang/FLAVOUR_1_general/esl-erlang_21.0-1~centos~6_amd64.rpm
sudo rpm -ivh erlang-20.1.7-1.el6.x86_64.rpm  

#######################
## Install Socat RabbitMQ Related
 yum install socat  
 
 ####################
 ## RabbitMQ 
wget https://dl.bintray.com/rabbitmq/all/rabbitmq-server/3.7.0/rabbitmq-server-3.7.0-1.el6.noarch.rpm
sudo rpm -ivh rabbitmq-server-3.7.0-1.el6.noarch.rpm

#####################
## NODE JS

curl --silent --location https://rpm.nodesource.com/setup_8.x | sudo bash -
sudo yum -y install nodejs

######################
## tILE38
curl -L  https://github.com/tidwall/tile38/releases/download/1.12.3/tile38-1.12.3-linux-amd64.tar.gz -o tile38-1.12.3-linux-amd64.tar.gz


mv $PATH/tile38-1.12.3-linux-amd64.tar.gz /home/ec2-user/HistoricalVehicleApplication/MappingApplication/Server/Dependencies/
cd /home/ec2-user/HistoricalVehicleApplication/MappingApplication/Server/Dependencies/
tar xzvf tile38-1.12.3-linux-amd64.tar.gz
cd tile38-1.12.3-linux-amd64
./tile38-server &

######################
## AutoStart

#echo $PATH


#mv /home/ec2-user/autorunMappingENV.sh //etc/init.d/
#sudo chmod +x //etc/init.d/autorunMappingENV.sh

