#
# Copyright (c) nexB Inc. and others. All rights reserved.
# purldb is a trademark of nexB Inc.
# SPDX-License-Identifier: Apache-2.0
# See http://www.apache.org/licenses/LICENSE-2.0 for the license text.
# See https://github.com/nexB/purldb for support or download.
# See https://aboutcode.org for more information about nexB OSS projects.
#


class PackageDBReadOnlyRouter(object):
    app_labels = [
        'clearcode',
        'clearindex',
        'minecode',
        'matchcode',
        'packagedb',
    ]

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.app_labels:
            return 'packagedb'
        return None

    def db_for_write(self, model, **hints):
        return None

    def allow_relation(self, obj1, obj2, **hints):
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return None