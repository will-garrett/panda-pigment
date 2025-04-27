from IPython.display import display, HTML

def style_df(header_bg="rgb(0,38,70)", 
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
            header_font_style="normal"
            ):
    """
    Apply custom styling to pandas DataFrames in Jupyter notebooks.
    
    Parameters:
    -----------
    header_bg : str
        Background color for the header row
    header_color : str
        Text color for the header row
    row_even_bg : str
        Background color for even rows
    row_odd_bg : str
        Background color for odd rows
    row_even_color : str
        Text color for even rows
    row_odd_color : str
        Text color for odd rows
    border_color : str
        Color of the table borders
    font_size : str
        Font size for the table content
    text_output : str
        Color of the output text
    header_size : str
        Font size for the header row
    header_font_weight : str
        Font weight for the header row (e.g., "bold", "normal")
    header_font_style : str
        Font style for the header row (e.g., "italic", "normal")
    """
    display(HTML("<style>.container { width:100% !important; }</style>"))
    display(HTML("<style>div.output_scroll { height: 1000px; }</style>"))
    display(HTML(f"<style>.output {{color: {text_output};}}</style>"))
    display(
        HTML(
            f"<style>table.dataframe, .dataframe td {{border: 1px solid {border_color}; color: black;font-size:{font_size};}}</style>"
        )
    )
    display(
        HTML(
            f"<style>table.dataframe tr:nth-child(even) {{background-color: {row_even_bg}; color: {row_even_color};}} table.dataframe tr:nth-child(even) td {{ color: {row_even_color}; }}</style>"
        )
    )
    display(
        HTML(
            f"<style>table.dataframe tr:nth-child(odd) {{background-color: {row_odd_bg}; color: {row_odd_color};}} table.dataframe tr:nth-child(odd) td {{ color: {row_odd_color}; }}</style>"
        )
    )
    display(
        HTML(
            f"<style>.dataframe th {{background-color: {header_bg}; border: 1px solid {border_color};color: {header_color}; font-size: {header_size}; font-weight: {header_font_weight}; font-style: {header_font_style};}}</style>"
        )
    ) 