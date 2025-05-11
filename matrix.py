#!/usr/bin/env python3

"""
Build matrix configuration for OpenSSL.
This file defines the versions and distributions to build.
"""

import yaml

VERSIONS = [
    "3.0.15"
]

DISTRIBUTIONS = [
    {
        "name": "ubuntu",
        "versions": ["22.04"]
    },
    {
        "name": "debian",
        "versions": ["11"]
    }
]

def generate_matrix():
    """Generate the build matrix."""
    matrix = []
    for version in VERSIONS:
        for distro in DISTRIBUTIONS:
            for distro_version in distro["versions"]:
                matrix.append({
                    "version": version,
                    "os": f"{distro['name']}-{distro_version}"
                })
    return matrix

if __name__ == "__main__":
    print(yaml.dump({"include": generate_matrix()}, default_flow_style=False)) 
