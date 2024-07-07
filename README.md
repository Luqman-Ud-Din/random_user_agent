Random User Agents
==================

Random User Agents is a python library that provides list of user agents,
from a collection of more than 326,000+ user agents, based on filters.

Some of the filter names which can be passed to `UserAgent()` are listed below:

    operating_systems : [
        UNIX, LINUX, WINDOWS, MAC, ...
    ]

    hardware_types : [
        MOBILE, COMPUTER, SERVER, ...
    ]

    software_types : [
        WEB_BROWSER, BOT__CRAWLER, BOT__ANALYSER, ...
    ]

    software_names : [
       EDGE, CHROME, CHROMIUM, ANDROID, FIREFOX, OPERA, ...
    ]

    software_engines : [
       BLINK, GECKO, WEBKIT, ...
    ]
    
    popularity : [
        POPULAR, COMMON, AVERAGE, ....
    ]


*All filters are available in random_user_agent.params*


Installation
------------

You can install random_useragent by running the following command:

    pip install random_user_agent

Or you can download direct from [Github](https://github.com/Luqman-Ud-Din/random_user_agent) and install it manually.


Usage
-----

To get 100 user agents of browser `chrome` based on operating systems `windows` or `linux`


```python
    from random_user_agent.user_agent import UserAgent
    from random_user_agent.params import SoftwareName, OperatingSystem


    # you can also import SoftwareEngine, HardwareType, SoftwareType, Popularity from random_user_agent.params
    # you can also set number of user agents required by providing `limit` as parameter
    
    software_names = [SoftwareName.CHROME.value]
    operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]   
    
    user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)

    # Get list of user agents.
    user_agents = user_agent_rotator.get_user_agents()

    # Get Random User Agent String.
    user_agent = user_agent_rotator.get_random_user_agent()

```

New in 1.0.2
---

loading from a config file

```python
user_agent_rotator = UserAgent(config_file="mobile_devices.json", limit=100)
```

example config file:

```json
{
    "operating_systems": ["ios", "android"],
    "software_names": ["safari", "chrome"]
}
```

all params values can be found in [params.py](random_user_agent/params.py)

all params for config files: 

```json
{
    "hardware_types": [],
    "software_types": [],
    "software_names": [],
    "software_engines": [],
    "operating_systems": [],
    "popularity": []
}
```

License
-------
The MIT License (MIT). Please see [License File](https://github.com/Luqman-Ud-Din/random_user_agent/blob/master/LICENSE) for more information.


User Agents Source
-------
special thanks to [whatismybrowser](https://developers.whatismybrowser.com/) for providing real user agents.
