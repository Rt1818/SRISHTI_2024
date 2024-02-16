import fiftyone as fo
import fiftyone.zoo as foz

dataset = fo.zoo.load_zoo_dataset(
              "open-images-v7",
              split="validation",
              label_types=["detections", "segmentations", "points"],
              classes=["Bird"],
              max_samples=100,
          )