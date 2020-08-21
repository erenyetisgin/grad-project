# smart-traffic-lights
This is a graduation project that aimed timing of traffic lights dynamically according to the feed of cameras that can see the cars on the intersection.

First part of the project is detection and counting of the cars in a video. We tried two methods for this part: image processing and a deep learning model. We used OpenCV on Python for image processing and YOLOv3 as a deep learning model. For image processing, we used background-subtraction to detect cars and improved accuracy a bit by using morphological operations.

Second part is about optimizing the traffic lights durations. While we had no means to connect the first part to this one, we made a simple intersection simulation matrix to imitate cars on an intersection and used an algorithm for the lights durations.
