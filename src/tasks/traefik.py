from invoke import task
import os, sys, re, time
import skp_env, skp_util

@task
def install(c):
    skp_util.mkdir_usr(c, skp_env.TRAEFIK_HOME)
    if skp_util.is_macos(c):
        pass # not yet
    if skp_util.is_ubuntu(c):
        cmd = f"sudo apt-get install -y libcap2-bin"
        skp_util.run_with_exit(c, cmd)        
        url = f"https://github.com/traefik/traefik/releases/download/v{skp_env.TRAEFIK_VER}/traefik_v{skp_env.TRAEFIK_VER}_linux_amd64.tar.gz"
        fname = url.split('/')[-1]
        cmd = f"wget -q {url} -O {skp_env.TRAEFIK_HOME}/usr/{fname}" # 출력이 길다면, -q 옵션 사용 가능
        skp_util.run_with_exit(c, cmd)
        # tar --strip-components: 압축 파일에서 제거하고자 하는 경로 depth
        cmd = f"cd {skp_env.TRAEFIK_HOME}/usr && rm -rf ./traefik_v{skp_env.TRAEFIK_VER} && mkdir ./traefik_v{skp_env.TRAEFIK_VER} && tar -zxf {fname} -C traefik_v{skp_env.TRAEFIK_VER} --strip-components=0"
        skp_util.run_with_exit(c, cmd)        
        cmd = f"sudo setcap cap_net_bind_service=+ep {skp_env.TRAEFIK_HOME}/usr/traefik_v{skp_env.TRAEFIK_VER}/traefik"
        skp_util.run_with_exit(c, cmd)    

@task
def start(c):
    cmd = f"envsubst < {skp_env.TRAEFIK_HOME}/etc/pm2.json | pm2 start -"
    skp_util.run_with_exit(c, cmd)

@task
def stop(c):
    cmd = f"envsubst < {skp_env.TRAEFIK_HOME}/etc/pm2.json | pm2 stop -"
    skp_util.run_with_exit(c, cmd)
    cmd = f"envsubst < {skp_env.TRAEFIK_HOME}/etc/pm2.json | pm2 delete -"
    skp_util.run_with_exit(c, cmd)

@task
def restart(c):
    stop(c)
    start(c)

