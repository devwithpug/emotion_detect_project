# 프로젝트 5주차

(2021.04.11 14:00 ~ 18:00)

***

# 학습 내용
정확도 향상을 목표로 신경망 모델을 개선한다.
[참고자료1](https://github.com/Conero007/Emotion-Detection-Pytorch.git)
[참고자료2](https://github.com/omar178/Emotion-recognition.git)
[참고자료3](https://github.com/oarriaga/face_classification.git)
[참고자료4](https://mindcompass.github.io/multicampus/project3_3_emotion_detector/)
[참고자료5](https://medium.com/swlh/emotion-detection-using-pytorch-4f6fbfd14b2e)
[참고자료6](https://github.com/omar178/Emotion-recognition)
[참고자료7](https://github.com/petercunha/Emotion)

# 문제 인식 / 원인 분석 / 해결
오류
![image](https://user-images.githubusercontent.com/79958455/114297997-ff3cca00-9aee-11eb-9a6f-d6115c0913e9.png)
1. 텐서 크기와 BatchNorm2d 크기 맞춰 해결
    ex) 32로 맞춰주기 => self.conv1 = nn.Conv2d(3, 32, 3) // self.bn_32 = nn.BatchNorm2d(32) 
2. 인접한 신경망 사이즈 연결 되게 값 수정하여 해결
    ex) self.conv1 = nn.Conv2d(3, 32, 3)
        self.conv2 = nn.Conv2d(32, 32, 3)
        self.conv3 = nn.Conv2d(32, 64, 3)
        self.conv4 = nn.Conv2d(64, 64, 3)

# 결과
![image](https://user-images.githubusercontent.com/79958455/114298178-0d3f1a80-9af0-11eb-94f5-27e10087fbc6.png)


## 다음 주. . .
- 신경망 모델 개선하여 정확도 향상