Demo of Twilio auth with Pyramid
================================

This repository contains a sample implementation of a Twilio interactive voice
response (IVR) system, using the Pyramid web application framework.

Specifically, this sample IVR implementation is intended to demonstrate proper
`request validation <https://www.twilio.com/docs/api/security#validating-requests>`_.

Follow along with this code on the `Twilio Blog <https://www.twilio.com/blog/>`_.

Usage:
------

.. code-block:: shell

    $ cd /tmp
    $ curl -LOk https://github.com/patrickyevsukov/twilio_demo_pyramid_auth/archive/master.zip
    $ unzip master.zip
    $ mv twilio_demo_pyramid_auth* twilio_demo_pyramid_auth
    $ cd twilio_demo_pyramid_auth
    $ pip install virtualenv
    $ virtualenv --clear venv
    $ . ./venv/bin/activate
    $ pip install -e .
    $ export TWILIO_AUTH_TOKEN=XXXX
    $ ./tools/serve -c examples/config.ini
