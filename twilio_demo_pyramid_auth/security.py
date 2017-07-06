# Copyright (c) 2017 Patrick Yevsukov. All Rights Reserved.
#
# Use of this source code is governed by the OSI license in the LICENSE file.
#

from __future__ import absolute_import

import logging
import os

from pyramid import security as pyramid_security
from twilio.request_validator import RequestValidator


logger = logging.getLogger(__name__)


Twilio = "twilio"


class TwilioSignatureAuthenticationPolicy(object):

    def _is_authentic_twilio_request(self, request):
        logger.info("Authenticating {} {}".format(request.method, request.path))

        twilio_auth_key = os.environ["TWILIO_AUTH_TOKEN"]
        request_validator = RequestValidator(twilio_auth_key)

        twilio_signature = request.headers.get("X-Twilio-Signature", "")
        is_authentic = request_validator.validate(
            request.url,
            request.POST,
            twilio_signature,
        )
        if is_authentic:
            logger.info("Authentication SUCCESS")
            return is_authentic

        logger.info("Authentication FAILURE")
        return is_authentic

    def effective_principals(self, request):
        principals = [pyramid_security.Everyone]

        if self._is_authentic_twilio_request(request):
            principals.append(Twilio)

        return principals
