#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
logging.basicConfig(level=debug, format='%(levelname)s %(asctime)s %(filename)s[line:%(lineno)d] %(message)s',datefmt='%Y-%m-%d')
logging.info('test info')
logging.debug('test debug')
logging.warning('test warning')
logging.error('test error')
logging.critical('test critical')