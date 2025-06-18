<!-- [![PyPi]()]() -->
[![GitHub issues](https://img.shields.io/badge/issue_tracking-github-blue.svg)](https://github.com/faridrodriguez/model-stability/issues)
![model-stability logo](assets/logo.svg)

Tools for stable ML models.

## Installation

Install via pip:

```bash
pip install .
```

## Usage

The main function provided is `stability_index`, which evaluates the stability of a sequence of metric values (e.g., accuracy over time or epochs).

### Example

```python
from modstablib.metrics._performance import stability_index

# Example: accuracy values over epochs
metric_vector = [0.85, 0.86, 0.84, 0.83, 0.82]

score = stability_index(metric_vector)
print(f"Stability index: {score}")
```

#### Parameters
- `metric_vector`: Sequence (list, numpy array, etc.) of metric values to evaluate stability.
- `falling_rate_weight`: (optional, default=12) Weight for penalizing negative trend (slope).
- `variability_weight`: (optional, default=0.5) Weight for penalizing variability (standard deviation of residuals).

#### Returns
- A float: Higher values indicate greater stability (less decrease and less variability).

## License
MIT

## Issues
For questions or issues, please use the [GitHub issue tracker](https://github.com/faridrodriguez/model-stability/issues).