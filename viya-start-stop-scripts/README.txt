Before running the ansible playbook, create symbolic links to the inventori.in and vars.yml files
of the sas_viya_deploment.

Example:

[centos@tdc-loadbalancer tas-ansible]$ ll
total 104
-rw-rw-r--. 1 centos centos  364 Nov 21 08:13 createViyaStartStopScripts.yml
-rw-rw-r--. 1 centos centos 3105 Nov 21 08:10 gel.startStopMicroServices.sh
lrwxrwxrwx. 1 centos centos   55 Nov 21 08:16 inventory.ini -> /nfs/sas/install/09N7MQ/sas_viya_playbook/inventory.ini
-rw-rw-r--. 1 centos centos 8449 Nov 21 08:10 startViyaCluster.j2
-rw-rw-r--. 1 centos centos 8258 Nov 21 08:10 stopViyaCluster.j2
lrwxrwxrwx. 1 centos centos   50 Nov 21 08:18 vars.yml -> /nfs/sas/install/09N7MQ/sas_viya_playbook/vars.yml

Then run the palybook with the command:

ansible-playbook -i inventory.ini createViyaStartStopScripts.yml


