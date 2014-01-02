# -*- coding: utf-8 -*-
#
# Copyright 2013 - Mirantis, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

"""
Configuration options registration and useful routines.
"""

from oslo.config import cfg

from mistral.openstack.common import log
from mistral import version


api_opts = [
    cfg.StrOpt('host', default='0.0.0.0', help='Mistral API server host'),
    cfg.IntOpt('port', default=8989, help='Mistral API server port')
]

db_opts = [
    # TODO: add DB properties.
]

rabbit_opts = [
    cfg.StrOpt('rabbit_host', default='0.0.0.0',
               help='RabbitMQ server host name'),
    cfg.IntOpt('rabbit_port', default=5672, help='RabbitMQ server port'),
    cfg.StrOpt('rabbit_virtual_host', default='/',
               help='RabbitMQ server virtual host name'),
    cfg.StrOpt('rabbit_task_queue', default='tasks',
               help='RabbitMQ tasks queue name'),
    cfg.StrOpt('rabbit_user', default='guest', help='RabbitMQ user'),
    cfg.StrOpt('rabbit_password', default='guest', help='RabbitMQ password')
]

CONF = cfg.CONF

CONF.register_opts(api_opts, group='api')
CONF.register_opts(db_opts, group='database')
CONF.register_opts(rabbit_opts, group='rabbit')


CONF.import_opt('verbose', 'mistral.openstack.common.log')
CONF.import_opt('debug', 'mistral.openstack.common.log')
CONF.import_opt('log_dir', 'mistral.openstack.common.log')
CONF.import_opt('log_file', 'mistral.openstack.common.log')
CONF.import_opt('log_config_append', 'mistral.openstack.common.log')
CONF.import_opt('log_format', 'mistral.openstack.common.log')
CONF.import_opt('log_date_format', 'mistral.openstack.common.log')
CONF.import_opt('use_syslog', 'mistral.openstack.common.log')
CONF.import_opt('syslog_log_facility', 'mistral.openstack.common.log')


cfg.set_defaults(log.log_opts,
                 default_log_levels=['sqlalchemy=WARN',
                                     'eventlet.wsgi.server=WARN'])


def parse_args(args=None, usage=None, default_config_files=None):
    CONF(args=args,
         project='mistral',
         version=version,
         usage=usage,
         default_config_files=default_config_files)