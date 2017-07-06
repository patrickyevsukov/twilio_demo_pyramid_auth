# Copyright (c) 2017 Patrick Yevsukov. All Rights Reserved.
#
# Use of this source code is governed by the OSI license in the LICENSE file.
#

from __future__ import absolute_import

from pyramid.security import Allow

from twilio_demo_pyramid_auth.security import Twilio


class RootContext(object):

    __name__ = ""
    __parent__ = None

    def __init__(self, request):
        pass

    @property
    def __acl__(self):
        return (
            (Allow, Twilio, "view"),
        )
