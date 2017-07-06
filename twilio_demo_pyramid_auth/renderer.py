# Copyright (c) 2017 Patrick Yevsukov. All Rights Reserved.
#
# Use of this source code is governed by the OSI license in the LICENSE file.
#
from __future__ import absolute_import

from pyramid import httpexceptions
from twilio.twiml.voice_response import VoiceResponse


class XMLRendererFactory(object):

    def __init__(self, info):
        """Create an instance of `XMLRendererFactory`

        :param info: An object having the following attributes:
            - name: The renderer name.
            - package: The package that was 'current' at the time the renderer
                was registered.
            - type: The renderer type name.
            - registry: The current application registry.
            - settings: The deployment settings dictionary.

        :returns: An instance of `XMLRendererFactory`

        Source:
            docs.pylonsproject.org/projects/pyramid/en/1.9-branch/narr/renderers.html

        """

    def __call__(self, value, system):
        """Convert a Twilio VoiceResponse object to a TwiML string and return
        it with the application/xml content type.

        :param value: The return value of a view.
        :param system: A dictionary containing available system values.

        :returns: A TwiML string.

        :raises pyramid.httpexceptions.HTTPServerError: If `value` is not an
            instance of `twilio.twiml.voice_response.VoiceResponse` or
            `request` is not in the `system` dictionary.

        Source:
            docs.pylonsproject.org/projects/pyramid/en/1.9-branch/narr/renderers.html

        """
        request = system.get("request")

        if request is None or not isinstance(value, VoiceResponse):
            raise httpexceptions.HTTPServerError()

        request.response.content_type = "application/xml"
        return value.to_xml()
