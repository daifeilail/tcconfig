**tcconfig**

.. contents:: Table of Contents
   :depth: 2

Summary
=========
A tc command wrapper. Easy to set up traffic control of network bandwidth/latency/packet-loss/packet-corruption/etc. to a network-interface/Docker-container(veth).

.. image:: https://badge.fury.io/py/tcconfig.svg
    :target: https://badge.fury.io/py/tcconfig

.. image:: https://img.shields.io/pypi/pyversions/tcconfig.svg
   :target: https://pypi.org/project/tcconfig

.. image:: https://travis-ci.org/thombashi/tcconfig.svg?branch=master
   :target: https://travis-ci.org/thombashi/tcconfig
   :alt: Linux CI test status

.. image:: https://img.shields.io/github/stars/thombashi/tcconfig.svg?style=social&label=Star
   :target: https://github.com/thombashi/tcconfig
   :alt: GitHub repository

Traffic control
------------------------

Setup traffic shaping rules
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Easy to apply traffic shaping rules to specific network:

- Outgoing/Incoming packets
- Source/Destination IP-address/network (IPv4/IPv6)
- Source/Destination ports

Available parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The following parameters can be set to network interfaces:

- Network bandwidth rate ``[G/M/K bps]``
- Network latency ``[microseconds/milliseconds/seconds/minutes]``
- Packet loss rate ``[%]``
- Packet corruption rate ``[%]``
- Packet duplicate rate ``[%]``
- Packet reordering rate  ``[%]``

Targets
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Network interfaces: e.g. ``eth0``
- Docker container (``veth`` corresponding with a container)

.. image:: docs/gif/tcset_example.gif

Usage
=======
Set traffic control (``tcset`` command)
-----------------------------------------
``tcset`` is a command to add traffic control rule to a network interface (device).

e.g. Set a limit on bandwidth up to 100Kbps
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: console

    # tcset eth0 --rate 100Kbps

e.g. Set network latency
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
You can use time units (such as us/sec/min/etc.) to designate delay time.

Set 100 milliseconds network latency
'''''''''''''''''''''''''''''''''''''''''''''''''''
.. code-block:: console

    # tcset eth0 --delay 100ms


Set 10 seconds network latency
'''''''''''''''''''''''''''''''''''''''''''''''''''
.. code-block:: console

    # tcset eth0 --delay 10sec

Set 0.5 minutes (30 seconds) network latency
'''''''''''''''''''''''''''''''''''''''''''''''''''
.. code-block:: console

    # tcset eth0 --delay 0.5min

You can also use the following units:

- m/min/mins/minute/minutes
- s/sec/secs/second/seconds
- ms/msec/msecs/millisecond/milliseconds
- us/usec/usecs/microsecond/microseconds

e.g. Set 0.1% packet loss
^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: console

    # tcset eth0 --loss 0.1

e.g. All of the above settings at once
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: console

    # tcset eth0 --rate 100Kbps --delay 100ms --loss 0.1

e.g. Specify the IP address of traffic control
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: console

    # tcset eth0 --delay 100ms --network 192.168.0.10

e.g. Specify the IP network and port of traffic control
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: console

    # tcset eth0 --delay 100ms --network 192.168.0.0/24 --port 80

Delete traffic control (``tcdel`` command)
------------------------------------------
``tcdel`` is a command to delete traffic shaping rules from a network interface (device).

e.g. Delete traffic control of ``eth0``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
You can delete all of the shaping rules for the ``eth0`` with ``-a``/``--all`` option:

.. code-block:: console

    # tcdel eth0 --all

Display traffic control configurations (``tcshow`` command)
-----------------------------------------------------------
``tcshow`` is a command to display the current traffic control settings for network interface(s).

Example
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

    # tcset eth0 --delay 10 --delay-distro 2  --loss 0.01 --rate 0.25M --network 192.168.0.10 --port 8080
    # tcset eth0 --delay 1 --loss 0.02 --rate 500K --direction incoming
    # tcshow eth0
    {
        "eth0": {
            "outgoing": {
                "dst-network=192.168.0.10/32, dst-port=8080, protocol=ip": {
                    "filter_id": "800::800",
                    "delay": "10.0ms",
                    "delay-distro": "2.0ms",
                    "loss": 0.01,
                    "rate": "250Kbps"
                }
            },
            "incoming": {
                "protocol=ip": {
                    "filter_id": "800::800",
                    "delay": "1.0ms",
                    "loss": 0.02,
                    "rate": "500Kbps"
                }
            }
        }
    }

For more information
----------------------
More examples are available at 
https://tcconfig.rtfd.io/en/latest/pages/usage/index.html



Installation
============
Install via pip (recommended)
------------------------------
``tcconfig`` can be installed from `PyPI <https://pypi.python.org/pypi>`__ via
`pip <https://pip.pypa.io/en/stable/installing/>`__ (Python package manager) command.

.. code:: console

    sudo pip install tcconfig


Install in Debian/Ubuntu from a deb package
--------------------------------------------
#. ``wget https://github.com/thombashi/tcconfig/releases/download/<version>/tcconfig_<version>_amd64.deb``
#. ``dpkg -iv tcconfig_<version>_amd64.deb``

:Example:
    .. code:: console

        $ wget https://github.com/thombashi/tcconfig/releases/download/v0.19.0/tcconfig_0.19.0_amd64.deb
        $ sudo dpkg -i tcconfig_0.19.0_amd64.deb


Dependencies
============
Python 2.7+ or 3.4+

Linux packages
--------------
- mandatory: required for ``tc`` command:
    - `Ubuntu`/`Debian`: ``iproute2``
    - `Fedora`/`RHEL`: ``iproute-tc``
- optional: required to when you use ``--iptables`` option:
    - ``iptables``

Linux kernel module
----------------------------
- ``sch_netem``

Python packages
---------------
Dependency python packages are automatically installed during
``tcconfig`` installation via pip.

- `DataPropery <https://github.com/thombashi/DataProperty>`__
- `ipaddress <https://pypi.org/project/ipaddress>`__
- `logbook <https://logbook.readthedocs.io/en/stable/>`__
- `msgfy <https://github.com/thombashi/msgfy>`__
- `pyparsing <https://github.com/pyparsing/pyparsing//>`__
- `six <https://pypi.org/project/six/>`__
- `subprocrunner <https://github.com/thombashi/subprocrunner>`__
- `typepy <https://github.com/thombashi/typepy>`__
- `voluptuous <https://github.com/alecthomas/voluptuous>`__

Optional Python packages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- `netifaces <https://github.com/al45tair/netifaces>`__
    - Suppress excessive error messages if this package installed
- `Pygments <http://pygments.org/>`__

Test dependencies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- `allpairspy <https://github.com/thombashi/allpairspy>`__
- `pingparsing <https://github.com/thombashi/pingparsing>`__
- `pytest <https://docs.pytest.org/en/latest/>`__
- `pytest-runner <https://github.com/pytest-dev/pytest-runner>`__
- `tox <https://testrun.org/tox/latest/>`__

Documentation
===============
https://tcconfig.rtfd.io/

Troubleshooting
=================
https://tcconfig.rtfd.io/en/latest/pages/troubleshooting.html

Docker image
==============
https://hub.docker.com/r/thombashi/tcconfig/

