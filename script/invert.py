from colorcodetools.hex import invert

def invert_theme():
    name_count = 0
    target_file = open('../themes/IntrepidDarknessLight.json', 'w')
    with open('../themes/IntrepidDarkness.json', 'r') as f:
        for e in f.readlines():
            try:
                line_splitted = e.split("#")
                color_code = line_splitted[1]
                if ',' not in e:
                    color_code = color_code.replace('"\n', '')
                    inverted_color = invert.invert_hex('#' + color_code)
                    target_file.write(line_splitted[0] + inverted_color + '"\n')
                else:
                    color_code = color_code.replace('",\n', '')
                    inverted_color = invert.invert_hex('#' + color_code)
                    target_file.write(line_splitted[0] + inverted_color + '",\n')

            except:
                if '"type":' in e.strip():
                    e = e.replace("dark", "light")
                    target_file.write(e)
                    continue
                if '"name":' in e.strip() and name_count == 0:
                    e = e.replace("Intrepid Darkness", "Intrepid Darkness Light")
                    target_file.write(e)
                    name_count += 1
                    continue
                target_file.write(e)
    f.close()
    target_file.close()

invert_theme()