import yaml
import tensorflow as tf
from string import Template
from .logger import logger


class Config(object):
    def __init__(self, entries):
        self.__dict__.update(entries)

    def __repr__(self):
        keys = self.__dict__.keys()
        args = ', '.join(['{}={}'.format(key, self.__dict__[key]) for key in keys])
        return '{}({})'.format(self.__class__.__name__, args)


def get_config_from_yaml(yaml_file):
    """
    Get the config from a yaml file
    :param yaml_file:
    :return: config(object) or config(dictionary)
    """
    # parse the configurations from the config yaml file provided
    with open(yaml_file, 'r') as config_file:
        config_dict = yaml.load(config_file)
        config_file.seek(0)
        template_str = config_file.read()

    replaced = Template(template_str).substitute(config_dict)

    config_dict = yaml.load(replaced)

    # convert the dictionary to a object
    config = Config(config_dict)

    return config, config_dict


def create_dirs(dirs):
    """
    dirs - a list of directories to create if these directories are not found
    :param dirs:
    :return exit_code: 0:success -1:failed
    """
    try:
        for _dir in dirs:
            if not tf.gfile.Exists(_dir):
                logger.warn("Path {0} do not exist, will create!".format(_dir))
                tf.gfile.MakeDirs(_dir)
            else:
                logger.warn("Path {0} already exist!".format(_dir))
                # tf.gfile.DeleteRecursively(_dir)
        return 0
    except Exception as err:
        logger.error("Creating directories error: {0}".format(err))
        exit(-1)
