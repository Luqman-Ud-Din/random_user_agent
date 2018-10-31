Random User Agents
==================

Random User Agents is a python library that provides list of user agents,
from a collection of more than 180,000+ user agents, based on filters.

Filter names which can be passed to `UserAgent()` are listed below:

    operating_systems : [
        'a-unix-based-os', 'haiku', 'webos', 'bada', 'symbian', 'windows-phone', 'freebsd',
        'macos', 'ios', 'windows', 'blackberry-os', 'mac', 'windows-mobile', 'linux', 'sunos',
        'beos', 'fire-os', 'chromeos', 'openbsd', 'android', 'mac-os-x', '---'
    ]

    hardware_types : [
        'mobile -> tablet', 'mobile', 'mobile -> ebook-reader', 'mobile -> music-player', 'computer',
        'large-screen -> media-player', 'mobile -> phone', 'mobile -> handheld-game', 'server',
        'large-screen -> game-console', 'large-screen -> tv', '---'
    ]

    software_types : [
        'application -> software-library', 'bot -> analyser', 'bot -> site-monitor',
        'browser -> web-browser', 'bot -> crawler', '---'
    ]

    software_names : [
        'qupzilla', 'opera-mini', 'catchpoint-analyser', 'yandex-search-bot', 'internet-channel', 'netsurf',
        'alertsite-monitoring-bot', 'nokia-browser', 'edge', 'cosmos-crawler', 'rockmelt', 'opera', 'skyfire',
        'k-meleon', 'pale-moon', 'uc-browser', 'yandex-browser', 'netscape-navigator', 'internet-archiver-bot',
        'internet-tv-browser', 'awesomium', 'chromium', 'webtv', 'unknown-browser', 'onebrowser', 'firefox',
        'android-browser', 'webkit-based-browser', 'obigo', 'yodaobot-search-bot', 'blackberry-browser',
        'firefox-focus', 'omniweb', 'dotcom-monitor-bot', 'speedcurve-speed-tester', 'chrome',
        'google-app-engine-software', '---'
    ]

    software_engines : [
        'Goanna', 'Gecko', 'Blink', 'Presto', 'WebKit', '---'
    ]


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


    user_agent_rotator = UserAgent(software_names=['chrome'], operating_systems=['windows', 'linux'])

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
