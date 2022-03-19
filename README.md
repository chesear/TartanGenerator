# TartanGenerator
Python script to generate woven tartan patterns

## Input
| **Param** | **Type** | **Notes** |
|-----------|----------|-----------|
| Image width | int | pixels |
| Image height | int | pixels |
| Scale factor | int | pixel width of most narrow stripe, or unit factor |
| Horizontal stripe pattern | array of valid colors | [color_dict["red"], color_dict["white"], color_dict["blue"]] |
| Vertical stripe pattern | array of valid colors | [color_dict["red"], color_dict["white"], color_dict["blue"]] |

## Output
| **Output** |
|------------|
| PNG image with a tartan weave |

## Hard-codings
Valid input colors are defined by RGB values in the get_color_dict() method.  Once a color has been added to the dictionary, it can be referenced as part of a stripe pattern.

## Next Steps
- User interface - webapp?
- GUI interface color input or color chooser
- Display image after creation
- Image download option after creation
- Flexibility of stripe pattern input - rather than [red, red, blue] move to something like [2red, 1blue]

## Project History
Due to difficulties installing the Pillow image library, development was moved to a Google Colab notebook (https://colab.research.google.com/drive/15rsTJc-Ibk6oiaGGGQJeFmThN1wLcGvT#scrollTo=iSdArdQ5rXTw).
