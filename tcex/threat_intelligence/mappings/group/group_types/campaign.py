# -*- coding: utf-8 -*-
"""ThreatConnect TI Campaign"""
from ..group import Group


class Campaign(Group):
    """Unique API calls for Campaign API Endpoints

    Args:
        name (str): The name for this Group.
        owner (str): The name for this Group.
        first_seen (str, kwargs): The first seen datetime expression for this Group.
    """

    def __init__(self, tcex, name, owner=None, **kwargs):
        """Initialize Class Properties."""
        super().__init__(
            tcex, 'Campaign', 'campaign', 'campaigns', owner=owner, name=name, **kwargs
        )

    def first_seen(self, first_seen):
        """Update the campaign with the new first_seen date.

        Args:
            first_seen (str): The first_seen date. Converted to %Y-%m-%dT%H:%M:%SZ date format

        Returns:
            requests.Response: The response from the API call.
        """
        if not self.can_update():
            self._tcex.handle_error(910, [self.type])

        first_seen = self._utils.datetime.format_datetime(
            first_seen, date_format='%Y-%m-%dT%H:%M:%SZ'
        )
        self._data['firstSeen'] = first_seen
        request = {'firstSeen': first_seen}
        return self.tc_requests.update(self.api_type, self.api_branch, self.unique_id, request)
