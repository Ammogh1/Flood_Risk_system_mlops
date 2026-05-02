import os
import numpy as np
import pandas as pd
from PIL import Image

def generate_dummy_tabular_data(num_samples=1000):
    """Generates dummy tabular data for ML and QML models."""
    np.random.seed(42)
    # Features: Rainfall (mm), Humidity (%), Temperature (C), River Level (m)
    rainfall = np.random.uniform(0, 500, num_samples)
    humidity = np.random.uniform(30, 100, num_samples)
    temperature = np.random.uniform(10, 45, num_samples)
    river_level = np.random.uniform(1, 15, num_samples)
    
    # Simple rule for flood risk: 
    # High rainfall + high river level + high humidity = High risk (1)
    risk_score = (rainfall / 500) * 0.4 + (river_level / 15) * 0.4 + (humidity / 100) * 0.2
    labels = (risk_score > 0.5).astype(int)
    
    df = pd.DataFrame({
        'Rainfall': rainfall,
        'Humidity': humidity,
        'Temperature': temperature,
        'River_Level': river_level,
        'Flood_Risk': labels
    })
    
    os.makedirs('data', exist_ok=True)
    df.to_csv('data/dummy_tabular_data.csv', index=False)
    return df

def generate_dummy_images(num_samples=100):
    """Generates dummy colored images for CNN model."""
    os.makedirs('data/images/flood', exist_ok=True)
    os.makedirs('data/images/no_flood', exist_ok=True)
    
    for i in range(num_samples // 2):
        # Flood images (bluish/brownish)
        img_flood = np.random.randint(50, 150, (64, 64, 3), dtype=np.uint8)
        img_flood[:, :, 2] = np.random.randint(150, 255, (64, 64)) # More blue
        Image.fromarray(img_flood).save(f'data/images/flood/img_{i}.jpg')
        
        # No flood images (greenish)
        img_no_flood = np.random.randint(50, 150, (64, 64, 3), dtype=np.uint8)
        img_no_flood[:, :, 1] = np.random.randint(150, 255, (64, 64)) # More green
        Image.fromarray(img_no_flood).save(f'data/images/no_flood/img_{i}.jpg')

if __name__ == "__main__":
    print("Generating dummy data...")
    generate_dummy_tabular_data()
    generate_dummy_images()
    print("Data generation complete.")
