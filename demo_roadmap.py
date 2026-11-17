"""Offline example: traceable roadmap summaries with fictional work items.

All data below are synthetic. No APIs, model calls or credentials are used.
"""
from dataclasses import dataclass
from collections import Counter
import json


@dataclass(frozen=True)
class WorkItem:
    item_id: int
    kind: str
    state: str
    title: str
    linked_ids: tuple[int, ...] = ()


SAMPLE_ITEMS = (
    WorkItem(101, "Feature", "Active", "Improve order status visibility", (102,)),
    WorkItem(102, "Change Request", "Active", "Show delayed shipments", (101,)),
    WorkItem(103, "Bug", "Resolved", "Fix status label", ()),
    WorkItem(104, "Change Request", "New", "Export order history", ()),
)

CLOSED_STATES = frozenset({"Closed", "Resolved", "Rejected"})


def summarize(items):
    """Return explicit counts for active items, excluding closed states."""
    active = [item for item in items if item.state not in CLOSED_STATES]
    by_kind = Counter(item.kind for item in active)
    return {
        "active_items": len(active),
        "excluded_items": len(items) - len(active),
        "by_kind": dict(sorted(by_kind.items())),
        "relationships": [
            {"item_id": item.item_id, "related_to": link}
            for item in active
            for link in item.linked_ids
        ],
        "caveat": "Links do not by themselves establish duplicate requests.",
    }


if __name__ == "__main__":
    print(json.dumps(summarize(SAMPLE_ITEMS), indent=2))
