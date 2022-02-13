# Invenio

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-orange.svg?style=flat-square)](https://opensource.org/licenses/Apache-2.0)
[![Code Style: Black](https://img.shields.io/badge/Code%20Style-Black-black?style=flat-square)](https://github.com/psf/black)
[![pyvers](https://img.shields.io/badge/python-3.6+-blue?style=flat-square)]()

Invenio is a lightweight and easy to use service discovery and load balancer written in Python. It was inspired by [Netflix Eureka](https://github.com/Netflix/eureka).

## Why I created Invenio

There are other FAR BETTER options for service discovery systems e.g Netflix Eureka, Hashicorp Consul, etc. But for me, those services were a bit overkill
and resource demanding. I liked Eureka a lot and used it with Spring Boot extensively. But to me, it felt that Eureka was very closely coupled with AWS (since Netflix uses AWS). And because it was written in Java, it required a lot of resources.

That's the reason I created Invenio, to be a lightweight and simple to use solution for service discovery that comes with minimal features. Invenio uses a very simple round robin/cycle load balancing for accessing a service instance. Usually, it's all you need. But if that is not what you want, then I guess Invenio is not for you.

## Running the server

Make sure you have Python 3.6+ installed. Prior versions might not work since it uses type annotations and some other fancy things that only the newer versions have.

By default, you may not have a config file. But don't worry, Invenio will create the config file (`config.yml`) with default values in the folder from where you run it.

Firstly, install the server's dependencies by running
```bash
$ pip install -r requirements.txt

# or

$ pip3 install -r requirements.txt
```

Now run the server using
```bash
$ python -m invenio

# or

$ python3 -m invenio
```

## Contributing

If you are considering to contribute, thanks a lot! We welcome all contributors here and, you can help out as well.

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.