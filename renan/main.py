car_brands = ["bmw ", "ferari", "mclaren", "  toyoya  ", "  ford "]


def normalize_brands(brand_list):
    normalize_brands = []
    for brand in brand_list:
        brand = brand.strip()
        brand = brand.lower()
        normalize_brands.append(brand)
    return normalize_brands


print(normalize_brands(car_brands))
