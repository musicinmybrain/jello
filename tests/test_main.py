#!/usr/bin/env python3

import unittest
import jello.cli


class MyTests(unittest.TestCase):

    def setUp(self):
        self.data_in = '''{"name": "jc", "version": "1.9.3", "description": "jc cli output JSON conversion tool", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "parser_count": 50, "parsers": [{"name": "airport", "argument": "--airport", "version": "1.0", "description": "airport -I command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["darwin"], "magic_commands": ["airport -I"]}, {"name": "airport_s", "argument": "--airport-s", "version": "1.0", "description": "airport -s command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["darwin"], "magic_commands": ["airport -s"]}, {"name": "arp", "argument": "--arp", "version": "1.2", "description": "arp command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux", "aix", "freebsd", "darwin"], "magic_commands": ["arp"]}, {"name": "blkid", "argument": "--blkid", "version": "1.0", "description": "blkid command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux"], "magic_commands": ["blkid"]}, {"name": "crontab", "argument": "--crontab", "version": "1.1", "description": "crontab command and file parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux", "darwin", "aix", "freebsd"], "magic_commands": ["crontab"]}, {"name": "crontab_u", "argument": "--crontab-u", "version": "1.0", "description": "crontab file parser with user support", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux", "darwin", "aix", "freebsd"]}, {"name": "csv", "argument": "--csv", "version": "1.0", "description": "CSV file parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "details": "Using the python standard csv library", "compatible": ["linux", "darwin", "cygwin", "win32", "aix", "freebsd"]}, {"name": "df", "argument": "--df", "version": "1.1", "description": "df command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux", "darwin"], "magic_commands": ["df"]}, {"name": "dig", "argument": "--dig", "version": "1.1", "description": "dig command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux", "aix", "freebsd", "darwin"], "magic_commands": ["dig"]}, {"name": "du", "argument": "--du", "version": "1.1", "description": "du command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux", "darwin", "aix", "freebsd"], "magic_commands": ["du"]}, {"name": "env", "argument": "--env", "version": "1.1", "description": "env command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux", "darwin", "cygwin", "win32", "aix", "freebsd"], "magic_commands": ["env"]}, {"name": "file", "argument": "--file", "version": "1.1", "description": "file command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux", "aix", "freebsd", "darwin"], "magic_commands": ["file"]}, {"name": "free", "argument": "--free", "version": "1.0", "description": "free command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux"], "magic_commands": ["free"]}, {"name": "fstab", "argument": "--fstab", "version": "1.0", "description": "fstab file parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux"]}, {"name": "group", "argument": "--group", "version": "1.0", "description": "/etc/group file parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux", "darwin", "aix", "freebsd"]}, {"name": "gshadow", "argument": "--gshadow", "version": "1.0", "description": "/etc/gshadow file parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux", "aix", "freebsd"]}, {"name": "history", "argument": "--history", "version": "1.2", "description": "history command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "details": "Optimizations by https://github.com/philippeitis", "compatible": ["linux", "darwin", "cygwin", "aix", "freebsd"]}, {"name": "hosts", "argument": "--hosts", "version": "1.0", "description": "/etc/hosts file parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux", "darwin", "cygwin", "win32", "aix", "freebsd"]}, {"name": "id", "argument": "--id", "version": "1.0", "description": "id command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux", "darwin", "aix", "freebsd"], "magic_commands": ["id"]}, {"name": "ifconfig", "argument": "--ifconfig", "version": "1.5", "description": "ifconfig command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "details": "Using ifconfig-parser package from https://github.com/KnightWhoSayNi/ifconfig-parser", "compatible": ["linux", "aix", "freebsd", "darwin"], "magic_commands": ["ifconfig"]}, {"name": "ini", "argument": "--ini", "version": "1.0", "description": "INI file parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "details": "Using configparser from the standard library", "compatible": ["linux", "darwin", "cygwin", "win32", "aix", "freebsd"]}, {"name": "iptables", "argument": "--iptables", "version": "1.1", "description": "iptables command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux"], "magic_commands": ["iptables"]}, {"name": "jobs", "argument": "--jobs", "version": "1.0", "description": "jobs command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux", "darwin", "cygwin", "aix", "freebsd"], "magic_commands": ["jobs"]}, {"name": "last", "argument": "--last", "version": "1.0", "description": "last and lastb command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux", "darwin", "aix", "freebsd"], "magic_commands": ["last", "lastb"]}, {"name": "ls", "argument": "--ls", "version": "1.3", "description": "ls command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux", "darwin", "cygwin", "aix", "freebsd"], "magic_commands": ["ls"]}, {"name": "lsblk", "argument": "--lsblk", "version": "1.3", "description": "lsblk command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux"], "magic_commands": ["lsblk"]}, {"name": "lsmod", "argument": "--lsmod", "version": "1.1", "description": "lsmod command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux"], "magic_commands": ["lsmod"]}, {"name": "lsof", "argument": "--lsof", "version": "1.0", "description": "lsof command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux"], "magic_commands": ["lsof"]}, {"name": "mount", "argument": "--mount", "version": "1.1", "description": "mount command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux", "darwin"], "magic_commands": ["mount"]}, {"name": "netstat", "argument": "--netstat", "version": "1.2", "description": "netstat command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux"], "magic_commands": ["netstat"]}, {"name": "ntpq", "argument": "--ntpq", "version": "1.0", "description": "ntpq -p command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux"], "magic_commands": ["ntpq"]}, {"name": "passwd", "argument": "--passwd", "version": "1.0", "description": "/etc/passwd file parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux", "darwin", "aix", "freebsd"]}, {"name": "pip_list", "argument": "--pip-list", "version": "1.0", "description": "pip list command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux", "darwin", "cygwin", "win32", "aix", "freebsd"], "magic_commands": ["pip list", "pip3 list"]}, {"name": "pip_show", "argument": "--pip-show", "version": "1.0", "description": "pip show command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux", "darwin", "cygwin", "win32", "aix", "freebsd"], "magic_commands": ["pip show", "pip3 show"]}, {"name": "ps", "argument": "--ps", "version": "1.1", "description": "ps command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux", "darwin", "cygwin", "aix", "freebsd"], "magic_commands": ["ps"]}, {"name": "route", "argument": "--route", "version": "1.0", "description": "route command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux"], "magic_commands": ["route"]}, {"name": "shadow", "argument": "--shadow", "version": "1.0", "description": "/etc/shadow file parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux", "darwin", "aix", "freebsd"]}, {"name": "ss", "argument": "--ss", "version": "1.0", "description": "ss command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux"], "magic_commands": ["ss"]}, {"name": "stat", "argument": "--stat", "version": "1.0", "description": "stat command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux"], "magic_commands": ["stat"]}, {"name": "systemctl", "argument": "--systemctl", "version": "1.0", "description": "systemctl command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux"], "magic_commands": ["systemctl"]}, {"name": "systemctl_lj", "argument": "--systemctl-lj", "version": "1.0", "description": "systemctl list-jobs command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux"], "magic_commands": ["systemctl list-jobs"]}, {"name": "systemctl_ls", "argument": "--systemctl-ls", "version": "1.0", "description": "systemctl list-sockets command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux"], "magic_commands": ["systemctl list-sockets"]}, {"name": "systemctl_luf", "argument": "--systemctl-luf", "version": "1.0", "description": "systemctl list-unit-files command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux"], "magic_commands": ["systemctl list-unit-files"]}, {"name": "timedatectl", "argument": "--timedatectl", "version": "1.0", "description": "timedatectl status command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux"], "magic_commands": ["timedatectl", "timedatectl status"]}, {"name": "uname", "argument": "--uname", "version": "1.1", "description": "uname -a command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux", "darwin"], "magic_commands": ["uname"]}, {"name": "uptime", "argument": "--uptime", "version": "1.0", "description": "uptime command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux", "darwin", "cygwin", "aix", "freebsd"], "magic_commands": ["uptime"]}, {"name": "w", "argument": "--w", "version": "1.0", "description": "w command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux", "darwin", "cygwin", "aix", "freebsd"], "magic_commands": ["w"]}, {"name": "who", "argument": "--who", "version": "1.0", "description": "who command parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "compatible": ["linux", "darwin", "cygwin", "aix", "freebsd"], "magic_commands": ["who"]}, {"name": "xml", "argument": "--xml", "version": "1.0", "description": "XML file parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "details": "Using the xmltodict library at https://github.com/martinblech/xmltodict", "compatible": ["linux", "darwin", "cygwin", "win32", "aix", "freebsd"]}, {"name": "yaml", "argument": "--yaml", "version": "1.0", "description": "YAML file parser", "author": "Kelly Brazil", "author_email": "kellyjonbrazil@gmail.com", "details": "Using the ruamel.yaml library at https://pypi.org/project/ruamel.yaml", "compatible": ["linux", "darwin", "cygwin", "win32", "aix", "freebsd"]}]}'''

    def test_jc_a(self):
        """
        Test jc -a
        """
        self.expected = '''\
{
  "name": "jc",
  "version": "1.9.3",
  "description": "jc cli output JSON conversion tool",
  "author": "Kelly Brazil",
  "author_email": "kellyjonbrazil@gmail.com",
  "parser_count": 50,
  "parsers": [
    {
      "name": "airport",
      "argument": "--airport",
      "version": "1.0",
      "description": "airport -I command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "darwin"
      ],
      "magic_commands": [
        "airport -I"
      ]
    },
    {
      "name": "airport_s",
      "argument": "--airport-s",
      "version": "1.0",
      "description": "airport -s command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "darwin"
      ],
      "magic_commands": [
        "airport -s"
      ]
    },
    {
      "name": "arp",
      "argument": "--arp",
      "version": "1.2",
      "description": "arp command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux",
        "aix",
        "freebsd",
        "darwin"
      ],
      "magic_commands": [
        "arp"
      ]
    },
    {
      "name": "blkid",
      "argument": "--blkid",
      "version": "1.0",
      "description": "blkid command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux"
      ],
      "magic_commands": [
        "blkid"
      ]
    },
    {
      "name": "crontab",
      "argument": "--crontab",
      "version": "1.1",
      "description": "crontab command and file parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux",
        "darwin",
        "aix",
        "freebsd"
      ],
      "magic_commands": [
        "crontab"
      ]
    },
    {
      "name": "crontab_u",
      "argument": "--crontab-u",
      "version": "1.0",
      "description": "crontab file parser with user support",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux",
        "darwin",
        "aix",
        "freebsd"
      ]
    },
    {
      "name": "csv",
      "argument": "--csv",
      "version": "1.0",
      "description": "CSV file parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "details": "Using the python standard csv library",
      "compatible": [
        "linux",
        "darwin",
        "cygwin",
        "win32",
        "aix",
        "freebsd"
      ]
    },
    {
      "name": "df",
      "argument": "--df",
      "version": "1.1",
      "description": "df command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux",
        "darwin"
      ],
      "magic_commands": [
        "df"
      ]
    },
    {
      "name": "dig",
      "argument": "--dig",
      "version": "1.1",
      "description": "dig command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux",
        "aix",
        "freebsd",
        "darwin"
      ],
      "magic_commands": [
        "dig"
      ]
    },
    {
      "name": "du",
      "argument": "--du",
      "version": "1.1",
      "description": "du command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux",
        "darwin",
        "aix",
        "freebsd"
      ],
      "magic_commands": [
        "du"
      ]
    },
    {
      "name": "env",
      "argument": "--env",
      "version": "1.1",
      "description": "env command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux",
        "darwin",
        "cygwin",
        "win32",
        "aix",
        "freebsd"
      ],
      "magic_commands": [
        "env"
      ]
    },
    {
      "name": "file",
      "argument": "--file",
      "version": "1.1",
      "description": "file command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux",
        "aix",
        "freebsd",
        "darwin"
      ],
      "magic_commands": [
        "file"
      ]
    },
    {
      "name": "free",
      "argument": "--free",
      "version": "1.0",
      "description": "free command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux"
      ],
      "magic_commands": [
        "free"
      ]
    },
    {
      "name": "fstab",
      "argument": "--fstab",
      "version": "1.0",
      "description": "fstab file parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux"
      ]
    },
    {
      "name": "group",
      "argument": "--group",
      "version": "1.0",
      "description": "/etc/group file parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux",
        "darwin",
        "aix",
        "freebsd"
      ]
    },
    {
      "name": "gshadow",
      "argument": "--gshadow",
      "version": "1.0",
      "description": "/etc/gshadow file parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux",
        "aix",
        "freebsd"
      ]
    },
    {
      "name": "history",
      "argument": "--history",
      "version": "1.2",
      "description": "history command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "details": "Optimizations by https://github.com/philippeitis",
      "compatible": [
        "linux",
        "darwin",
        "cygwin",
        "aix",
        "freebsd"
      ]
    },
    {
      "name": "hosts",
      "argument": "--hosts",
      "version": "1.0",
      "description": "/etc/hosts file parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux",
        "darwin",
        "cygwin",
        "win32",
        "aix",
        "freebsd"
      ]
    },
    {
      "name": "id",
      "argument": "--id",
      "version": "1.0",
      "description": "id command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux",
        "darwin",
        "aix",
        "freebsd"
      ],
      "magic_commands": [
        "id"
      ]
    },
    {
      "name": "ifconfig",
      "argument": "--ifconfig",
      "version": "1.5",
      "description": "ifconfig command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "details": "Using ifconfig-parser package from https://github.com/KnightWhoSayNi/ifconfig-parser",
      "compatible": [
        "linux",
        "aix",
        "freebsd",
        "darwin"
      ],
      "magic_commands": [
        "ifconfig"
      ]
    },
    {
      "name": "ini",
      "argument": "--ini",
      "version": "1.0",
      "description": "INI file parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "details": "Using configparser from the standard library",
      "compatible": [
        "linux",
        "darwin",
        "cygwin",
        "win32",
        "aix",
        "freebsd"
      ]
    },
    {
      "name": "iptables",
      "argument": "--iptables",
      "version": "1.1",
      "description": "iptables command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux"
      ],
      "magic_commands": [
        "iptables"
      ]
    },
    {
      "name": "jobs",
      "argument": "--jobs",
      "version": "1.0",
      "description": "jobs command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux",
        "darwin",
        "cygwin",
        "aix",
        "freebsd"
      ],
      "magic_commands": [
        "jobs"
      ]
    },
    {
      "name": "last",
      "argument": "--last",
      "version": "1.0",
      "description": "last and lastb command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux",
        "darwin",
        "aix",
        "freebsd"
      ],
      "magic_commands": [
        "last",
        "lastb"
      ]
    },
    {
      "name": "ls",
      "argument": "--ls",
      "version": "1.3",
      "description": "ls command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux",
        "darwin",
        "cygwin",
        "aix",
        "freebsd"
      ],
      "magic_commands": [
        "ls"
      ]
    },
    {
      "name": "lsblk",
      "argument": "--lsblk",
      "version": "1.3",
      "description": "lsblk command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux"
      ],
      "magic_commands": [
        "lsblk"
      ]
    },
    {
      "name": "lsmod",
      "argument": "--lsmod",
      "version": "1.1",
      "description": "lsmod command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux"
      ],
      "magic_commands": [
        "lsmod"
      ]
    },
    {
      "name": "lsof",
      "argument": "--lsof",
      "version": "1.0",
      "description": "lsof command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux"
      ],
      "magic_commands": [
        "lsof"
      ]
    },
    {
      "name": "mount",
      "argument": "--mount",
      "version": "1.1",
      "description": "mount command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux",
        "darwin"
      ],
      "magic_commands": [
        "mount"
      ]
    },
    {
      "name": "netstat",
      "argument": "--netstat",
      "version": "1.2",
      "description": "netstat command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux"
      ],
      "magic_commands": [
        "netstat"
      ]
    },
    {
      "name": "ntpq",
      "argument": "--ntpq",
      "version": "1.0",
      "description": "ntpq -p command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux"
      ],
      "magic_commands": [
        "ntpq"
      ]
    },
    {
      "name": "passwd",
      "argument": "--passwd",
      "version": "1.0",
      "description": "/etc/passwd file parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux",
        "darwin",
        "aix",
        "freebsd"
      ]
    },
    {
      "name": "pip_list",
      "argument": "--pip-list",
      "version": "1.0",
      "description": "pip list command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux",
        "darwin",
        "cygwin",
        "win32",
        "aix",
        "freebsd"
      ],
      "magic_commands": [
        "pip list",
        "pip3 list"
      ]
    },
    {
      "name": "pip_show",
      "argument": "--pip-show",
      "version": "1.0",
      "description": "pip show command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux",
        "darwin",
        "cygwin",
        "win32",
        "aix",
        "freebsd"
      ],
      "magic_commands": [
        "pip show",
        "pip3 show"
      ]
    },
    {
      "name": "ps",
      "argument": "--ps",
      "version": "1.1",
      "description": "ps command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux",
        "darwin",
        "cygwin",
        "aix",
        "freebsd"
      ],
      "magic_commands": [
        "ps"
      ]
    },
    {
      "name": "route",
      "argument": "--route",
      "version": "1.0",
      "description": "route command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux"
      ],
      "magic_commands": [
        "route"
      ]
    },
    {
      "name": "shadow",
      "argument": "--shadow",
      "version": "1.0",
      "description": "/etc/shadow file parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux",
        "darwin",
        "aix",
        "freebsd"
      ]
    },
    {
      "name": "ss",
      "argument": "--ss",
      "version": "1.0",
      "description": "ss command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux"
      ],
      "magic_commands": [
        "ss"
      ]
    },
    {
      "name": "stat",
      "argument": "--stat",
      "version": "1.0",
      "description": "stat command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux"
      ],
      "magic_commands": [
        "stat"
      ]
    },
    {
      "name": "systemctl",
      "argument": "--systemctl",
      "version": "1.0",
      "description": "systemctl command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux"
      ],
      "magic_commands": [
        "systemctl"
      ]
    },
    {
      "name": "systemctl_lj",
      "argument": "--systemctl-lj",
      "version": "1.0",
      "description": "systemctl list-jobs command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux"
      ],
      "magic_commands": [
        "systemctl list-jobs"
      ]
    },
    {
      "name": "systemctl_ls",
      "argument": "--systemctl-ls",
      "version": "1.0",
      "description": "systemctl list-sockets command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux"
      ],
      "magic_commands": [
        "systemctl list-sockets"
      ]
    },
    {
      "name": "systemctl_luf",
      "argument": "--systemctl-luf",
      "version": "1.0",
      "description": "systemctl list-unit-files command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux"
      ],
      "magic_commands": [
        "systemctl list-unit-files"
      ]
    },
    {
      "name": "timedatectl",
      "argument": "--timedatectl",
      "version": "1.0",
      "description": "timedatectl status command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux"
      ],
      "magic_commands": [
        "timedatectl",
        "timedatectl status"
      ]
    },
    {
      "name": "uname",
      "argument": "--uname",
      "version": "1.1",
      "description": "uname -a command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux",
        "darwin"
      ],
      "magic_commands": [
        "uname"
      ]
    },
    {
      "name": "uptime",
      "argument": "--uptime",
      "version": "1.0",
      "description": "uptime command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux",
        "darwin",
        "cygwin",
        "aix",
        "freebsd"
      ],
      "magic_commands": [
        "uptime"
      ]
    },
    {
      "name": "w",
      "argument": "--w",
      "version": "1.0",
      "description": "w command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux",
        "darwin",
        "cygwin",
        "aix",
        "freebsd"
      ],
      "magic_commands": [
        "w"
      ]
    },
    {
      "name": "who",
      "argument": "--who",
      "version": "1.0",
      "description": "who command parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "compatible": [
        "linux",
        "darwin",
        "cygwin",
        "aix",
        "freebsd"
      ],
      "magic_commands": [
        "who"
      ]
    },
    {
      "name": "xml",
      "argument": "--xml",
      "version": "1.0",
      "description": "XML file parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "details": "Using the xmltodict library at https://github.com/martinblech/xmltodict",
      "compatible": [
        "linux",
        "darwin",
        "cygwin",
        "win32",
        "aix",
        "freebsd"
      ]
    },
    {
      "name": "yaml",
      "argument": "--yaml",
      "version": "1.0",
      "description": "YAML file parser",
      "author": "Kelly Brazil",
      "author_email": "kellyjonbrazil@gmail.com",
      "details": "Using the ruamel.yaml library at https://pypi.org/project/ruamel.yaml",
      "compatible": [
        "linux",
        "darwin",
        "cygwin",
        "win32",
        "aix",
        "freebsd"
      ]
    }
  ]
}'''
        self.assertEqual(jello.cli.main(data=self.data_in), self.expected)


if __name__ == '__main__':
    unittest.main()
