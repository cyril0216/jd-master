#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author:Cyril

import os
from jinja2 import Environment, FileSystemLoader

global BASE_DIR
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
global env
templateLoader = FileSystemLoader(searchpath=BASE_DIR + "/templates")
env = Environment(loader=templateLoader)
import logging

_logger = logging.getLogger(__name__)

import odoo
from odoo import http
from odoo.http import request
from odoo.addons.web.controllers.main import WebClient, Binary, Home
import json


class Website(Home):
    pass
