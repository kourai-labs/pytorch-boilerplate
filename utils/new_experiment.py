import hydra

@hydra.main(config_path="../conf/")
def new_experiment(cfg):
    print(cfg)

if __name__ == "__main__":
    new_experiment()