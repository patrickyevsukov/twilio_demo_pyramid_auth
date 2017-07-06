# Copyright (c) 2017 Patrick Yevsukov. All Rights Reserved.
#
# Use of this source code is governed by the OSI license in the LICENSE file.
#

class BaseViews(object):

    def __init__(self, request):
        self.request = request
