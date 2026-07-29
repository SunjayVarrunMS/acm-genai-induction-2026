# Project Sentinel — Eyes of the Highway Reserve

Land-cover classification for the (fictional) highway-reserve satellite feed, using EuroSAT (Sentinel-2 RGB, 10 classes) as a stand-in dataset.

## What's here

`Project_Sentinel_EuroSAT.ipynb` trains and compares four models:

| Run | Model | Augmentation |
|---|---|---|
| `scratch_no_aug` | TinyVGG (from scratch) | no |
| `scratch_aug` | TinyVGG (from scratch) | yes |
| `pretrained_no_aug` | ResNet-18 (fine-tuned) | no |
| `pretrained_aug` | ResNet-18 (fine-tuned) | yes |

Augmentation = random horizontal/vertical flip + small rotation. Normalization uses EuroSAT's own computed mean/std for the scratch CNN, and ImageNet stats for the fine-tuned ResNet.

## How to run

1. Open the notebook in Google Colab.
2. `Runtime → Change runtime type → T4 GPU`.
3. `Runtime → Run all`. The dataset downloads automatically via `torchvision.datasets.EuroSAT` (same RGB Sentinel-2 data as the Kaggle version linked in the brief — no Kaggle API key needed).

## Results

_Fill in after running: final test accuracy per run (see the `summary` table, section 7), and a confusion-matrix screenshot (`confusion_matrices.png`, generated in the last cells of section 7)._

| Run | Test accuracy | Test loss |
|---|---|---|
| scratch_no_aug | | |
| scratch_aug | | |
| pretrained_no_aug | | |
| pretrained_aug | | |

## Colab link

_Paste the Colab link here after uploading/running._
