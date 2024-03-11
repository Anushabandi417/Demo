def move_disks(num_disks, pillar1, pillar2,pillar3):
    if num_disks == 1:
        c[0]+=1
        print(f"Move ring 1 from pillar {pillar1} to pillar {pillar2}")
        return
    move_disks(num_disks - 1, pillar1, pillar3, pillar2)
    c[0]+=1
    print(f"Move ring {num_disks} from pillar {pillar1} to pillar {pillar2}")
    move_disks(num_disks - 1, pillar3, pillar2, pillar1)
num_disks = 7
c=[0]
move_disks(num_disks, "1", "2", "3")
print(c[0])
