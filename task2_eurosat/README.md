# Project Sentinel (Eyes of the Highway Reserve)

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

Run locally (Python 3.12, GPU used automatically if available) or in Colab; the notebook in this repo already has all cells executed with real outputs. `Runtime → Change runtime type → T4 GPU` if using Colab, then `Runtime → Run all`. The dataset downloads automatically via `torchvision.datasets.EuroSAT` (same RGB Sentinel-2 data as the Kaggle version linked in the brief, no Kaggle API key needed).

## Results

Held-out test set (4,050 tiles), see the `summary` table and `confusion_matrices.png` in section 7, and the full write-up in section 8's field report:

| Run | Test accuracy | Test loss |
|---|---|---|
| pretrained_aug | 0.9807 | 0.0566 |
| pretrained_no_aug | 0.9637 | 0.1471 |
| scratch_aug | 0.9402 | 0.2035 |
| scratch_no_aug | 0.9284 | 0.2954 |

Augmentation improved both architectures (scratch CNN +1.18 points, fine-tuned ResNet +1.70 points). Without augmentation, the fine-tuned model most often confuses Highway and River tiles, both narrow linear features that the model can otherwise tell apart mainly by orientation; augmentation fixes most of this. See section 8 of the notebook for the full analysis and pipeline recommendation.

## Colab link

Run locally rather than in Colab; the notebook in this repo already contains the full executed run with real outputs.
