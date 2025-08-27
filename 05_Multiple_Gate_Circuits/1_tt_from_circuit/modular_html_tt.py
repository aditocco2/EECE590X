## modular_html_tt( string: results data, int: number of inputs, list[strings]: input labels )
# This function creates a truth table with embedded html using the specified parameters.
# The size will change to match the proper number of inputs in the chosen system. 

def modular_html_tt(s, col_headers):
    import math
    
    # Parameter Filtering
    num_inputs = int(math.log2(len(s)))
    rows, cols = 2**num_inputs, num_inputs+1  # Table dimensions (Without Labels)
    if len(s) != rows:
        return "ERROR - Invalid data string length. Make sure the amount \
                of data string characters is a power of 2."
    
    for char in s:
        if char != '0' and char != '1' and char != 'X' and char != 'x':
            return "ERROR - data string contains invalid character. \
                    Make sure the string contains only '0', '1', 'x' or 'X'"
    
    if len(col_headers) != num_inputs:
        return "ERROR - Invalid quantity of column headers given. Make sure the \
                list contains ONE string for each input"
    
    # Generating input data
    in_data = []
    swap = rows
    for col in range(num_inputs):
        sublist = []
        swap = swap/2
        flag = 1
        for i in range(rows):
            if i%swap==0:
                flag ^= 1
            sublist.append(f"{flag}")
        in_data.append(sublist)
    
    # Constant Definitions
    w = 30
    h = 30
    ph = w/2
    pd = w/3
    border_style = "2px solid black"
    special_border_style = "4px solid black"

    # Styling for "Zebra Striped" table
    table = "<style>tr:nth-child(even) {\nbackground-color: #E6E6E6;\n}\n</style>\n"
    
    # Table declaration and adding the column labels
    table += "<table style='border-collapse: collapse;'>\n<tr>\n"
    for label in col_headers:
        table += f"    <th style='width: {w}px; height: {h}px; text-align: center; \
                padding: {ph}px; border: {border_style};'>{label}</th>\n"
    table += f"    <th style='width: {w}px; height: {h}px; text-align: center; padding: \
            {ph}px; border: {border_style}; border-left: {special_border_style};'>Result</th>\n"
    table += "  </tr>\n"
  
    # Filling in the table
    for r in range(rows):
        table += "  <tr>\n"
        for col in in_data:
            table += f"    <td style='width: {w}px; height: {h}px; text-align: center;\
                    padding: {pd}px; border: {border_style};'>{col[r]}</td>\n"
        
        index = r
        char = s[index] if index < len(s) else "&nbsp;"
        table += f"    <td style='width: {w}px; height: {h}px; text-align: center; padding: {pd}px; \
                border: {border_style}; border-left: {special_border_style};'>{char}</td>\n"
        table += "  </tr>\n"
    
    table += "</table><p>\n\n</p>"
    return table

# # Example usage
# html_output = modular_html_tt("011X11X01X11X001", ["A", "B", "C", "D"])
# print(html_output)
# html_output2 = modular_html_tt("00X1", ["F", "G"])
# print(html_output2)
# with open("output2.html", "w") as file:
#     file.write(html_output)
#     file.write(html_output2)
