#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author:Cyril

from datetime import datetime, timedelta
from functools import partial
from itertools import groupby

from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import AccessError, UserError, ValidationError
from odoo.tools.misc import formatLang, get_lang
from odoo.osv import expression
from odoo.tools import float_is_zero, float_compare
from werkzeug.urls import url_encode
import requests, json

class JD_access_token(models.Model):
    _name = "jd_access_token"
    _description = "京东账户相关"
    _log_access = True
    _check_worflow_auto = False
    

    account = fields.Char(string='账户')
    passwd = fields.Integer(string='密码')
    cookie = fields.Char(string='cookie')


    def get_token(self):

        
        pass

    


        





