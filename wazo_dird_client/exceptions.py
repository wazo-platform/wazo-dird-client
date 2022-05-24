# -*- coding: utf-8 -*-
# Copyright 2017-2022 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later


from requests import HTTPError


class DirdError(HTTPError):
    def __init__(self, response):
        try:
            body = response.json()
        except ValueError:
            raise InvalidDirdError()

        if not body:
            raise InvalidDirdError()

        self.status_code = response.status_code
        try:
            self.message = body['message']
            self.error_id = body['error_id']
            self.details = body['details']
            self.timestamp = body['timestamp']

        except KeyError:
            raise InvalidDirdError()

        exception_message = '{e.message}: {e.details}'.format(e=self)
        super(DirdError, self).__init__(exception_message, response=response)


class InvalidDirdError(Exception):
    pass


class DirdServiceUnavailable(DirdError):
    pass
