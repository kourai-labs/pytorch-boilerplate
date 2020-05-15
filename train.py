import torch
import hydra

from pytorch_lightning import Trainer
from argparse import ArgumentParser
from omegaconf import DictConfig

from systems.runtime import Runtime

@hydra.main(config_path="configs/config.yaml")
def main(cfg: DictConfig) -> None:
    print(cfg.pretty())

    # Create runtime and trainer with args+configs.
    runtime = Runtime(cfg)
    trainer = Trainer(**cfg.trainer)

    # Start training.
    trainer.fit(runtime)

    print("done.")

if __name__ == "__main__":
    main()
