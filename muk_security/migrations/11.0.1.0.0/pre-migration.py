# Copyright 2021 Tecnativa - Víctor Martínez
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openupgradelib import openupgrade  # pylint: disable=W7936

_model_renames = [
    ("muk_dms.lock", "muk_security.lock"),
]
_table_renames = [
    ("muk_dms_lock", "muk_security_lock"),
]


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.rename_models(env.cr, _model_renames)
    for table in _table_renames:
        if openupgrade.table_exists(env.cr, table[0]):
            openupgrade.rename_tables(env.cr, [table])
