"""Simple rule-based assistant for reducing food waste."""


class WasteLessAgent:
    """A basic AI-style assistant that gives waste-reduction suggestions."""

    def __init__(self):
        # Items that are commonly considered wet waste after disposal.
        self._wet_waste_items = {
            "fruit peels",
            "vegetable peels",
            "tea leaves",
            "coffee grounds",
            "egg shells",
            "leftover food",
            "milk",
            "bread",
        }

        # Items that are commonly considered dry waste after disposal.
        self._dry_waste_items = {
            "plastic bottle",
            "paper",
            "cardboard",
            "glass",
            "metal can",
            "rice bag",
            "snack wrapper",
        }

    def _item_state(self, days_left):
        """Classify an item as fresh, near expiry, or expired using days left."""
        if days_left < 0:
            return "expired"
        if days_left <= 2:
            return "near expiry"
        return "fresh"

    def _normalize_name(self, value):
        """Normalize item names for safe case-insensitive comparisons."""
        if isinstance(value, str):
            return value.strip().lower()
        return ""

    def analyze_items(self, items_list):
        """
        Analyze each item and suggest an action.

        Expected input:
        [
            {"name": "milk", "days_left": 1},
            {"name": "rice", "days_left": 30}
        ]
        """
        suggestions = []

        for item in items_list:
            raw_name = item.get("name", "unknown item")
            normalized_name = self._normalize_name(raw_name)
            name = raw_name.strip() if normalized_name else "unknown item"
            days_left = item.get("days_left", 0)

            state = self._item_state(days_left)

            if state == "expired":
                action = "dispose safely"
            elif state == "near expiry":
                action = "use soon"
            else:
                action = "safe to store"

            suggestions.append(
                {
                    "name": name,
                    "state": state,
                    "suggestion": action,
                }
            )

        return suggestions

    def suggest_purchase(self, existing_items, new_item):
        """
        Suggest whether a new item should be purchased.

        Rule:
        - If same item already exists and is still usable (days_left >= 0): do not buy now.
        - If same item exists but expired: buying is okay.
        - If item does not exist: buying is okay.
        """
        new_item_name = self._normalize_name(new_item.get("name", ""))

        for item in existing_items:
            existing_name = self._normalize_name(item.get("name", ""))
            existing_days_left = item.get("days_left", 0)

            if existing_name == new_item_name and self._item_state(existing_days_left) != "expired":
                return "do not buy (you already have this item)"

        return "buy (item needed)"

    def waste_category(self, item_name):
        """
        Return a simple waste category for the given item name.

        Possible outputs: "wet waste", "dry waste", "unknown"
        """
        normalized_name = self._normalize_name(item_name)

        if normalized_name in self._wet_waste_items:
            return "wet waste"
        if normalized_name in self._dry_waste_items:
            return "dry waste"
        return "unknown"
