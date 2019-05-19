# Melih Safa Çelik  010180519 

def traverse_area_519(coordinate_list_519):
    area_list_519 = []
    for var_519 in range(len(coordinate_list_519)-2):
        pts_519 = ((coordinate_list_519[var_519][0]*coordinate_list_519[var_519+1][1])-(coordinate_list_519[var_519][1]*coordinate_list_519[var_519+1][0]))
        area_list_519.append(pts_519)
    calculate_doublef_519 = sum(area_list_519)
    area_519 = calculate_doublef_519 / 2
    return area_519