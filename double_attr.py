import random
data = [
    [0.58, 0.60, 0.61, 0.62, 0.63,0.64, 0.64, 0.65, 0.66, 0.66, 0.67, 0.68],
    [0.60, 0.61, 0.62, 0.63, 0.64, 0.64, 0.65, 0.65, 0.66, 0.68, 0.69, 0.70],
    [0.60, 0.62, 0.63, 0.63, 0.64, 0.65, 0.66, 0.66, 0.66, 0.68, 0.69, 0.70],
    [0.61, 0.63, 0.63, 0.63, 0.64, 0.65, 0.66, 0.66, 0.67, 0.69, 0.70, 0.71],
    [0.61, 0.63, 0.63, 0.64, 0.65, 0.66, 0.66, 0.67, 0.68, 0.69, 0.70, 0.71],
    [0.62, 0.63, 0.63, 0.64, 0.65, 0.66, 0.67, 0.67, 0.68, 0.69, 0.70, 0.71],
    [0.62, 0.63, 0.63, 0.65, 0.66, 0.66, 0.67, 0.67, 0.69, 0.69, 0.70, 0.71],
    [0.62, 0.63, 0.64, 0.65, 0.66, 0.66, 0.67, 0.67, 0.69, 0.69, 0.70, 0.72],
    [0.63, 0.63, 0.65, 0.66, 0.66, 0.67, 0.67, 0.68, 0.69, 0.69, 0.71, 0.72],
    [0.64, 0.64, 0.65, 0.66, 0.66, 0.67, 0.67, 0.69, 0.70, 0.71, 0.71, 0.72],
    [0.64, 0.65, 0.66, 0.66, 0.66, 0.68, 0.68, 0.69, 0.70, 0.71, 0.72, 0.73],
    [0.65, 0.66, 0.66, 0.67, 0.67, 0.68, 0.70, 0.70, 0.71, 0.72, 0.72, 0.74]
]

race = [
    "Orc", 
    "Dragonborn", 
    "Drow", 
    "Halfling", 
    "Half-Orc", 
    "Githyanki",
    "Tiefling", 
    "Human", 
    "Gnome",
    "Dwarf",
    "Elf",
    "Half-Elf"
]

career = [
    "Ranger",
    "Druid",
    "Wizard",
    "Monk",
    "Warlock",
    "Bard",
    "Barbarian",
    "Sorcerer",
    "Fighter",
    "Cleric",
    "Paladin",
    "Rogue",
]

if __name__ == '__main__':
    # Print header
    header = "| Race \\ Class | " + " | ".join(career) + " |"
    print(header)
    
    # Print separator
    separator_parts = ["---"] * len(career)
    separator = "| --- | " + " | ".join(separator_parts) + " |"
    print(separator)
    
    # Print data rows
    for i in range(len(race)):
        row_values = ["{:.2f}".format(val) for val in data[i]]
        row_str = "| " + race[i] + " | " + " | ".join(row_values) + " |"
        print(row_str)

    # Calculate and print Row Averages (Average for each Race)
    print("\n\n### Row Averages (By Race)")
    # Transposing to horizontal table
    header = "| Race | " + " | ".join(race) + " |"
    print(header)
    
    separator = "| --- | " + " | ".join(["---"] * len(race)) + " |"
    print(separator)
    
    averages = []
    for i in range(len(race)):
        if data[i]:
            avg_val = sum(data[i]) / len(data[i])
            averages.append(f"{avg_val:.2f}")
        else:
            averages.append("N/A")
    print("| Average Score | " + " | ".join(averages) + " |")

    # Calculate and print Column Averages (Average for each Class)
    print("\n\n### Column Averages (By Class)")
    # Transposing to horizontal table
    header = "| Class | " + " | ".join(career) + " |"
    print(header)
    
    separator = "| --- | " + " | ".join(["---"] * len(career)) + " |"
    print(separator)
    
    num_rows = len(data)
    num_cols = len(data[0]) if num_rows > 0 else 0
    
    col_averages = []
    for j in range(len(career)):
        if j < num_cols:
            col_sum = sum(data[i][j] for i in range(num_rows))
            avg_val = col_sum / num_rows
            col_averages.append(f"{avg_val:.2f}")
        else:
            col_averages.append("N/A")
            
    print("| Average Score | " + " | ".join(col_averages) + " |")

    # Perturbed Row Averages
    print("\n\n### Perturbed Row Averages (By Race)")
    print(header) # Reuse header from Row Averages sections (Wait, Row Averages header was Race horizontal)
    # Re-construct or reuse headers carefully.
    
    # Row Avg Header
    row_header = "| Race | " + " | ".join(race) + " |"
    print(row_header)
    print(separator) # Re-use compatible separator (same length as race)

    perturbed_averages = []
    for i in range(len(race)):
        if data[i]:
            avg_val = sum(data[i]) / len(data[i])
            # Add noise
            noise = random.gauss(0, 0.0033)
            # Clip noise to [-0.01, 0.01]
            noise = max(min(noise, 0.01), -0.01)
            perturbed_val = avg_val + noise
            perturbed_averages.append(f"{perturbed_val:.2f}")
        else:
            perturbed_averages.append("N/A")
    print("| Average Score | " + " | ".join(perturbed_averages) + " |")

    # Perturbed Column Averages
    print("\n\n### Perturbed Column Averages (By Class)")
    col_header = "| Class | " + " | ".join(career) + " |"
    print(col_header)
    col_separator = "| --- | " + " | ".join(["---"] * len(career)) + " |"
    print(col_separator)

    perturbed_col_averages = []
    for j in range(len(career)):
        if j < num_cols:
            col_sum = sum(data[i][j] for i in range(num_rows))
            avg_val = col_sum / num_rows
            # Add noise
            noise = random.gauss(0, 0.0033)
            noise = max(min(noise, 0.01), -0.01)
            perturbed_val = avg_val + noise
            perturbed_col_averages.append(f"{perturbed_val:.2f}")
        else:
            perturbed_col_averages.append("N/A")
            
    print("| Average Score | " + " | ".join(perturbed_col_averages) + " |")

