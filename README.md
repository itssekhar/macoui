# [MAC-OUI Lookup] SDK.

## Introduction

[maclookup] is the sdk that provides an interface to lookup a vendor name for a given macaddress. 

- [x] Supported Features
  - [x] [Get vendor name by mac]
  - [x] [Mac validation]
  - [x] [Error hanndling]
  - [x] [Output format. Default is json]
  - [x] [ApiKey based authentication]

## Installation

```

git clone git@github.com:macoui

docker build /home/macoui --file /home/macoui/docker/Dockerfile -t macoui:v1.0

```

## Usage

```

container_id = docker images | grep macoui | awk ' { print $3 } '
docker run -it $container_id /bin/bash

source /home/.virtualenvs/vtest/bin/activate

python maclookup.py --apiKey <YOUR_API_KEY> --macaddress <MAC_ADDRESS>

or 

./maclookup.py --apiKey <YOUR_API_KEY> --macaddress <MAC_ADDRESS>

```

## Example

```

./maclookup.py --apiKey "hidden apikey" --macaddress "44:38:39:ff:ef:57"

Output will be:

{'name': 'Cumulus Networks, Inc'}

```
