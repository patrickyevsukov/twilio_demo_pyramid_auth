# Copyright (c) 2017 Patrick Yevsukov. All Rights Reserved.
#
# Use of this source code is governed by the OSI license in the LICENSE file.
#

from __future__ import absolute_import

from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.config import Configurator

from twilio_demo_pyramid_auth import context
from twilio_demo_pyramid_auth.security import (
    TwilioSignatureAuthenticationPolicy,
)


def main(global_config, **settings):

    config = Configurator(
        settings=settings,
        root_factory=context.RootContext,
        authorization_policy=ACLAuthorizationPolicy(),
        authentication_policy=TwilioSignatureAuthenticationPolicy(),
    )
    config.add_renderer(
        name="xml",
        factory="twilio_demo_pyramid_auth.renderer.XMLRendererFactory",
    )
    config.scan("twilio_demo_pyramid_auth.views")

    return config.make_wsgi_app()
