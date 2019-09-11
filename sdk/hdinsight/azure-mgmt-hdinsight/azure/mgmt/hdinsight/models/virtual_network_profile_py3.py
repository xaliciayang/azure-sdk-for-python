# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class VirtualNetworkProfile(Model):
    """The virtual network properties.

    :param id: The ID of the virtual network.
    :type id: str
    :param subnet: The name of the subnet.
    :type subnet: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'subnet': {'key': 'subnet', 'type': 'str'},
    }

    def __init__(self, *, id: str=None, subnet: str=None, **kwargs) -> None:
        super(VirtualNetworkProfile, self).__init__(**kwargs)
        self.id = id
        self.subnet = subnet