from PIL import Image, ImageFilter

def main():
    input_path = "books/back_cover.png"
    output_path = "books/back_cover_epub.png"
    
    # Target dimensions (1:1.6 ratio, high res)
    target_width = 1600
    target_height = 2560
    
    try:
        img = Image.open(input_path)
        print(f"Original size: {img.size}")
        
        # 1. Create the background (Blurred version)
        # Resize to fill the height to ensure coverage
        # Aspect ratio of target is 0.625. Aspect ratio of img is 1.
        # To fill height 2560, width needs to be 2560 (since img is square).
        bg_size = (target_height, target_height)
        background = img.resize(bg_size, Image.Resampling.LANCZOS)
        
        # Crop to target width
        left = (background.width - target_width) / 2
        top = 0
        right = (background.width + target_width) / 2
        bottom = target_height
        background = background.crop((left, top, right, bottom))
        
        # Blur it
        background = background.filter(ImageFilter.GaussianBlur(radius=50))
        
        # Darken it slightly to make the foreground pop
        # (Optional, but looks better)
        from PIL import ImageEnhance
        enhancer = ImageEnhance.Brightness(background)
        background = enhancer.enhance(0.6)
        
        # 2. Prepare the foreground (The actual cover)
        # Resize to fit width (with some padding maybe? or full width?)
        # Let's do full width (1600)
        fg_width = target_width
        fg_height = int(fg_width * img.height / img.width)
        foreground = img.resize((fg_width, fg_height), Image.Resampling.LANCZOS)
        
        # 3. Paste foreground onto background
        # Center vertically
        y_pos = (target_height - fg_height) // 2
        background.paste(foreground, (0, y_pos))
        
        # Save
        background.save(output_path)
        print(f"✅ Created {output_path} ({target_width}x{target_height})")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
