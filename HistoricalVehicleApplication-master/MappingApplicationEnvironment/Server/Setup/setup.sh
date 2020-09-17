#!/bin/bash
# Script to setup work enviroment for the Historical Mapping Application
# Targets ubuntu
# Written by: Edward C. Deaver, IV

echo "Setup enviroment"
apt-get    update 
apt-get -y upgrade

 wget http://packages.erlang-solutions.com/site/esl/esl-erlang/FLAVOUR_1_general/esl-erlang_21.0-1~debian~jessie_amd64.deb
 
 sudo dpkg -i esl-erlang_21.0-1~debian~jessie_amd64.deb

 
wget -O - 'https://dl.bintray.com/rabbitmq/Keys/rabbitmq-release-signing-key.asc' | sudo apt-key add -
echo "deb https://dl.bintray.com/rabbitmq/debian xenial main" | sudo tee /etc/apt/sources.list.d/bintray.rabbitmq.list
sudo apt-get update
sudo apt-get -f install rabbitmq-server