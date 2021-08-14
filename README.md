<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
[![MIT License][license-shield]][license-url]

<!-- ABOUT THE PROJECT -->
## About The Project

Simple linux tool built to make it easier to viewing SSH ```auth.log(s)``` by pulling only failed password attempts. Tool will display by deafult the top 5 ip addresses, users, and ports used in failed attempts to log into a SSH session. Additionally tool is able to provide a full ip list along with the total number of failed occurences. Appending a cleaning flag will give a clean version of that list only displaying ip addresses. 


### Built With

* [Python 3.9.2](https://www.python.org/downloads/)


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/ocastaneda3/log_analyzer.git
   ```

<!-- USAGE EXAMPLES -->
## Usage

Tool can be run from any location but does require ```sudo``` or root privileges in order to be able to read SSH auth.log(s) that are located under ```/var/log/```. Tool is used as follows:
   ```sh 
      $ sudo python3 log_analyzer.py /var/log/auth.log
   ```
By default this tool print the top 5 results of occurences in ip addresses, users, and ports used in failed attempts to login.

#### Help Screen 
   ```sh
   $ sudo python3 log_analyzer.py -h

   usage: sudo log_analysis.py [-h] [-n N] [-f] [-c] [-d] filename [filename ...]

   Simple tool to pull Failed Password attempts from SSH AUTH Logs

   positional arguments:
     filename     input file name

   optional arguments:
     -h, --help   show this help message and exit
     -n N         print top N
     -f, --full   print full ip list w/ number of occurences
     -c, --clean  print clean list and to be used with [-f] to
     -d, --debug  enable debugging

   ```

#### Running

##### - Print Top N Results ```[-n N]```
   ```sh
   $ sudo python3 log_analyzer.py -n 5 /var/log/auth.log

   ------------------------------------------------------------
   << Top # 5 IP Addresses >>
   ------------------------------------------------------------
   1)             49.88.112.116:      899
   2)              218.92.0.205:      816
   3)           221.181.185.135:      615
   4)            222.186.42.213:      585
   5)              87.241.1.186:      526
   ------------------------------------------------------------
   ------------------------------------------------------------
   << Top # 5 Users >>
   ------------------------------------------------------------
   1)                      root:    29659
   2)                   invalid:     7546
   3)                    backup:       15
   4)                       www:       11
   5)                      sshd:        8
   ------------------------------------------------------------
   ------------------------------------------------------------
   << Top # 5 Ports >>
   ------------------------------------------------------------
   1)                      1024:       67
   2)                     18048:       50
   3)                      1089:       39
   4)                      1090:       39
   5)                      1091:       37
   ------------------------------------------------------------
   ```
   
##### - Print Full List ```[-f], [--full]```
   ```sh
   $ sudo python3 log_analyzer.py --full /var/log/auth.log

   49.88.112.116        899
   218.92.0.205         816
   221.181.185.135      615
   222.186.42.213       585

   . . .

   42.192.134.176         1
   106.12.182.249         1
   220.117.154.138        1
   119.136.154.50         1
   ```
 
##### - Print Full Clean List ```[-c], [--clean]```
   ```sh
   $ sudo python3 log_analyzer.py --full --clean /var/log/auth.log

   49.88.112.116
   218.92.0.205
   221.181.185.135
   222.186.42.213

   . . . 

   42.192.134.176
   106.12.182.249
   220.117.154.138
   119.136.154.50
   ```
  
  ##### - Print W/ Debug ```[-d], [--debug]```
   ```sh
   $ sudo python3 log_analyzer.py --full --clean /var/log/auth.log

   date/timestamp: Aug  1 00:00:15, user: root, ip: 218.92.0.205, port 27348
   date/timestamp: Aug  1 00:00:23, user: root, ip: 218.92.0.205, port 27348
   date/timestamp: Aug  1 00:00:38, user: invalid, ip: 118.195.132.206, port 57754
   date/timestamp: Aug  1 00:00:43, user: invalid, ip: 59.63.230.46, port 57910

   . . .

   date/timestamp: Aug  5 18:42:00, user: invalid, ip: 45.55.193.62, port 37152
   date/timestamp: Aug  5 18:42:21, user: root, ip: 220.88.1.208, port 41622
   date/timestamp: Aug  5 18:42:29, user: invalid, ip: 27.221.18.26, port 50646

   ```
   
<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [Black Hills Information Security](https://www.youtube.com/watch?v=6j0zjmaYcXs&t=3241s)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/ocastaneda3/log_analyzer?style=for-the-badge
[contributors-url]: https://github.com/ocastaneda3/log_analyzer/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/ocastaneda3/log_analyzer?style=for-the-badge
[forks-url]: https://github.com/ocastaneda3/log_analyzer/network/members
[stars-shield]: https://img.shields.io/github/stars/ocastaneda3/log_analyzer?style=for-the-badge
[stars-url]: https://github.com/ocastaneda3/log_analyzer/stargazers
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/oscar-castaneda93/
[license-shield]: https://img.shields.io/github/license/ocastaneda3/log_analyzer?style=for-the-badge
[license-url]: https://github.com/ocastaneda3/log_analyzer/blob/main/LICENSE
