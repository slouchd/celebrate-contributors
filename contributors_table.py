#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import json
import html
from tabulate import tabulate

# Read contributors from input
contributors = json.loads(sys.argv[1])

# Data required for table
contributor_profile_usernames = [contributor['login'] for contributor in contributors]
contributor_profile_urls = [contributor['html_url'] for contributor in contributors]
contributor_profile_avatars = [contributor['avatar_url'] for contributor in contributors]

# Create a list of rows
table_rows = []

for (username, url, avatar) in zip(contributor_profile_usernames, contributor_profile_urls, contributor_profile_avatars):
    tr = f'<a href="{url}"><img src="{avatar}" width="100px;" alt="{username}"/><br /><sub><b>{username}</b></sub></a><br />'
    table_rows.append(tr)

# Create table html no row bigger than 7 wide
list_group = 7
table = [table_rows[i:i + list_group] for i in range(0, len(table_rows), list_group)]
contributors_table = tabulate(table, tablefmt='html')

# Save table to markdown file
with open('CONTRIBUTORS.md', 'w') as f:
    f.write('## Contributors ✨\n')
    f.write('With thanks to all our contributors!\n\n')
    f.write(html.unescape(contributors_table))
