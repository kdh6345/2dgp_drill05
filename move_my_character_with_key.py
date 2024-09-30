from pico2d import *
#2022184001 Drill 05
open_canvas(1000, 800)
character = load_image('sprite sheet.png')
ground = load_image('TUK_GROUND.png')

running = True
action = False
rightside = True
leftside=False
stop=True
dirx = 0
diry = 0
x = 800 // 2
y = 600 // 2

# 프레임 크기 및 프레임 수 설정
frame_width = 110
frame_height = 144
frame_count = 6

def handle_events():
    global running, dirx, diry, action, rightside

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False

        # 키를 눌렀을 때
        elif event.type == SDL_KEYDOWN:
            action = True
            if event.key == SDLK_RIGHT:

                rightside = True  # 오른쪽으로 이동할 때 오른쪽을 보도록 설정


                dirx += 1
            elif event.key == SDLK_LEFT:

                rightside=False  # 왼쪽으로 이동할 때 왼쪽을 보도록 설정

                dirx -= 1
            elif event.key == SDLK_UP:

                diry += 1
            elif event.key == SDLK_DOWN:
                diry -= 1
            elif event.key == SDLK_ESCAPE:
                running = False

        # 키를 뗐을 때
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dirx -= 1
            elif event.key == SDLK_LEFT:
                dirx += 1
            elif event.key == SDLK_UP:
                diry -= 1
            elif event.key == SDLK_DOWN:
                diry += 1

            # 모든 방향키가 눌리지 않으면 action을 False로 설정
            if dirx == 0 and diry == 0:
                action = False

frame = 0  # 초기 프레임 설정

while running:
    handle_events()

    #영역 경계 설정

    if x < 55:  # 왼쪽 경계를 넘지 않도록
        x = 55

    elif x > 1055 - frame_width:  # 오른쪽 경계를 넘지 않도록
        x = 1055 - frame_width

    if y < 75:  # 아래쪽 경계를 넘지 않도록
        y = 75

    elif y > 875 - frame_height:  # 위쪽 경계를 넘지 않도록
        y = 875 - frame_height

    clear_canvas()
    ground.draw(400, 300)  # 배경 그리기

    if rightside:
    #오른쪽 프레임 출력
        character.clip_draw(10+frame * frame_width, 400, frame_width, frame_height, x, y)
    else:
    #왼쪽 프레임 출력
        character.clip_composite_draw(10+frame * frame_width, 400, frame_width, frame_height, 0, 'h', x, y, frame_width, frame_height)


    update_canvas()

    x += dirx * 20
    y += diry * 20

    if action:
        frame = (frame + 1) % frame_count

    delay(0.05)

close_canvas()
