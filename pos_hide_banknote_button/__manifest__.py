# Copyright (C) 2020 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Point of Sale - Hide Banknote Buttons",
    "version": "16.0.1.0.0",
    "category": "Point Of Sale",
    "summary": "Hide useless Banknote buttons in the PoS (+10, +20, +50)",
    "author": "GRAP, Odoo Community Association (OCA)",
    "maintainers": ["legalsylvain"],
    "website": "https://github.com/OCA/pos",
    "license": "AGPL-3",
    "depends": ["point_of_sale"],
    "assets": {
        "point_of_sale.assets": [
            "pos_hide_banknote_button/static/src/scss/pos_hide_banknote_button.scss",
        ],
    },
}
