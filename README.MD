# SunEvil: Decentralized Botnet Over RPi Cluster #
## Computer Networks COSC6377 - Fall 2018 ##
## Taha Eghtesad - 1802109 ##

### Problem ###

**Botnets** have always been a key component to **DDoS attacks**. They are untraceable as each node work as a regular innocent user, and unblockable because they are large in number and geographically spread. With growing number of IoT devices eg. _Smart Home Appliances, Smart Sensors, etc,_ made by startup companies that security is not of paramount concern, they can be a good choice to be exploited and converted to botnets. These IoT devices having limited resources like _network bandwidth, processing power, and memory_ are a perfect fit for this usage. The purpose of this project is to determine how effective they can be.

### Approach ###

Raspberry Pis (3 Model B+) have two on-chip networking interfaces: 10/100 Mbit/s ethernet and a 2.4GHz and 5GHz IEEE 802.11.b/g/n/ac wireless LAN. To determine the feasibility of a _DDoS_ attack with botnets of IoT devices, 20+ RPis are connected through a gigabit switch and then a distributed botnet is installed on all of them. This botnet malware, **SunEvil**, will then start sending large and small requests to a target host running an HTTP Server. **SunEvil** having it's own node discovery protocol and being decentralized can be a good example of a botnet which has no single point of failure. The host will measure the bandwidth caused by this malicious network and see whether it can affect it's resources or not. Another measuring tool running on another computer will then measure the response time of the HTTP server. This experiment will be re-executed when the RPis are connected through a 2.4Ghz and 5GHz wireless access points.

### Deliverables ###

_Milestone 1:_
* A Raspberry Pi Cluster connected through Ethernet and Wifi
* SunEvil Botnet

_Milestone 2:_
* Measurements, charts and results