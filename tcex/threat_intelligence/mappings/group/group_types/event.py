# -*- coding: utf-8 -*-
"""ThreatConnect TI Event"""
from ..group import Group


class Event(Group):
    """Unique API calls for Event API Endpoints

    Valid status:
    + Escalated
    + False Positive
    + Needs Review
    + No Further Action

    Args:
        name (str): The name for this Group.
        event_date (str, kwargs): The event datetime expression for this Group.
        status (str, kwargs): The status for this Group.
    """

    def __init__(self, tcex, name, owner=None, **kwargs):
        """Initialize Class Properties."""
        super().__init__(tcex, 'Event', 'event', 'events', owner=owner, name=name, **kwargs)

    def event_date(self, event_date):
        """Update the event date for the Event.

        Args:
            event_date (str): The event datetime expression for this Group.

        Returns:
            requests.Response: The response from the API call.
        """
        if not self.can_update():
            self._tcex.handle_error(910, [self.type])

        event_date = self._utils.datetime.format_datetime(
            event_date, date_format='%Y-%m-%dT%H:%M:%SZ'
        )
        self._data['eventDate'] = event_date
        request = {'eventDate': event_date}
        return self.tc_requests.update(self.api_type, self.api_branch, self.unique_id, request)

    def status(self, status):
        """Update the event date for the Event.

        Valid status:
        + Escalated
        + False Positive
        + Needs Review
        + No Further Action

        Args:
            status (str, kwargs): The status for this Group.

        Returns:
            requests.Response: The response from the API call.
        """
        if not self.can_update():
            self._tcex.handle_error(910, [self.type])

        self._data['status'] = status
        request = {'status': status}
        return self.tc_requests.update(self.api_type, self.api_branch, self.unique_id, request)
