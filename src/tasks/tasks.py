from invoke import Collection
import skp_env, skp_util

ns = Collection()

if skp_env.TRAEFIK:
    import traefik
    ns.add_collection(Collection.from_module(traefik), 'traefik')

