"""TicketRouter — route triaged tickets to the right destination.

Takes Ticket objects (from TicketSync/TicketTriage or any compatible source)
and dispatches them to queues, teams, channels, or external webhooks.

Supports static rule-based routing out of the box, with an extensible
sink interface for destinations like Slack, PagerDuty, ServiceNow, SQS, etc.

>>> from ticket_router import version
>>> version()
'hello ticket'
"""

from ticket_router.version import version

__all__ = ["version"]
