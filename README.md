# Visualise spacy pattern

## Installation

```bash
pip install visualise-spacy-pattern
```

## Usage

```python
import visualise_spacy_pattern

# Load the example dependency pattern
pattern_file = 'examples/pattern_1.json'
with open(pattern_file) as f:
    pattern = json.load(f)

graph = visualise_spacy_pattern.to_pydot(pattern)
png = graph.create_png()
graph_file = 'examples/graph_1.png'.format()
with open(graph_file, 'wb') as f:
    f.write(png)
```