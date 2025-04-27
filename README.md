# Panda Pigment

A Python library for styling pandas DataFrames with beautiful, customizable themes.

## Installation

```bash
pip install panda-pigment
```

## Usage

```python
import pandas as pd
from panda_pigment import style_df

# Create a sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

# Apply default styling
style_df()

# Display the DataFrame
df
```

## Customization

You can customize the styling by passing different parameters:

```python
style_df(
    header_bg="rgb(0,38,70)", 
    header_color="white",
    row_even_bg="rgb(27,45,65)", 
    row_odd_bg="rgb(15,15,15)",
    row_even_color="rgb(225,225,225)",
    row_odd_color="rgb(190,190,190)",
    border_color="rgba(255,255,255,0.1)",
    font_size="12px",
    text_output="cyan",
    header_size="14px",
    header_font_weight="bold",
    header_font_style="italic"
)
```

## Parameters

- `header_bg`: Background color for the header row
- `header_color`: Text color for the header row
- `row_even_bg`: Background color for even rows
- `row_odd_bg`: Background color for odd rows
- `row_even_color`: Text color for even rows
- `row_odd_color`: Text color for odd rows
- `border_color`: Color of the table borders
- `font_size`: Font size for the table content
- `text_output`: Color of the output text
- `header_size`: Font size for the header row
- `header_font_weight`: Font weight for the header row (e.g., "bold", "normal")
- `header_font_style`: Font style for the header row (e.g., "italic", "normal") 