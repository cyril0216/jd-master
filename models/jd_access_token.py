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

        #
        # '''账户信息'''
        # userName = 'zhsz'
        # passWord = '123456'
        # url = 'https://igh.zolbon.com:18081/sys/oauth/token'
        # data = {'userName': userName, 'passWord': passWord}
        # rawdata = self.env['dt_access_token'].sudo().search([])
        #
        # res = json.loads(str(requests.post(url=url, json=data).text))
        #
        # data_list = res['data']
        # proInfo = data_list['proInfo']
        #
        # access_token = data_list['access_token']
        # expires_in = data_list['expires_in']
        # user_id = data_list['user_id']
        # for i in proInfo:
        #     projectid = i['projectId']
        #     projectname = i['projectName']
        #
        #
        # rawdata = self.env['dt_access_token'].sudo().search([])
        #
        #
        # values = {
        #     'access_token': access_token,
        #     'expires_in': expires_in,
        #     'user_id': user_id,
        #     'projectid': projectid,
        #     'projectname': projectname,
        # }
        #
        # try:
        #     rawdata = self.env[self._name].sudo().search([('user_id', '=', user_id)])
        #     if rawdata:
        #         self.env[self._name].sudo().write(values)
        #         print('更新token成功')
        #
        #     else:
        #         self.env[self._name].sudo().create(values)
        #         print('获取token成功')
        #
        # except Exception as err:
        #     print('更新token错误', err)
        #
        #
        #
        #
        pass

    


        





