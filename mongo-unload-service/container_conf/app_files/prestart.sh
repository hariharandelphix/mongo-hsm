#! /usr/bin/env sh
#
# Copyright (c) 2023 by Delphix. All rights reserved.
#

echo "Running inside /app/prestart.sh, you could add migrations to this file, e.g.:"

echo "
#! /usr/bin/env bash

# Let the DB start
sleep 10;
# Run migrations
alembic upgrade head
"
