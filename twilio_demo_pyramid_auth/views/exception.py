# Copyright (c) 2017 Patrick Yevsukov. All Rights Reserved.
#
# Use of this source code is governed by the OSI license in the LICENSE file.
#

from __future__ import absolute_import

from pyramid import httpexceptions
from pyramid.view import (
    exception_view_config,
    notfound_view_config,
    forbidden_view_config,
    view_defaults,
)
from twilio.twiml.voice_response import VoiceResponse

from .base import BaseViews 


@view_defaults(
    renderer="xml",
)
class ExceptionViews(BaseViews):

    def _handle_exception(self):
        response = VoiceResponse()

        self.request.response.status_int = 200

        message = (
            "My apologies. We seem to be experiencing technical difficulties. "
            "You will now be redirected to our call center for assistance."
        )
        response.say(
            message,
            voice="woman",
            language="en",
        )
        response.dial(self.request.registry.settings["support_number"])

        return response

    @notfound_view_config()
    def notfound(self):
        return self._handle_exception()

    @forbidden_view_config()
    def forbidden(self):
        return self._handle_exception()

    @exception_view_config(httpexceptions.HTTPServerError)
    def exception(self):
        return self._handle_exception()
