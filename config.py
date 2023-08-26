# imports
import sqlalchemy
import logging
import yaml


def create_logger():
    conf_dict = yaml.load(open('logging.conf'), Loader=yaml.FullLoader)
    logging.config.dictConfig(conf_dict)
    return logging.getLogger()


logger = create_logger()
engine = sqlalchemy.create_engine('sqlite:///sqlite/database.db')
