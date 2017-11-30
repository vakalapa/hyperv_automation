#!/usr/bin/env python
# coding: utf-8

import xmlrpc.client

with xmlrpc.client.ServerProxy("http://172.18.40.59:8000/") as proxy:
    print("3 is even: %s" % str(proxy.is_even(3)))
    print("100 is even: %s" % str(proxy.is_even(100)))