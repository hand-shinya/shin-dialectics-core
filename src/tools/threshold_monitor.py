#!/usr/bin/env python3
import argparse,json
from importlib import import_module
params=import_module("src.specs.params")
def decide(lambda_a,tau,u):
    if lambda_a>=params.LAMBDA_A and tau>=params.TAU_STOP and u<=params.U_MAX: return "consolidate"
    return "explore_more" if u>params.U_MAX or lambda_a<params.LAMBDA_A or tau<params.TAU_STOP else "explore_more"
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--thesis",required=True); ap.add_argument("--lambda-a",type=int,required=True); ap.add_argument("--tau",type=float,default=0.5); ap.add_argument("--u",type=float,default=0.3); ap.add_argument("--axes",nargs="*",default=["Historical","Psychological","Economic","Ethical"])
    a=ap.parse_args()
    guard=[{"axis":x,"priority":"quality of feedback rather than quantity","risk":"automation bias"} for x in a.axes[:6]]
    out={"thesis":a.thesis,"guardrails":guard,"thresholds":{"lambda_p":params.LAMBDA_P,"lambda_a":params.LAMBDA_A,"lambda_s":params.LAMBDA_S,"lambda_i":params.LAMBDA_I,"tau_stop":params.TAU_STOP,"u_max":params.U_MAX},"decision":{"action":decide(a.lambda_a,a.tau,a.u),"rationale":"threshold rule"}}
    print(json.dumps(out,ensure_ascii=False,indent=2))
if __name__=="__main__": main()
