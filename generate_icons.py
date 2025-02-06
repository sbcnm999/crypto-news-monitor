from PIL import Image, ImageDraw
import os

def create_icon(size, filename, is_maskable=False):
    # Create a new image with a white background
    image = Image.new('RGB', (size, size), 'white')
    draw = ImageDraw.Draw(image)
    
    # Draw a blue circle for the icon background
    circle_size = size * 0.8
    circle_pos = (size - circle_size) / 2
    draw.ellipse(
        [circle_pos, circle_pos, circle_pos + circle_size, circle_pos + circle_size],
        fill='#0175C2'
    )
    
    # Draw the "CN" text in white
    font_size = int(size * 0.4)
    draw.text(
        (size/2, size/2),
        "CN",
        fill='white',
        anchor="mm",
        font=None,  # Using default font
        font_size=font_size
    )
    
    # Save the icon
    os.makedirs('icons', exist_ok=True)
    image.save(f'icons/{filename}')

# Generate icons
sizes = [192, 512]
for size in sizes:
    create_icon(size, f'icon-{size}.png')
    create_icon(size, f'icon-maskable-{size}.png', True)
