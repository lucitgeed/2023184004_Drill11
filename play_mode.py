import random

from pico2d import *
import game_framework

import game_world
from grass import Grass
from boy import Boy
from ball import Ball
from zombie import Zombie

# boy = None




def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)

def init():
    global boy

    grass = Grass()
    game_world.add_object(grass, 0)

    boy = Boy()
    game_world.add_object(boy, 1)

    # fill here
    global balls
    balls = [Ball(random.randint(100, 1600 - 100), 60, 0) for _ in range(30)]
    game_world.add_objects(balls, 1)


    #충돌 정보를 등록한다
    game_world.add_collision_pair('boy:ball', boy, None)
    for ball in balls:
        game_world.add_collision_pair('boy:ball',None, ball)
#                                      ^^^^^^^^어떤 충돌인지 ''로 알려줌

    zombies = [Zombie() for _ in range(5)]
    game_world.add_objects(zombies,1)

    ############### 좀비 충돌 정보를 등록
    for zoms in zombies:
        game_world.add_collision_pair('thrown_ball:zombie', None, zoms)

    game_world.add_collision_pair('boy:zombie', boy, None)
    for zoms in zombies:
        game_world.add_collision_pair('boy:zombie', None, zoms)




def finish():
    game_world.clear()
    pass


def update():
    game_world.update()         #소년과 ball의 위치가 모두 업데이트 완료

    game_world.handle_collisions()  #너가 충돌을 처리해줘라 라고 gameworld에게 부탁

#    # fill here 그러므로 여기서 충돌 검사하면 됨
#    for ball in balls.copy():
#        if game_world.collide(boy, ball):
#            print('boy : ball has COLLIDED')
#
#            #충돌 됐으ㅕㅁㄴ
#            #소년 ballcount 증가
#            boy.ball_count += 1
#            #ball을 없애야
#            game_world.remove_object(ball)
#            #^얘는 월드에서 ball을 없애는 것임 = 월드는 layer의 리스트들인데 여기서 없애려면 없으니까 당연히 안지워지고 오류가 나지.
#            #그러면 어디서도 지워야한다? balls라스트에서 없에야지
#
#            balls.remove(ball)
#            #그러나 그냥 작성은 권장하지 않음
#            #얘는 for ball in balls.copy()로 만들어서 반복문 파괴와 관련된 오류가 없도록 복사해서 검사.



def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass

