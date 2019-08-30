import os
import subprocess as AAY

# install the snmpd package
print("installing packages... ")

check = AAY.Popen(["yum", "-y", "install", "net-snmp", "net-snmp-utils"], stdout=AAY.PIPE, stderr=AAY.PIPE)
read, err = check.communicate()

"""print('================================')
print("read value: ", read)
print('\n\n\n================================')
print("error value: ", err)"""

if "Nothing to do" in read:
    print("The Package is already installed :|")
elif "Installed" and "Complete!" in read:
    print("Package has been installed successfully! :)")
else:
    print(" You have problem. Please check your connectivity or permission!")
    exit(1)


# check the snmpd.conf (default) file existing
with open(os.devnull, "w") as f:
    check = AAY.call(['ls', '-l', '/etc/snmp/'], stdout=f, stderr=f)
    if check == 0:
        print("Deleting the default configuration file...")
        AAY.call(['rm', '-rf', '/etc/snmp/snmpd.conf'], stdout=f, stderr=f)
    else:
        print("The snmp directory doesn't exist!")
        exit(1)

    # copy the new configuration file "snmpd.conf"
    print("copying the new configuration file \"snmpd.conf\"...")
    check = AAY.call(['cp', 'snmpd.conf', '/etc/snmp/'], stdout=f, stderr=f)
    if check == 0:
        print("file copied successful to \"/etc/snmp/\"  :)")
    else:
        print("Please make sure that your configuration file is under the project directory :|")
        exit(1)

# start the service

check = AAY.Popen(['service', 'snmpd', 'status'], stdout=AAY.PIPE, stderr=AAY.PIPE)
read, err = check.communicate()

if "stopped" in read:
    AAY.call(['service', 'snmpd', 'start'])
elif "running" in read:
    AAY.call(['service', 'snmpd', 'restart'])
    AAY.call(['chkconfig', 'snmpd', 'on'])

else:
    print("Some problem accord!!")
    exit(1)
