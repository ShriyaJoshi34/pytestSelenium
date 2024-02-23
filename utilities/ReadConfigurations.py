from configparser import ConfigParser


def read_configuration(section, key):
    config = ConfigParser()
    # file = open("../configurations/config.ini", "r")
    config.read('configurations/config.ini')
    return config.get(section, key)
