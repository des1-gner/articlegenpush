#!/bin/bash
sudo yum install git -y
sudo yum install python3-boto
git clone https://github.com/des1-gner/articlegenpush.git
cd articlegenpush
python3 push.py
