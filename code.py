from adafruit_circuitplayground.express import cpx

# Main loop gets x, y and z axis acceleration, prints the values, and turns on
# red, green and blue, at levels related to the x, y and z values.
tones = 0
while True:
    if cpx.switch:
        print("Slide switch off!")
        cpx.pixels.fill((0, 0, 0))
        continue
    else:
        R = 0
        G = 0
        B = 0
        x, y, z = cpx.acceleration
        print((x, y, z))
        if x:
            R = R + abs(int(x))
            if x < 0:
                tones = 261
        if y:
            G = G + abs(int(y))
            if y > 0:    
                tones = 277
        if z:
            B = B + abs(int(z))
            if z < 0:    
                tones = 311
        cpx.pixels.fill((R, G, B))
        cpx.play_tone(tones, 2)
