from frappe import _


def get_data():
    return [
        {
            "label": _("Data Collection App"),
            "icon": "octicon octicon-graph",
            "items": [
                {
                    "type": "doctype",
                    "name": "Periods",
                    "label": _("Periods"),
                    "description": _("The time period for each business cycle."),
                },
                {
                    "type": "doctype",
                    "name": "Assignments",
                    "label": _("Assignments"),
                    "description": _(
                        "Operations to collect data within a given Period."
                    ),
                },
                {
                    "type": "doctype",
                    "name": "Product Groups",
                    "label": _("Product Groups"),
                    "description": _("Different categories that products belong to"),
                },
                {
                    "type": "doctype",
                    "name": "Countries",
                    "label": _("Countries"),
                    "description": _("Countries we run operations within."),
                },
                {
                    "type": "doctype",
                    "name": "Channels",
                    "label": _("Channels"),
                    "description": _("Channel which shops belong to."),
                },
                {
                    "type": "doctype",
                    "name": "Brands",
                    "label": _("Brands"),
                    "description": _("Brands for items we track."),
                },
                {
                    "type": "doctype",
                    "name": "Descriptions",
                    "label": _("Descriptions"),
                    "description": _("Item Descriptions"),
                },
                {
                    "type": "doctype",
                    "name": "Locations",
                    "label": _("Locations"),
                    "description": _("Locations within countries that we operate in."),
                },
                {
                    "type": "doctype",
                    "name": "Shops",
                    "label": _("Shops"),
                    "description": _("Shops that have been recruited to our platform."),
                },
                {
                    "type": "doctype",
                    "name": "Items",
                    "label": _("Items"),
                    "description": _(
                        "Items that have been identified and added to platform"
                    ),
                },
                {
                    "type": "doctype",
                    "name": "Item Specification",
                    "label": _("Item Specification"),
                    "description": _("Specification of a given item we track."),
                },
                {
                    "type": "doctype",
                    "name": "Shop Items",
                    "label": _("Shop Items"),
                    "description": _("Items stocked in a given shop."),
                },
                {
                    "type": "doctype",
                    "name": "Entries",
                    "label": _("Entries"),
                    "description": _(
                        "Entries from datacollection process for a given assignment."
                    ),
                },
                {
                    "type": "doctype",
                    "name": "Item Logs",
                    "label": _("Item Logs"),
                    "description": _("Data record for a given item."),
                },
                {
                    "type": "doctype",
                    "name": "Assignments Details",
                    "label": _("Assignments Details"),
                    "description": _(
                        "Extra details about assignments, link user and shops."
                    ),
                },
                {
                    "type": "doctype",
                    "name": "Assignment Locations",
                    "label": _("Assignment Locations"),
                    "description": _(
                        "Represent locations where an assignment will be carried out."
                    ),
                },
                {
                    "type": "doctype",
                    "name": "Data Collection",
                    "label": _("Data Collection"),
                    "description": _("Data collected for a given assignment."),
                },
            ],
        }
    ]
