# SNMP-Auto-config-MIBireasoning-installation
<h2> Brief description </h2>
The program download, install and configure SNMP packages and ireasoning software for monitoring. The main goal of the program is to automate
the deployment of SNMP and ireasoning to multiple servers and avoid going through the steps manually for each deployment.
<h2> Prerequisites </h2>
<ul>
  <li>This program uses yum for the installation part</li>
  <li>Import subprocess and os libraries</li>
  <li>Tested on pythons 2</li>
  <li>Tested on CentOS 6</li>
  <ii> Access to /root/Desktop</li>
  <li> root privileges</li>
</ul>

<h2>Installing and running the program</h2>
Download the forlder and change the permissions of the run.sh file to be executable. The run by simply typing <i>./run.sh</i>

<h2>Documentation</h2>
The program avoids the use of any special python libraries to ensure its compatibility with the most systems that are running on minimum python environment.
The program contains two python programs and one run script.
<h3>installSnmp.py</h3>
<ul>
  <li>Download and Install net-snmp, net-snmp-utils packages and verify.</li>
  <li>Uses predefined snmpd.conf file to replace the default file.</li>
  <li>Run SNMP services and verify</li>
  <li>configure SNMP to run on boot</li>
</ul>

<h3>ireasoningInstall.py</h3>
<ul>
  <li>Download ireasoning software and verify.</li>
  <li>unzip ireasoning software</li>
  <li>Check the software minimum requirements</li>
  <li>Install and reconfigure the software permissions</li>
</ul>

<h3>run.sh</h3>
The main file to run both python programs in an interactive way.


