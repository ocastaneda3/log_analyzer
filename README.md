<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
[![MIT License][license-shield]][license-url]

<!-- ABOUT THE PROJECT -->
## About The Project

Simple tool built to make it easier to viewing SSH auth.logs by pulling only failed password attempts. Tool will display by deafult the top 5 ip addresses, users, and ports used in failed attempts to log into a SSH session. Additionally tool is able to provide a full ip list along with the total number of failed occurences. Appending a cleaning flag will give a clean version of that list only displaying ip addresses. 


### Built With

* [Python 3.9.2](https://www.python.org/downloads/)


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/ocastaneda3/log_analyser.git
   ```

<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

#### [-h], [--help]   show this help message and exit 
  ```sh
  $ sudo python3 log_analyzer.py --help
  
  usage: sudo log_analysis.py [-h] [-n N] [-f] [-c] [-d] filename [filename ...]

  optional arguments:
    -h, --help   show this help message and exit
    -n N         print top N
    -f, --full   print full ip list w/ number of occurences
    -c, --clean  to be used with [-f] to print clean list
    -d, --debug  enable debugging

  required arguments:
    filename     input file name
  ```
####  [-n] N         print top N
  ```sh
  $ sudo python3 log_analyzer.py -n 3 /var/log/auth.log
  
  ------------------------------------------------------------
   << Top # 3 IP Addresses >>
  ------------------------------------------------------------
   1)             49.88.112.116:      899
   2)              218.92.0.205:      816
   3)           221.181.185.135:      615
  ------------------------------------------------------------
  ------------------------------------------------------------
   << Top # 3 Users >>
  ------------------------------------------------------------
   1)                      root:    29659
   2)                   invalid:     7546
   3)                    backup:       15
  ------------------------------------------------------------
  ------------------------------------------------------------
   << Top # 3 Ports >>
  ------------------------------------------------------------
   1)                      1024:       67
   2)                     18048:       50
   3)                      1089:       39
  ------------------------------------------------------------
  ```
#### [-f], [--full]   print full ip list w/ number of occurences
  ```sh
  $ sudo python3 log_analyzer.py --full /var/log/auth.log
  
  49.88.112.116        899
  218.92.0.205         816
  221.181.185.135      615
  222.186.42.213       585
  87.241.1.186         526
  221.181.185.153      467
  221.181.185.198      403
  221.181.185.159      388
  . 
  . .
  . . .
  ```
 
#### [-c], [--clean]  to be used with [-f] to print clean list
  ```sh
  $ sudo python3 log_analyzer.py --full --clean /var/log/auth.log
  
  49.88.112.116
  218.92.0.205
  221.181.185.135
  222.186.42.213
  87.241.1.186
  221.181.185.153
  221.181.185.198
  221.181.185.159
  . 
  . .
  . . .
  ```
  
<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [Black Hills Information Security](https://www.youtube.com/watch?v=6j0zjmaYcXs&t=3241s)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/ocastaneda3/multilayer-perceptron.svg?style=for-the-badge
[contributors-url]: https://github.com/ocastaneda3/multilayer-perceptron/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/ocastaneda3/multilayer-perceptron.svg?style=for-the-badge
[forks-url]: https://github.com/ocastaneda3/multilayer-perceptron/network/members
[stars-shield]: https://img.shields.io/github/stars/ocastaneda3/multilayer-perceptron.svg?style=for-the-badge
[stars-url]: https://github.com/ocastaneda3/multilayer-perceptron/stargazers
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/oscar-castaneda93/
[license-shield]: https://img.shields.io/github/license/ocastaneda3/log_analyzer.svg?style=for-the-badge
[license-url]: https://github.com/ocastaneda3/log_analyzer/blob/main/LICENSE
