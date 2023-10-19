#!/bin/bash

echo -e "\nwelcome to network interface"

echo """$(tput setab 0)$(tput bold)
 $(tput setaf 3)1 $(tput setaf 6)set static IP 
 $(tput setaf 3)2 $(tput setaf 1)Disable Interface
 $(tput setaf 3)3 $(tput setaf 2)Enable Interface
 $(tput setaf 3)4 $(tput setaf 6)restart network
 $(tput setaf 3)5 $(tput setaf 1)stop service network-manager
 $(tput setaf 3)6 $(tput setaf 2)start service network-manager
 $(tput setaf 3)7 $(tput setaf 4)see service network-manager status
 $(tput setaf 3)8 $(tput setaf 4)See interface configuration $(tput sgr0)"""
read  opt

case "$opt" in

  1)
    #To set static IP
    echo "$(tput setaf 3)$(tput bold)Do you want to $(tput setaf 1)set static IP $(tput sgr0)[Y/N]"
    read ds_opt_YN
    if [ "$ds_opt_YN" != "${ds_opt_YN#[Yy]}" ];then 
        #Reading Interface
        echo -e "$(tput setaf 3)Interface ? $(tput sgr0)\t:"
        read interface

        #Reading Ip Address
        echo -e "$(tput setaf 3)IP Address ? $(tput sgr0)\t:"
        read ip_address

        #Reading Subnet/Netmas
        echo -e "$(tput setaf 3)Subnet/Netmask ?$(tput sgr0)\t:"
        read subnet_netmask 

        #Reading Gateway Address
        #echo -e "$(tput setaf 3)Gateway Address ?$(tput sgr0)\t:"
        #read gateway

        #Reading Network  ID 
        #echo  -e "$(tput setaf 3)Network ID ?$(tput sgr0)\t:"
        #read network

        #Reading Broadcast IP
        echo -e "$(tput setaf 3)Broadcast ip ? $(tput sgr0)\t:"
        read broadcast_ip

        #To Set static IP
        echo -e """$(tput setaf 1)$(tput bold)Do you want set $(tput rev)
    Interface : $interface
    Ip Address : $ip_address  
    Subnet\Netmask : $subnet_netmask
    Broadcast :  $broadcast_ip$(tput sgr0)\t\t\t[Y/N]"""
        read ipall_opt_YN
        if [ "$ipall_opt_YN" != "${ipall_opt_YN#[Yy]}" ];then
            #Assigning ip address
            sudo ifconfig $interface $ip_address netmask $subnet_netmask broadcast $broadcast_ip
            echo -e """$(tput setaf 2)$(tput bold)All assigned $(tput rev)
    Interface : $interface
    Ip Address : $ip_address
    Subnet\Netmask : $subnet_netmask
    Broadcast :  $broadcast_ip$(tput sgr0)"""
            #Making Delay of 5 seconds
            echo -e """
            $(tput setab 0)$(tput bold)\n\n\t\t\tWait 5s\n$(tput sgr0)"""
            sleep 5s
            #To show interface configuration
            ifconfig $interface 
        fi
    fi
    ;;

  2)
    #To Make Interface Down
    echo "$(tput setaf 3)$(tput bold)Do you want $(tput setaf 1 )$(tput bold)$interface Interface Down $(tput sgr0)[Y/N]"
    read ifdown_opt_YN
    if [ "$ifdown_opt_YN" != "${ifdown_opt_YN#[Yy]}" ];then
        echo -e "$(tput setaf 3)Interface ? $(tput sgr0)\t:"
        read interface 
        sudo ifconfig $interface down
        #Making Delay of 5 seconds
        echo -e """
        $(tput setab 0)$(tput bold)\n\n\t\t\tWait 5s\n$(tput sgr0)"""
        sleep 5s
        ifconfig
    fi
    ;;

  3)
    #To Make Interface UP
    echo "$(tput setaf 3)$(tput bold)Do you want $(tput setaf 2)$(tput bold)$interface Interface Up $(tput sgr0) [Y/N]"
    read ifup_opt_YN
    if [ "$ifup_opt_YN" != "${ifup_opt_YN#[Yy]}" ];then
        echo -e "$(tput setaf 3)Interface ? $(tput sgr0)\t:"
        read interface  
        sudo ifconfig $interface up
        #Making Delay of 5 seconds
        echo -e """
        $(tput setab 0)$(tput bold)\n\n\t\t\tWait 5s\n$(tput sgr0)"""
        sleep 5s
        ifconfig 
    fi
    ;;

  4)
    #To restart service network
    echo "$(tput setaf 3)$(tput bold)Do you want to $(tput setaf 5)restart network $(tput sgr0)[Y/N]"
    read restart_opt_YN
    if [ "$restart_opt_YN" != "${restart_opt_YN#[Yy]}" ];then
        sudo service network-manager restart
        
        #Making Delay of 5 seconds
        echo -e """
        $(tput setab 0)$(tput bold)\n\n\t\t\tWait 5s\n$(tput sgr0)"""        
        sleep 5s
        ifconfig
    fi

    ;;
    
  5)
    #To stop service network  
    echo "$(tput setaf 3)$(tput bold)Do you want to $(tput setaf 1)stop service network-manager $(tput sgr0)[Y/N]"
    read stop_opt_YN
    if [ "$stop_opt_YN" != "${stop_opt_YN#[Yy]}" ];then
        sudo service network-manager stop
        #Making Delay of 5 seconds
        echo -e """
        $(tput setab 0)$(tput bold)\n\n\t\t\tWait 5s\n$(tput sgr0)"""
        sleep 5s
        ifconfig
    fi
    ;;

  6)
    #To start service network
    echo "$(tput setaf 3)$(tput bold)Do you want to $(tput setaf 2)start service network-manager $(tput sgr0)[Y/N]"
    read start_opt_YN
    if [ "$start_opt_YN" != "${start_opt_YN#[Yy]}" ];then
        sudo service network-manager start
        #Making Delay of 5 seconds
        echo -e """
        $(tput setab 0)$(tput bold)\n\n\t\t\tWait 5s\n$(tput sgr0)"""
        sleep 5s
        ifconfig
    fi
    ;;

  7)
    #To see status of network
    echo "$(tput setaf 3)$(tput bold)Do you want to $(tput setaf 4)see service network-manager status $(tput sgr0)[Y/N]"
    read status_opt_YN
    if [ "$status_opt_YN" != "${status_opt_YN#[Yy]}" ];then
        sudo service network-manager status > status_network.txt
        cat status_network.txt
        echo "$(tput setaf 3)$(tput bold)Do you want to $(tput setaf 4)save network status $(tput sgr0)[Y/N]"
        read save_status_opt_YN
        if [ "$save_status_opt_YN" != "${save_status_opt_YN#[Yy]}" ];then
            echo -e "$(tput setaf 3) File Name '[No file extension]' $(tput sgr0)\t:"
            read file_name_0 
            echo -e "$(tput setaf 3) /Directory/Path/ $(tput sgr0)\t:"
            read dir_path_0 
            cp status_network.txt "$dir_path_0"$file_name_0.txt
            if [[ -z "$dir_path_0" ]];then
                echo -e "$(tput setaf 2)Successfully saved $file_name_0.txt at $PWD $(tput sgr0)\t"
            else
                echo -e "$(tput setaf 2)Successfully saved $file_name_0.txt at $dir_path_0 $(tput sgr0)\t"
            fi
            true > status_network.txt
        else 
        true > status_network.txt
        fi
    fi
    ;;

  8)
    echo "$(tput setaf 3)$(tput bold)Show interface configuration $(tput sgr0)[Y/N]"
    read ifconfig_opt_YN
    if [ "$ifconfig_opt_YN" != "${ifconfig_opt_YN#[Yy]}" ];then 
        ifconfig  -a
    fi
    ;;

  *) echo "Invalid option"
    ;;
esac
