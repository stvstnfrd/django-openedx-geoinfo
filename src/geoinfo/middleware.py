# coding: utf-8
"""
Middleware to identify the country of origin of page requests.

Middleware adds `country_code` in session.

Usage:

# To enable the Geoinfo feature on a per-view basis, use decoarator:
`django.utils.decorators.decorator_from_middleware(CountryMiddleware)`

"""
from ipware.ip import get_real_ip
import logging
import pygeoip

from django.conf import settings

LOG = logging.getLogger(__name__)


class CountryMiddleware(object):  # pylint: disable=too-few-public-methods
    """
    Identify the country by IP address.
    """
    def process_request(self, request):  # pylint: disable=no-self-use
        """
        Identify the country by IP address.

        Store country code in session.
        """
        new_ip_address = get_real_ip(request)
        old_ip_address = request.session.get('ip_address', None)

        if not new_ip_address and old_ip_address:
            del request.session['ip_address']
            del request.session['country_code']
        elif new_ip_address != old_ip_address:
            if new_ip_address.find(':') >= 0:
                path_data = settings.GEOIPV6_PATH
            else:
                path_data = settings.GEOIP_PATH
            geo_ip = pygeoip.GeoIP(path_data)
            country_code = geo_ip.country_code_by_addr(new_ip_address)
            request.session['country_code'] = country_code
            request.session['ip_address'] = new_ip_address
            LOG.debug(
                "Country code for IP: %s is set to %s",
                new_ip_address,
                country_code,
            )
