import cv2

def draw_dashboard(frame, counts, total, entry, exit):

    cv2.rectangle(frame,(10,10),(310,280),(35,35,35),-1)

    y = 40

    cv2.putText(frame,"SMARTVISION AI",(20,y),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0,255,255),
                2)

    y += 40

    for name,value in counts.items():

        cv2.putText(
            frame,
            f"{name.capitalize()} : {value}",
            (20,y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0,255,0),
            2
        )

        y += 30

    y += 10

    cv2.putText(frame,
                f"Total : {total}",
                (20,y),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (255,255,255),
                2)

    y += 30

    cv2.putText(frame,
                f"Entry : {entry}",
                (20,y),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (255,255,0),
                2)

    y += 30

    cv2.putText(frame,
                f"Exit : {exit}",
                (20,y),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (255,255,0),
                2)


def draw_line(frame, y):

    cv2.line(
        frame,
        (0,y),
        (frame.shape[1],y),
        (0,0,255),
        3
    )