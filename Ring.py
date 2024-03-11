def move_rings(num_rings, pillar1, to_pillar, aux_pillar):
    if num_rings == 1:
        c[0]+=1
        print(f"Move ring 1 from pillar {pillar1} to pillar {to_pillar}")
        return
    move_rings(num_rings - 1, pillar1, aux_pillar, to_pillar)
    c[0]+=1
    print(f"Move ring {num_rings} from pillar {pillar1} to pillar {to_pillar}")
    move_rings(num_rings - 1, aux_pillar, to_pillar, pillar1)
num_rings = 7
c=[0]
move_rings(num_rings, "1", "3", "2")
print(c[0])
