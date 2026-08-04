import cv2

icons = {
    "car":"CAR",
    "bus":"BUS",
    "truck":"TRUCK",
    "person":"PERSON",
    "motorcycle":"BIKE"
}


def draw_dashboard(frame, counts, total, fps):

    cv2.rectangle(frame,(10,10),(330,300),(35,35,35),-1)

    cv2.putText(
        frame,
        "SMARTVISION AI",
        (20,40),
        cv2.FONT_HERSHEY_DUPLEX,
        0.8,
        (0,255,255),
        2
    )

    cv2.line(frame,(15,55),(320,55),(255,255,255),1)

    y=90

    order=[
        "car",
        "bus",
        "truck",
        "motorcycle",
        "person"
    ]

    colors={
        "car":(0,255,0),
        "bus":(0,165,255),
        "truck":(255,0,255),
        "motorcycle":(0,255,255),
        "person":(255,0,0)
    }

    for cls in order:

        count=counts.get(cls,0)

        cv2.putText(
            frame,
            f"{icons[cls]} : {count}",
            (20,y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            colors[cls],
            2
        )

        y+=35

    cv2.line(frame,(15,240),(320,240),(255,255,255),1)

    cv2.putText(
        frame,
        f"TOTAL : {total}",
        (20,270),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255,255,255),
        2
    )

    cv2.putText(
        frame,
        f"FPS : {fps:.1f}",
        (170,270),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0,255,255),
        2
    )