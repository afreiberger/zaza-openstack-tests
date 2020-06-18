# Copyright 2020 Canonical Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Code for setting up neutron-arista."""

import logging
import zaza


def test_fixture():
    """Pass arista-virt-test-fixture's IP address to neutron-arista."""
    fixture_ip_addr = zaza.model.get_units(
        'arista-virt-test-fixture')[0].public_address
    logging.info(
        "arista-virt-test-fixture's IP address is '{}'. ".format(
            fixture_ip_addr) +
        "Passing it to neutron-arista...")
    zaza.model.set_application_config('neutron-arista',
                                      {'eapi-host': fixture_ip_addr})
