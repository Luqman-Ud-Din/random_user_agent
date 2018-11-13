Random User Agents
==================

Random User Agents is a python library that provides list of user agents,
from a collection of more than 180,000+ user agents, based on filters.

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


*All filters are available in random_user_agent.params*


Installation
------------

You can install random_useragent by running the following command:

    pip install random_user_agent

Or you can download direct from [Github](https://github.com/Luqman-Ud-Din/random_user_agent) and install it manually.


Usage
-----

To get user agents of browser `chrome` based on operating systems `windows` or `linux`


```python
    from random_user_agent.user_agent import UserAgent
    from random_user_agent.params import SoftwareNames, OperatingSystems


    # you can also import SoftwareEngines, HardwareTypes, SoftwareTypes from random_user_agent.params


    user_agent_rotator = UserAgent(software_names=[SoftwareNames.CHROME.value], operating_systems=[OperatingSystems.WINDOWS.value])

    # Get list of user agents.
    user_agents = user_agent_rotator.get_user_agents()

    # Get Random User Agent String.
    user_agent = user_agent_rotator.get_random_user_agent()

    # list all available operating systems
    operating_systems = user_agent_rotator.get_operating_systems()

    # list all available software names
    operating_systems = user_agent_rotator.get_software_names()

    # list all available software rendering engines
    operating_systems = user_agent_rotator.get_software_engines()

    # list all available software types
    operating_systems = user_agent_rotator.get_software_types()

    # list all available hardwrae types
    operating_systems = user_agent_rotator.get_hardware_types()

```

License
-------
The MIT License (MIT). Please see [License File](https://github.com/Luqman-Ud-Din/random_user_agent/blob/master/LICENSE) for more information.


User Agents Source
-------
special thanks to [whatismybrowser](https://developers.whatismybrowser.com/) for providing real user agents.
