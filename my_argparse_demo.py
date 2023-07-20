import argparse
import sys
import os
import random
from pathlib import Path
import wandb
import socket
import math
def parse(args):
    parser=argparse.ArgumentParser(
        description='wandb_useage',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--project_name",type=str)
    parser.add_argument("--experiment_name",type=str)
    # parser.add_argument("--scenario_name",type=str)
    parser.add_argument("--seed",type=int,default=0)
    #parse_known_args第一个元素是Namespace对象，存储解析后的参数.第二个元素是是否解析的bool值
    all_args=parser.parse_known_args(args)[0]
    return all_args
def test_curves(args):
    all_args=parse(args)
    random.seed(all_args.seed)
    run_dir=Path("./results")/all_args.project_name/all_args.experiment_name
    if not run_dir.exists():
        os.makedirs(str(run_dir))
    wandb.init(
        config=all_args,
        project=all_args.project_name,
        notes=socket.gethostname(),
        name=all_args.experiment_name+" "+str(all_args.seed),
        dir=str(run_dir),
        job_type="training",
        reinit=True
    )
    total_step_num=1000
    for step in range(total_step_num):
        wandb.log({'random_curve':step/100+random.random()},step=step)
        wandb.log({'log_curve':math.log(step+1)},step=step)
    wandb.finish()

if __name__=='__main__':
    #python test_curves.py --team_name "tmarl" --project_name "wandb_usage" --experiment_name "test_curves" --scenario_name "random_curves"
    #sys.argv[0]是命令行中的第一个参数test_curves.py,sys.argv[1:]是之后的参数
    test_curves(sys.argv[1:])