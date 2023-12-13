import cv2 as cv
import cv2.data
import pandas as pd
from sklearn import datasets, svm
from sklearn.model_selection import train_test_split
from Resizing import resizing
#task 1

class DetectFace:
    def __init__(self, file_path):
        self.file_path = file_path
        self.frame = None


    def open_pic(self):
        self.frameframe = cv.imread(self.file_path)
        if self.frameframe is None:
            raise Exception('Фото нет')


    def workpic(self):
        face_cascade = cv.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        eyes_cascade = cv.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
        frame_gray = cv.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
        frame_gray = cv.equalizeHist(frame_gray)
        faces = face_cascade.detectMultiScale(frame_gray)
        for (x, y, w, h) in faces:
            center = (x + w//2, y + h//2)
            self.frame = cv.ellipse(self.frame, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)
            face_ROI = frame_gray[y:y+h, x:x+w]
            eyes = eyes_cascade.detectMultiScale(face_ROI)
            for (x2, y2, w2, h2) in eyes:
                eye_center = (x + x2 + w2//2, y + y2 + h2//2)
                radius = int(round((w2 + h2)*0.25))
                self.frame = cv.circle(self.frame, eye_center, radius, (255, 0, 0), 4)
                self.frame =resizing(self.frame, 600)

    def show_video(self):
        camera_device = 0
        cap = cv.VideoCapture(camera_device)
        if not cap.isOpened:
            raise Exception ('Error')
        while True:
            read, frame = cap.read()
            if not read:
                raise Exception ('Error')
            if cv.waitKey(10) == ord('q'):
                break


    def show_pic(self):
        cv2.imshow('Img', self.frame)
        cv2.waitkey(0)

processor = DetectFace("C:/Users/Kukushkin/PycharmProjects/game/hw_task_7/irgups.png")

processor.open_pic()

processor.workpic()
processor.show_pic()
processor.show_video()




#task 2
df = pd.read_csv('C:/Users/Kukushkin/Desktop/titanic.csv')
model = svm.SVC()

df.drop(['Name', 'Ticket', 'Cabin', 'Embarked'], axis=1, inplace=True)
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
df = df.dropna()

X = df.drop('Survived', axis=1)
y = df['Survived']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, shuffle = False)

model.fit(X_train, y_train)
pred = model.predict(X_test[0:10])


y_test = y_test[0:10]
# print(pred)
# print(y_test)
