#!/bin/bash

echo "welcome to SCP Communication"

echo "Copying a File Remotely over SSH with SCP"
#echo "Copy a Local File to a Remote System with the scp"
#echo "To copy a directory from a local to remote system"

echo "File Name with . extension"
read  file_Name

echo "Remote User Name"
read remote_user_name

echo "Remote Host Ip Address"
read remote_host_ip_address

echo "Remote directory path"
read remote_dir_path

#echo "Port number"
#read port_number

sudo scp "$file_Name" $remote_user_name@$remote_host_ip_address:$remote_dir_path


#scp -p $port_number $file_Name $remote_user_name@$remote_host_ip_address:$remote_dir_path


#echo "To copy a directory from a local to remote system"

#scp -r /local/directory remote_username@10.10.0.2:/remote/directory




#scp remote_username@10.10.0.2:/remote/file.txt /local/directory





#echo "Copy a File Between Two Remote Systems using the scp"
#scp user1@host1.com:/files/file.txt user2@host2.com:/files
  
#scp -3 user1@host1.com:/files/file.txt user2@host2.com:/files


