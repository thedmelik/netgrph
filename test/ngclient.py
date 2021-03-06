#!/usr/bin/env python3
#
# Copyright (c) 2016 "Jonathan Yantis"
#
# This file is a part of NetGrph.
#
#    This program is free software: you can redistribute it and/or  modify
#    it under the terms of the GNU Affero General Public License, version 3,
#    as published by the Free Software Foundation.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#    As a special exception, the copyright holders give permission to link the
#    code of portions of this program with the OpenSSL library under certain
#    conditions as described in each individual source file and distribute
#    linked combinations including the program with the OpenSSL library. You
#    must comply with the GNU Affero General Public License in all respects
#    for all of the code used other than as permitted herein. If you modify
#    file(s) with this exception, you may extend this exception to your
#    version of the file(s), but you are not obligated to do so. If you do not
#    wish to do so, delete this exception statement from your version. If you
#    delete this exception statement from all source files in the program,
#    then also delete it in the license file.
#
#
"""
NetGrph API Client
"""
import sys
import requests
import json
import nglib.ngtree.export


user = 'yantisj'
passwd = 'testapi'
url = 'http://localhost:4096'

output = 'JSON'

if len(sys.argv) > 1:
    output = sys.argv[1]

#qlist = ['/netgrph/api/v1.1/devs?group=MDC', '/netgrph/api/v1.1/devs?group=CON&full=1', \
#          '/netgrph/api/v1.1/devs/waringsw1']

qlist = ['/netgrph/api/v1.1/vlans?vrange=200-205', '/netgrph/api/v1.1/devs?full=1&search=cr3.*']


for q in qlist:
    r = requests.get(url + q, auth=(user, passwd), verify=False)

    if r.status_code == 200:
        response = r.json()
        nglib.ngtree.export.exp_ngtree(response, output)
    else:
        print("Request Error:", r.status_code, r.text)
