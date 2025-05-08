from PIL import Image, ImageDraw
import math

class ColorAtlasGenerator:
    def __init__(self, colors):
        # Clean and format colors to ensure "#RRGGBB" format.
        self.colors = [color.strip() for color in colors if color.strip()]
        self.colors = [color if color.startswith("#") else f"#{color}" for color in self.colors]

    def create_png(self, canvas_width, canvas_height, output_file="color_atlas.png", progress_callback=None):
        num_colors = len(self.colors)
        if num_colors == 0:
            print("No colors provided.")
            return

        # Calculate grid dimensions.
        # Use the canvas aspect ratio to guess a grid that fits the colors
        aspect_ratio = canvas_width / canvas_height
        grid_cols = math.ceil(math.sqrt(num_colors * aspect_ratio))
        grid_rows = math.ceil(num_colors / grid_cols)

        # Compute cell width and height so the grid fills the entire canvas.
        cell_width = canvas_width / grid_cols
        cell_height = canvas_height / grid_rows

        # Create new image with a white background.
        image = Image.new("RGB", (canvas_width, canvas_height), "white")
        draw = ImageDraw.Draw(image)

        # Draw each color block in its computed cell.
        for idx, color in enumerate(self.colors):
            col = idx % grid_cols
            row = idx // grid_cols
            x0 = int(col * cell_width)
            y0 = int(row * cell_height)
            x1 = int((col + 1) * cell_width)
            y1 = int((row + 1) * cell_height)
            try:
                draw.rectangle([x0, y0, x1 - 1, y1 - 1], fill=color)
            except Exception as e:
                print(f"Error drawing rectangle with color {color}: {e}")
                
            # Update progress
            if progress_callback:
                progress = ((idx + 1) / num_colors) * 100
                progress_callback(progress)

        image.save(output_file)
        print(f"Color atlas saved as {output_file}")