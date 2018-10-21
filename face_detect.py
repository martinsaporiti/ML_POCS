import cv2
import sys

try:
    imagePath = sys.argv[1]
    scaleFactor = float(sys.argv[2])
    # cascPath = sys.argv[2]
    # cascPath = "/usr/local/Cellar/opencv/3.4.3/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml"
    cascPath = "haarcascade_frontalface_default.xml"

    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier(cascPath)

    # Read the image
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor = scaleFactor,
        minNeighbors = 5,
        minSize = (30, 30),
        flags = 0
    )

    print("Found {0} faces!".format(len(faces)))

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)


    cv2.imshow("Faces found", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
except Exception as e:
    print('Los parámetros que deben enviarse son: \n(1) el path de la imagen \n(2) el factor de escala (float).')
    print('Detalle del error: ', e)


