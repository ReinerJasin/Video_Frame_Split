import cv2

capture = cv2.VideoCapture('video/magic-nets-game.mp4')
print(capture)


frameIndex = 0
frameState = 0
frameIncrementValue = 1

# while (True):
#     success, frame = capture.read()

#     capture.set(cv2.CAP_PROP_FPS, 10)
#     if success:
#         if frameState % frameIncrementValue == 0:
#             fps = capture.get(cv2.CAP_PROP_FPS)
#             print(fps)

#             cv2.waitKey(100)

#             cv2.imwrite(f'./output/frame_{frameIndex}.jpg', frame)
            
#             # Only for naming system
#             frameIndex += 1

#         frameState += 1
        
#     else:
#         break

fps_in = capture.get(cv2.CAP_PROP_FPS)
fps_out = 0.5

index_in = -1
index_out = -1

while True:

    # DEBUG
    print(f'frame index : {frameIndex}')
    print(f'fps_in : {fps_in}')
    print(f'fps_out : {fps_out}')
    print(f'index_in : {index_in}')
    print(f'index_out : {index_out}')
    print("")

    if(frameIndex == 5):
        break

    success = capture.grab()
    if not success: break
    index_in += 1

    out_due = int(index_in / fps_in * fps_out)
    if out_due > index_out:
        success, frame = capture.retrieve()
        if not success: break
        index_out += 1
        
        cv2.imwrite(f'./output/frame_{frameIndex}.jpg', frame)
        frameIndex += 1

capture.release()