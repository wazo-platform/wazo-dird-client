# Copyright 2022-2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_lib_rest_client.command import RESTCommand

from .exceptions import DirdError, DirdServiceUnavailable, InvalidDirdError


class DirdCommand(RESTCommand):
    @staticmethod
    def raise_from_response(response):
        if response.status_code == 503:
            raise DirdServiceUnavailable(response)

        try:
            raise DirdError(response)
        except InvalidDirdError:
            RESTCommand.raise_from_response(response)
