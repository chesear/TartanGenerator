import math
from PIL import Image

def set_params():
  width: int = 400
  height: int = 400
  scale_factor: int = 15

  color_dict = get_color_dict()
  horz_pattern = [
                  color_dict["blue"], 
                  color_dict["green"], 
                  color_dict["white"]
                  ]
  vert_pattern = [
                  color_dict["white"], 
                  color_dict["green"], 
                  color_dict["blue"]
                  ]
  return width, height, scale_factor, horz_pattern, vert_pattern

def create_image(width: int, height: int):
  img = Image.new('RGB', (width, height))
  return img

def choose_orientation(w_ind, h_ind) -> str:
  w_rem = w_ind % 4
  h_rem = h_ind % 4
  if (w_rem == h_rem or w_rem == h_rem + 1):
    return "horz"
  else:
    return "vert"

def choose_color(v_pattern, h_pattern, w_ind, h_ind, w, h):
  orientation = choose_orientation(w, h)

  pattern = v_pattern if orientation == "vert" else h_pattern
  ind = w_ind if orientation == "vert" else h_ind
  return pattern[ind % len(pattern)]

def colorize_image(img, horz_pattern, vert_pattern, scale_factor):
  width, height = img.size
  print("Width: {} | Height: {} | Scale Factor: {}"
    .format(width, height, scale_factor))
  print("Horz Pattern: {}".format(horz_pattern))
  print("Vert Pattern: {}".format(vert_pattern))

  for w in range(width):
    for h in range(height):
      w_floor = math.floor(w / scale_factor)
      h_floor = math.floor(h / scale_factor)
      color = choose_color(vert_pattern, horz_pattern, w_floor, h_floor, w, h)
      img.putpixel((w, h), color)

def get_color_dict():
  color_dict = {
      "red": (255, 0, 0),
      "blue": (0, 0, 255),
      "green": (0, 255, 0),
      "white": (255, 255, 255),
      "gray": (150, 150, 150),
      "tan": (194, 158, 114)
  }
  return color_dict

def main():
  print("heya!")
  width, height, scale_factor, horz_pattern, vert_pattern = set_params()
  img = create_image(width, height)

  colorize_image(img, horz_pattern, vert_pattern, scale_factor)

  img.save("/tmp/output-images/output.png")
  print("Done!")

if __name__ == "__main__":
    main()
