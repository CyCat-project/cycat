#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Verifying and building CyCAT.org url
#
# Software is free software released under the "2-Clause BSD License"
#
# This software is part of cycat.org Python library
#
# Copyright (c) 2021 Alexandre Dulaunoy - a@foo.be

import uuid
import re

def generate(publisher=None, project=None):
    """Generate a CyCAT.org url for an item without associated UUID. The output url
    is a fixed value based on the CyCAT namespace, the publisher and the UUID
    hashed value from the publisher and project."""
    if publisher is None or project is None:
        return False
    _uuid = uuid.uuid5(uuid.UUID("690b3b43-d689-481c-aa61-5351963a36f2"), "{}:{}:".format(publisher, project))
    return "{}:{}:{}".format(publisher.lower(), project.lower(), _uuid)

def validate(url=None):
    """Validate a CyCAT.org url format including its UUID."""
    if url is None:
        return False
    val = url.split(':')
    if len(val) != 3:
        return False
    try:
        _val = uuid.UUID(val[2])
    except ValueError:
        return False
    return True

def build(publisher=None, project=None, uuid=None):
    """Generate a valid CyCAT.url based on the existing publisher, project and
    UUID."""
    if publisher is None or project is None or uuid is None:
        return False
    _url = "{}:{}:{}".format(publisher.lower(), project.lower(), uuid)
    if validate(url=_url):
        return _url
    else:
        return False

