#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import json
import matplotlib.pyplot as plt

# Read contributors from input
contributors = json.loads(sys.argv[1])

# Extract contributor logins and contributions
contributor_logins = [contributor['login'] for contributor in contributors]
contributor_contributions = [contributor['contributions'] for contributor in contributors]

# Generate the graph
plt.bar(contributor_logins, contributor_contributions)
plt.xlabel('Contributor')
plt.ylabel('Contributions')
plt.title('Contributions by Contributor')
plt.xticks(rotation=45)
plt.tight_layout()

# Save the graph
plt.savefig('contributions_graph.png')

# Append graph to markdown file
with open('CONTRIBUTORS.md', 'a') as f:
    f.write('\n\n<img src="./contributions_graph.png">')
