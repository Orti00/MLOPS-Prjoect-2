import argparse
import project2

parser = argparse.ArgumentParser()
parser.add_argument("--learning_rate", "-lr", type=float, default=1e-4)
parser.add_argument("--warmup_steps", "-ws", type=int, default=0)
parser.add_argument("--weight_decay", "-wd", type=float, default=0.0)
parser.add_argument("--batch_size", "-bs", type=int, default=64)
parser.add_argument("--checkpoint_dir", type=str, default="models")
args = parser.parse_args()

project2.train(vars(args))
