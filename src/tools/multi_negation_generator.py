#!/usr/bin/env python3
import argparse,json,random
from importlib import import_module
params=import_module("src.specs.params")
T=["From the {axis} perspective, the thesis neglects {gap}.","A {axis} lens suggests the opposite: {counter}.","Under {axis} constraints, {risk} undermines the thesis.","A {axis} reading would prioritize {priority} over the claimed benefit.","Historically analogous cases show {analogy} contradicting the thesis."]
G=["path dependency and institutional inertia","users' tacit knowledge and affective factors","hidden costs and externalities","distributional impacts and equity","verification/validation brittleness","workload and assessment fidelity","governance and accountability gaps"]
C=["the need to slow down rather than accelerate deployment","that local context outperforms standardized solutions","that human judgement should remain the first-class citizen","that measurement changes the measured behavior (Goodhart effects)","that adoption without capacity building backfires"]
R=["specification gaming","automation bias","opportunity loss for low-resource users","lock-in to proprietary ecosystems","privacy leakage and chilling effects"]
P=["robustness under distribution shift","human agency and collective sensemaking","pluralism of pathways","quality of feedback rather than quantity","data governance and auditability"]
A=["past tech waves overselling personalization","ERP rollouts that ignored tacit workflows","measurement regimes that distorted incentives","top-down reforms failing without buy-in","AI pilots that could not scale beyond champions"]
def gen(thesis,axes,stances):
    random.seed(42); claims=[]; ie={"internal":0,"external":0}
    for a in axes:
        for i in range(stances):
            t=T[i%len(T)]
            claims.append(t.format(axis=a,gap=random.choice(G),counter=random.choice(C),risk=random.choice(R),priority=random.choice(P),analogy=random.choice(A)))
            (ie.__setitem__("internal",ie["internal"]+1) if i%2==0 else ie.__setitem__("external",ie["external"]+1))
    return claims,ie
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--thesis",required=True); ap.add_argument("--axes",type=int,default=4); ap.add_argument("--stances",type=int,default=params.STANCES_DEFAULT)
    args=ap.parse_args()
    axes=params.AXES_DEFAULT[:max(1,min(args.axes,len(params.AXES_DEFAULT)))]
    claims,ie=gen(args.thesis,axes,args.stances)
    print(json.dumps({"thesis":args.thesis,"axes":axes,"claims":claims,"meta":{"mode":"demo","lambda_a":len(claims),"i_e_ratio":ie}},ensure_ascii=False,indent=2))
if __name__=="__main__": main()
