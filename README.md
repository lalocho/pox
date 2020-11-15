Assignment 4 - Software Defined Networks
Luis Ochoa
Peter Hanson
Software-Defined Networking (SDN) is a recently proposed networking paradigm in which the
data and control planes are decoupled from one another. One can think of the control plane as
being the networks "brain", i.e., it is responsible for making all decisions, for example, how to
forward data, while the data plane is what actually moves the data. In traditional networks, both
the control- and data planes are tightly integrated and implemented in the forwarding devices
that comprise a network. The SDN control plane is implemented by the "controller" and the data
plane by "switches". The controller acts as the "brain" of the network and sends commands
("rules") to the switches on how to handle traffic. OpenFlow has emerged as the de facto SDN
standard and specifies how the controller and the switches communicate as well as the rules
controllers install on switches.


Task-1: Programming Mininet Topologies (30 pts)


Mininet is also programmable using the python programming language. A set of sample
topologies are provide in the “assign4starter.zip”. Download and unzip this file in the Ubuntu
VM and you'll find two different directories: topo and pox. Ignore the pox directory for now (it's
used in Task-2). In the topo folder there are a variety of python files. Each defines a topology,
run the part1 file with command “sudo python assign4starter/topos/part1.py”. It will drop you
into the CLI with the network topology defined in the python script.
1) Your task here is to modify part1.py to represent the following network topology
Where [x] means you create a host named x, {y} means a switch named y, and --- means
there is a link between the node and the switch.
2) After creating the above architecture, provide the two items in a part1 folder in a
compressed file: a) Your modified part1.py file; (b) Screenshots of the iperf, dump,
and pingall commands (from mininet) in pdf format.
Instructions for running part1.py:
In order to run the code, you need to have mininet installed on your computer, then you need to move to the directory of the code and type into the command line

sudo python part1.py

Once you are inside the mininet, you can type in the desired commands as seen above in order to get the same results from the images. You can also open the file to take a look at the source code.


Task-2: SDN Controller using POX (70 pts)


In task 1, you experimented with Mininet using its internal controller. In this (and future) task, you
will instead be using a custom controller to send commands to the switches. Here, we will be using
the POX controller, which is written in Python. For this part, you will create a simple firewall
using OpenFlow-enabled switches. The term "firewall" is derived from building construction: a
firewall is a wall you place in buildings to stop a fire from spreading. In the case of networking, it
is the act of providing security by not letting specified traffic pass through the firewall. This feature
is good for minimizing attack vectors and limiting the network "surface" exposed to attackers.
In this part, you are provided with the Mininet topology, part2.py, to setup your network which
assumes a remote controller listening on the default IP address and port number 127.0.0.1:6633.
You do not need to (and should not) modify this file. The topology that this script will setup is
as follows. Note that h1 and h4 are on the same subnet and a different one from h2 and h3.
For part-2, you are also provided with a skeleton POX controller (under pox folder):
“part2controller.py”. This file is required to be modified to create the firewall that implements
the following rules.
Then, you need to deploy this new controller and run mininet under the new topology provided in
“part2.py”.
Note: Basically, your Firewall should allow all ARP and ICMP traffic to pass. However, any other
type of traffic should be dropped. It is acceptable to flood the allowable traffic out all ports. Be
careful! Flow tables match the rule with highest priority first, where priority is established based
on the order rules are placed in the table. When you create a rule in the POX controller, you need
to also have POX "install" the rule in the switch. This makes it so the switch "remembers" what to
do for a few seconds. Do not handle each packet individually inside of the controller! Hint:
To do this, look up ofp_flow_mod. The OpenFlow tutorial (specifically " Sending OpenFlow
messages with POX") and the POX Wiki are both useful resources for understanding how to use
POX. 


Instructions for running Part 2:
  Install pox on your machine
  Sudo pip install pox
  Go to directory ~pox/ext
  Download the files to your machine
  Save the part2controller.py file inside ~pox/ext  folder
  Go back to the pox directory 
  Use ./pox.py part2controller to run
  In another terminal run mininet with  part2.py using sudo python part2.py
  Use sudo mn -c if you have run a topology before to clear it if you get an error
  Inside the mininet terminal use the following commands
  Pingall
  Iperf     * should hang, interrupt with ctrl^c
  Dpctl dump-flows
