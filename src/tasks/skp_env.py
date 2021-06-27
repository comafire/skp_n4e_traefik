import os, sys, json, re
from pprint import pprint

# SKP
SKP_USER = os.environ["SKP_USER"]
SKP_HOME = os.environ["SKP_HOME"]

# TRAEFIK
try:
    TRAEFIK_HOME = os.environ["TRAEFIK_HOME"]
    TRAEFIK_VER = os.environ["TRAEFIK_VER"]
    TRAEFIK = True
except:
    TRAEFIK = False

