#!/bin/bash

echo -e "\nwelcome to SSH Communication"
echo """$(tput setab 0)$(tput bold)
$(tput setaf 3)1 $(tput setaf 6)1 $(tput setaf 1)install openSSH client
$(tput setaf 3)1 $(tput setaf 6)2 $(tput setaf 1)install openSSH server
$(tput setaf 3)1 $(tput setaf 6)3 $(tput setaf 0)
$(tput setaf 3)1 $(tput setaf 6)4 $(tput setaf 4)SSH status
$(tput setaf 3)1 $(tput setaf 6)5 $(tput setaf 6)restart SSH
$(tput setaf 3)1 $(tput setaf 6)6 $(tput setaf 0)
$(tput sgr0)"""
echo "Do you want to install openSSH client [Y/N]" 
read client_opt_YN
if [ "$client_opt_YN" != "${client_ssh_opt_YN#[Yy]}" ]
    then
        sudo apt-get install openssh-client
fi

echo "Do you want to install openSSH server [Y/N]" 
read server_opt_YN
if [ "$server_opt_YN" != "${server_opt_YN#[Yy]}" ]
    then
        sudo apt-get install openssh-server ii.
fi

echo "User Name"
read user_name

echo "Host Ip Address"
read host_ip_address

echo "Port number"
read port_number
echo "welcome to ssh"
if [[ -z "$port_number" ]]
    then
        echo "we are going to enter SSH please  wait  .... "
        ssh $user_name@$host_ip_address 
    else
        echo "we are going to enter SSH with port number please  wait  ...."
        ssh $user_name@$host_ip_address -p $port_number
fi


#echo "some use full commands\n sudo service ssh status \n sudo service ssh restart"


echo "Do you want to see SSH status [Y/N]"
read status_opt_YN
if [ "$status_opt_YN" != "${status_opt_YN#[Yy]}" ]
    then
        sudo service ssh status
fi

echo "Do you want to restart SSH [Y/N]"
read restart_opt_YN
if [ "$restart_opt_YN" != "${restart_opt_YN#[Yy]}" ]
    then
        sudo service ssh restart
fi