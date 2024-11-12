from os import remove

world = [[] for _ in range(4)]
collision_pairs = {} #빈 딕셔너리 {key: [[A list] [B list]]}

def add_collision_pair(group, a, b):
    if group not in collision_pairs:        #group인 key가 없다면
        collision_pairs[group] = [ [],[] ]  #리스트를 초기화

   #a,b가 있을때만 추가 하는 것(None을 줘도 되도록)
    if a:
        collision_pairs[group][0].append(a)
    if b:
        collision_pairs[group][1].append(b)
    pass


def add_object(o, depth = 0):
    world[depth].append(o)

def add_objects(ol, depth = 0):
    world[depth] += ol


def update():
    for layer in world:
        for o in layer:
            o.update()


def render():
    for layer in world:
        for o in layer:
            o.draw()


###############################
def remove_collision_object(o):
    for pairs in collision_pairs.values():
        if o in pairs[0]:
            pairs[0].remove(o)
        if o in pairs[1]:
            pairs[1].remove(o)
    pass


def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)              #월드에서 o객체를 삭제
            remove_collision_object(o)   #여기서도 o객체를 삭제= collision pairs에 등록된 객체o를 날린다
                                         # = 리스트에 있는건 날아갔지만 메모리에 있는 객체는 남아있음
            del o                        #그러므로 메모리에 남아있는 객체 자체까지도 삭제
            return
    raise ValueError('Cannot delete non existing object')
###############################


def clear():
    for layer in world:
        layer.clear()



# fill here
def collide(a, b):
    aleft, abottom, aright, atop = a.get_bb()
    bl, bb, br, bt = b.get_bb()

    if aright < bl: return False
    if aleft > br: return False
    if atop < bb: return False
    if abottom > bt : return False

    return True     #4개의 위의 조건을 빗겨가면 충돌한 것이다 True
    pass


def handle_collisions():
    #게임월드에 등록된 충돌 정보를 바탕으로, 실제 충돌 검사를 수행
    #어디에?    collision_pairs 여기에
    for group, pairs in collision_pairs.items():
        for a in pairs[0]:                          # A 리스트에서 하나를 뽑고
            for b in pairs[1]:                      # B 리스트에서 하나 뽑아서 두 객체를 갖고와서
                if collide(a,b):                    # 충돌처리 수행
                    print(f'        {group} has collided')
                                                    #객체 지향적으로 객체에게 스스로 충돌 처리하라고 요청
                    a.handle_collision(group, b)    #왜 발생한 충돌인지group알려주고,
                    b.handle_collision(group, a)    #누구랑 충돌했는지a,b를 알려준다.
    pass
