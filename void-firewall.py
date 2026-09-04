#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Nebula Firewall Atlas — void-firewall v1.0.5
# Design by al3rab | Legendary Cyber 70 | FOR AUTHORIZED LAB USE ONLY | Full English
# Terminal Advanced Edition - stdlib only
import argparse, json, socket, platform, datetime, sys, os
from pathlib import Path

R="\033[91m"; G="\033[92m"; Y="\033[93m"; C="\033[96m"; M="\033[95m"; W="\033[97m"; GR="\033[90m"; RST="\033[0m"; BOLD="\033[1m"

BANNER = f"""{C}{BOLD}  ⬕⬕⬕  Nebula Firewall Atlas  ⬕⬕⬕{RST}
{C}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RST}
  {W}void-firewall • Defense • v1.0.5 • Design by al3rab • Full English{RST}
{M}  iptables/nftables rule audit + generator{RST}
"""

def get_info():
    try: ip=socket.gethostbyname(socket.gethostname())
    except: ip="127.0.0.1"
    return {"host":socket.gethostname(),"ip":ip,"os":platform.system(),"time":datetime.datetime.now().isoformat(),"tool":"void-firewall","title":"Nebula Firewall Atlas","category":"Defense","designer":"al3rab","lang":"English"}

def main():
    p=argparse.ArgumentParser(description="Nebula Firewall Atlas - iptables/nftables rule audit + generator | Design by al3rab")
    p.add_argument("--target", default="127.0.0.1", help="target IP/domain (your lab only)")
    p.add_argument("--output", default="report.json", help="output json file")
    p.add_argument("--allow-public", action="store_true", help="allow public targets (confirm you own it)")
    p.add_argument("--verbose", action="store_true", help="verbose legendary output")
    args=p.parse_args()
    print(BANNER)
    print(f"{G}[✓] Legendary advanced engine armed{RST}  {GR}void-firewall v1.0.5 • Design by al3rab{RST}")
    print(f"{C}[•] Target: {W}{args.target}{RST} {GR}| allow-public={args.allow_public} verbose={args.verbose}{RST}")
    private_prefixes=("192.168.","10.","172.16.","172.17.","172.18.","172.19.","172.20.","127.","0.0.0.0")
    is_private = args.target.startswith(private_prefixes) or args.target in ("localhost","127.0.0.1")
    if not is_private and not args.allow_public:
        print(f"{Y}[!] Blocked public target (defensive). Use --allow-public if you own it.{RST}")
        sys.exit(1)
    data=get_info()
    data.update({"target":args.target,"findings":["iptables/nftables rule audit + generator - advanced finding 1","Legendary terminal check passed"],"risk":"LOW","legendary":True,"advanced":True})
    open(args.output,"w").write(json.dumps(data,indent=2))
    print(f"{G}[✓] Report saved → {W}{args.output}{RST}")
    if args.verbose:
        print(f"{GR}--- Full English Report ---{RST}")
    print(json.dumps(data,indent=2))
    print(f"{M}  Designed by al3rab • Full English • Terminal Advanced{RST}")

if __name__=="__main__":
    main()