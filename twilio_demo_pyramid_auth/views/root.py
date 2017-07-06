# Copyright (c) 2017 Patrick Yevsukov. All Rights Reserved.
#
# Use of this source code is governed by the OSI license in the LICENSE file.
#

from __future__ import absolute_import

from collections import OrderedDict

from pyramid.view import view_config, view_defaults
from twilio.twiml.voice_response import Gather, VoiceResponse

from twilio_demo_pyramid_auth import context

from .base import BaseViews


SELECTIONS = OrderedDict((
    ("1", "accessible"),
    ("2", "restricted"),
))


@view_defaults(
    context=context.RootContext,
    permission="view",
    renderer="xml",
)
class RootViews(BaseViews):

    @view_config(
        request_method="GET",
    )
    def get(self):
        response = VoiceResponse()

        message = "Welcome to this demo of Twilio authentication, with Pyramid."
        for digit, word in SELECTIONS.items():
            message += " To visit the {} route, press {}.".format(word, digit)

        gather = Gather(
            num_digits=1,
            action=self.request.path_url,
            method="POST",
            timeout=3,
        )
        gather.say(message, voice="woman", language="en")

        response.append(gather)
        response.say("Please try again.", voice="woman", language="en")
        response.redirect(self.request.path_url, method="GET")

        return response

    @view_config(
        request_method="POST",
    )
    def post(self):
        response = VoiceResponse()

        selection = self.request.params.get("Digits")
        selected_route = SELECTIONS.get(selection)
        if selected_route is not None:
            url = self.request.resource_url(self.request.context, selected_route)
            response.redirect(url, method="GET")

        response.say(
            "Unrecognized selection. Please try again.",
            voice="woman",
            language="en",
        )
        response.redirect(self.request.path_url, method="GET")

        return response

    @view_config(
        request_method="GET",
        name="accessible",
    )
    def accessible(self):
        response = VoiceResponse()

        message = (
            "You were successfully redirected to an authenticated route. "
            "Goodbye."
        )
        response.say(message, voice="woman", language="en")
        response.hangup()

        return response

    @view_config(
        request_method="GET",
        name="restricted",
        permission="restricted",
    )
    def restricted(self):
        """This route is NOT accessible.

        """
