import os

import torch
import pytorch_lightning as pl
import hydra

from torch.utils.data import DataLoader
from pytorch_lightning import Trainer


class Runtime(pl.LightningModule):

    def __init__(self, cfg):
        super().__init__()
        self.cfg = cfg.runtime

        # Import models.
        # self.model = ...

    def forward(self, x):
        # return self.model(x)
        return NotImplemented

    ##########
    ## DATA ##
    ##########

    def prepare_data(self):
        project_home = hydra.utils.get_original_cwd()
        # Initialize datasets.
        # self.training_dataset = ...
        # self.validation_dataset = ...
        # self.test_dataset = ...

    def train_dataloader(self):
        # return DataLoader(self.training_dataset, batch_size=self.cfg.batch_size, num_workers=self.cfg.num_workers)
        raise NotImplemented
    def val_dataloader(self):
        # return DataLoader(self.validation_dataset, batch_size=self.cfg.batch_size, num_workers=self.cfg.num_workers)
        raise NotImplemented
    def test_dataloader(self):
        # return DataLoader(self.test_dataset, batch_size=self.cfg.batch_size, num_workers=self.cfg.num_workers)
        raise NotImplemented

    ##############
    ## TRAINING ##
    ##############

    def training_step(self, batch, batch_idx):
        # x, y = batch
        # ...
        # return {'loss': loss}
        raise NotImplemented

    def configure_optimizers(self):
        # self.optimizer = ...
        # return self.optimizer
        raise NotImplemented

    ################
    ## VALIDATION ##
    ################

    def validation_step(self, batch, batch_idx):
        # x, y = batch
        # return {'val_loss': loss}
        raise NotImplemented

    def validation_epoch_end(self, outputs):
        avg_loss = torch.stack([x['val_loss'] for x in outputs]).mean()
        return {'val_loss': avg_loss}

    #############
    ## TESTING ##
    #############

    def test_step(self, batch, batch_idx):
        # x, y = batch
        # return {'val_loss': loss}
        raise NotImplemented

    def test_epoch_end(self, outputs):
        avg_loss = torch.stack([x['val_loss'] for x in outputs]).mean()
        return {'val_loss': avg_loss }
