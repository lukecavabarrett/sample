import hydra
import time
import numpy as np

t0 = time.time()

per_epoch_time = []
epoch_train_losses = []
epoch_val_losses = []
epoch_train_MAEs = []
epoch_val_MAEs = []

for i in range(10):
    tstart = time.time()
    print(i, '/', 10)
    time.sleep(1)
    for l in [epoch_train_losses, epoch_val_losses, epoch_train_MAEs, epoch_val_MAEs]:
        l.append(np.random.uniform() * 4 / (1 + len(l)))
    per_epoch_time.append(time.time() - tstart)

if hydra.is_available():
    hydra.save_output({'loss': {'train': epoch_train_losses, 'val': epoch_val_losses},
                       'MAE': {'train': epoch_train_MAEs, 'val': epoch_val_MAEs}}, 'history')
    hydra.save_output(
        {'test_MAE': 34.5, 'train_MAE': 23, 'val_MAE': 2 * 8, 'total_time': time.time() - t0,
         'avg_epoch_time': np.mean(per_epoch_time)}, 'summary')
