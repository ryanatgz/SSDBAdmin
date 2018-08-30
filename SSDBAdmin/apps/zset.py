# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     zset
   Description :   zset view
   Author :        JHao
   date：          2018/8/30
-------------------------------------------------
   Change Activity:
                   2018/8/30: zset view
-------------------------------------------------
"""
__author__ = 'JHao'

from SSDBAdmin import app
from SSDBAdmin.model.SSDBClient import SSDBClient
from SSDBAdmin.utils.paginator import getPagingTabsInfo
from flask import render_template, request, make_response, redirect, url_for


@app.route('/ssdbadmin/zset/')
def zsetLists():
    """
    show the items of zset
    :return:
    """
    page_num = int(request.args.get('page_num', 1))
    page_size = request.args.get('page_size')
    if not page_size:
        page_size = request.cookies.get('SIZE', 20)
    start = request.args.get('start', '')
    db_client = SSDBClient(request)
    zset_list, has_next = db_client.zsetList(start=start, page_num=page_num, page_size=int(page_size))
    select_arg = {'start': start, 'page_size': int(page_size)}
    resp = make_response(render_template('zset/zset.html', zset_list=zset_list, has_next=has_next,
                                         has_prev=page_num > 1,
                                         page_num=page_num, select_arg=select_arg, active='zset'))
    resp.set_cookie('SIZE', str(page_size))
    return resp


@app.route('/ssdbadmin/zset/zset/', methods=['GET', 'POST'])
def zset_zset():
    """
    add item to queue(support back and front)
    :return:
    """
    pass


@app.route('/ssdbadmin/zset/zscan/')
def zset_zscan():
    """
    show the list of item from queue
    :return:
    """
    name = request.args.get('name')
    key_start = request.args.get('start', '')
    tp = request.args.get('type')
    page_size = request.args.get('page_size')
    if not page_size:
        page_size = request.cookies.get('SIZE', 20)
    ssdb_object = SSDBObject(request)
    has_next, has_prev, item_list = ssdb_object.zset_zscan(name, key_start, tp, limit=int(page_size))
    prev_s, next_s = '', ''
    if item_list:
        next_s = item_list[-1].get('key')
        prev_s = item_list[0].get('key')
    select_arg = {'page_size': int(page_size), 'prev_s': prev_s, 'next_s': next_s}
    resp = make_response(render_template('zset/zset_zscan.html',
                                         item_list=item_list,
                                         name=name,
                                         page_num=1,
                                         key_start=key_start,
                                         has_next=has_next,
                                         has_prev=has_prev,
                                         select_arg=select_arg,
                                         active='zset'))
    resp.set_cookie('SIZE', str(page_size))
    return resp


@app.route('/ssdbadmin/zset/zdel/', methods=['GET', 'POST'])
def zset_zdel():
    """
    remove keys from zset_name
    :return:
    """
    pass


@app.route('/ssdbadmin/zset/zclear/', methods=['GET', 'POST'])
def zset_zclear():
    """
    delete  the specified zset data
    :return:
    """
    pass


@app.route('/ssdbadmin/zset/zget/')
def zset_zget():
    """
    show an item info from zset
    :return:
    """
    pass
